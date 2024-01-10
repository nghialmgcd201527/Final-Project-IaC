from aws_cdk import (
    Stack,
    aws_iam as iam,
)
from constructs import Construct
import aws_cdk as core
from helper import config

class ApiGatewayRoleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        conf = config.Config(self.node.try_get_context('environment'))

        self.api_gateway_role = iam.Role(
            self,
            "ApiGatewayRole",
            assumed_by=iam.ServicePrincipal('apigateway.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_managed_policy_arn(
                    self,
                    "AmazonAPIGatewayPushToCloudWatchLogs",
                    managed_policy_arn="arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
                )
            ],
            role_name="FacialRecognitionAPIGatewayRoleCDK"
        )

        core.CfnOutput(self, "ApiGatewayRoleName", value=self.api_gateway_role.role_name,
                       export_name="ApiGatewayRoleName")
        core.CfnOutput(self, "ApiGatewayRoleArn", value=self.api_gateway_role.role_arn,
                       export_name="ApiGatewayRoleArn")
