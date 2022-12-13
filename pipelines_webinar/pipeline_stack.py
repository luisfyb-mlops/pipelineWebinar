# SPDX-License-Identifier: MIT-0
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from aws_cdk import Stack, pipelines, SecretValue
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from constructs import Construct


class PipelineStack(Stack):
    def __init__(self, scope: Stack, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        input_ = pipelines.CodePipelineSource.git_hub(
            repo_string="luisfyb-mlops/pipeline-webinar",
            branch="main",
            authentication=SecretValue.secrets_manager("github-token"),
            trigger=cpactions.GitHubTrigger.POLL,
        )

        pipeline = pipelines.CodePipeline(
            self,
            id="Pipeline",
            pipeline_name="WebinarPipeline",
            self_mutation=True,
            docker_enabled_for_synth=True,
            docker_enabled_for_self_mutation=True,
            synth=pipelines.ShellStep(
                "Synth",
                input=input_,
                commands=["npm install -g aws-cdk", "pip install -r requirements.txt", "cdk synth --no-lookups"],
            ),
        )
