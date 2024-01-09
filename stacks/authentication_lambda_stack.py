from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_iam as iam,
    triggers,
    aws_s3 as s3,
    aws_s3_notifications as s3_notifications,
)
from constructs import Construct
import aws_cdk as core
from helper import config

class AuthenticationLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        conf = config.Config(self.node.try_get_context('environment'))
        environment = conf.get('environment')
        stage = conf.get('stage')

        self.authentication_lambda = lambda_.Function(
            self,
            "AuthenticationLambda",
            runtime=lambda_.Runtime.PYTHON_3_10,
            code=lambda_.Code.from_asset("./stacks/authentication_lambda_code"),
            handler="employee_authentication.lambda_handler",
            role=iam.Role.from_role_arn(
                self,
                "ImportToLambdaRegistrationLambdaRoleArn",
                role_arn = f"{core.Fn.import_value('RegisterLambdaRoleArn')}"
            ),
            memory_size=500,
            timeout=core.Duration.minutes(1),
            function_name="employee-authentication-cdk"
        )

        # Implement S3 trigger for lambda if possible

        core.CfnOutput(self, "AuthenticationLambdaName", value=self.authentication_lambda.function_name,
                       export_name="AuthenticationLambdaName")
        core.CfnOutput(self, "AuthenticationLambdaArn ", value=self.authentication_lambda.function_arn,
                       export_name="AuthenticationLambdaArn")
