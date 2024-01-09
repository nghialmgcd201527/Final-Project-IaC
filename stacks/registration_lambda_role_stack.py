from aws_cdk import (
    Stack,
    aws_iam as iam,
)
from constructs import Construct
import aws_cdk as core
from helper import config

class RegistrationLambdaRoleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        conf = config.Config(self.node.try_get_context('environment'))
        environment = conf.get('environment')
        stage = conf.get('stage')

        self.register_lambda_role = iam.Role(
            self,
            "RegisterLambdaRole",
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRekognitionFullAccess"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonDynamoDBFullAccess"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "CloudWatchLogsFullAccess"
                )
            ],
            role_name="FacialRecognitionLambdaRoleCDK"
        )

        core.CfnOutput(self, "RegisterLambdaRoleName", value=self.register_lambda_role.role_name,
                       export_name="RegisterLambdaRoleName")
        core.CfnOutput(self, "RegisterLambdaRoleArn", value=self.register_lambda_role.role_arn,
                       export_name="RegisterLambdaRoleArn")
