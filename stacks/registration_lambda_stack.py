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

class RegistrationLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        conf = config.Config(self.node.try_get_context('environment'))
        environment = conf.get('environment')
        stage = conf.get('stage')

        self.registration_lambda = lambda_.Function(
            self,
            "RegistrationLambda",
            runtime=lambda_.Runtime.PYTHON_3_10,
            code=lambda_.Code.from_asset("./stacks/registration_lambda_code"),
            handler="employee_registration.lambda_handler",
            role=iam.Role.from_role_arn(
                self,
                "ImportToLambdaRegistrationLambdaRoleArn",
                role_arn = f"{core.Fn.import_value('RegisterLambdaRoleArn')}"
            ),
            memory_size=500,
            timeout=core.Duration.minutes(1),
            function_name="employee-registration-cdk"
        )

        # Implement S3 trigger for lambda if possible

        core.CfnOutput(self, "RegistrationLambdaName", value=self.registration_lambda.function_name,
                       export_name="RegistrationLambdaName")
        core.CfnOutput(self, "RegistrationLambdaArn ", value=self.registration_lambda.function_arn,
                       export_name="RegistrationLambdaArn")
