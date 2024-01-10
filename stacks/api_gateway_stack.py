from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_apigateway as apigw
)
from constructs import Construct
import aws_cdk as core
from helper import config

class ApiGatewayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        conf = config.Config(self.node.try_get_context('environment'))

        self.api_gateway = apigw.RestApi(
            self,
            "ApiGateway",
            rest_api_name="facial-recognition-api-cdk",
        )

        # core.CfnOutput(self, "ApiGatewayRoleName", value=self.api_gateway_role.role_name,
        #                export_name="ApiGatewayRoleName")
        # core.CfnOutput(self, "ApiGatewayRoleArn", value=self.api_gateway_role.role_arn,
        #                export_name="ApiGatewayRoleArn")