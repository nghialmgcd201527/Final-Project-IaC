from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
)
from constructs import Construct
import aws_cdk as core
from helper import config

class DynamoDBStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        conf = config.Config(self.node.try_get_context('environment'))

        self.dynamodb = dynamodb.Table(
            self,
            "DynamoDB",
            table_name="employee-cdk",
            partition_key=dynamodb.Attribute(
                name="rekognitionid",
                type=dynamodb.AttributeType.STRING
            ),
        )
        
        core.CfnOutput(self, "DynamoDBName", value=self.dynamodb.table_name,
                       export_name="DynamoDBName")
        core.CfnOutput(self, "DynamoDBArn", value=self.dynamodb.table_arn,
                       export_name="DynamoDBArn")
