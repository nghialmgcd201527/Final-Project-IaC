from aws_cdk import (
    Stack,
    aws_s3 as s3,
)
from constructs import Construct
import aws_cdk as core
from helper import config

class ImageBucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        conf = config.Config(self.node.try_get_context('environment'))
        environment = conf.get('environment')
        stage = conf.get('stage')

        self.image_bucket = s3.Bucket(
            self,
            "RegisterImageBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            # bucket_key_enabled=True,
            bucket_name="minhnghia-employee-image-storage-cdk",
            versioned=True,
            # encryption_key=s3.BucketEncryption.UNENCRYPTED,
        )
        
        core.CfnOutput(self, "RegisterImageBucketName", value=self.image_bucket.bucket_name,
                       export_name="RegisterImageBucketName")
        core.CfnOutput(self, "RegisterImageBucketArn", value=self.image_bucket.bucket_arn,
                       export_name="RegisterImageBucketArn")
