# from aws_cdk import (
#     Stack,
#     aws_iam as iam,
# )
# from constructs import Construct
# import aws_cdk as core
# from helper import config

# class S3PutPolicyStack(Stack):

#     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)

#         conf = config.Config(self.node.try_get_context('environment'))

#         self.s3_put_policy = iam.Policy(
#             self,
#             "S3PutPolicy",
#             statements=[
#                 iam.PolicyStatement(
#                     actions=["s3:PutObject"],
#                     resources=[f"{core.Fn.import_value('RegisterLambdaRoleArn')}/*"],
#                     effect=iam.Effect.ALLOW,
#                     sid="AllowPutObject"
#                 )
#             ],
#             policy_name="FacialRecognitionS3PutPolicyCDK"
#         )

#         core.CfnOutput(self, "S3PutPolicyName", value=self.s3_put_policy.policy_name,
#                        export_name="S3PutPolicyName")
