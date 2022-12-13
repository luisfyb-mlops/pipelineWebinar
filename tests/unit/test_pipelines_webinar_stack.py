import aws_cdk as core
import aws_cdk.assertions as assertions

from pipelines_webinar.pipelines_webinar_stack import PipelinesWebinarStack

# example tests. To run these tests, uncomment this file along with the example
# resource in pipelines_webinar/pipelines_webinar_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PipelinesWebinarStack(app, "pipelines-webinar")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
