#!/usr/bin/env python3
import os

import aws_cdk as cdk

# from stacks.vpc_stack import VPCStack
# from stacks.iam.iam_group_stack import IamGroupStack
# from stacks.iam.iam_policy.iam_policy_devops_stack import IamPolicyDevopsStack
# from stacks.iam.iam_policy.iam_policy_maintainers_stack import IamPolicyMaintainersStack
# from stacks.iam.iam_policy.iam_policy_developers_stack import IamPolicyDevelopersStack
# from stacks.iam.iam_role_codebuild.iam_role_codebuild_fe_stack import IamRoleCodebuildFeStack
# from stacks.iam.iam_role_codebuild.iam_role_codebuild_be_stack import IamRoleCodebuildBeStack
# from stacks.secret_manager_stack import SecretManagerStack
# from stacks.codebuild_be.file_service_stack import FileServiceCodebuildStack
# from stacks.iam.iam_role_codepipeline_stack import IamRoleCodePipelineStack

from stacks.image_bucket_stack import ImageBucketStack
from stacks.registration_lambda_role_stack import RegistrationLambdaRoleStack
from stacks.registration_lambda_stack import RegistrationLambdaStack
from stacks.dynamodb_stack import DynamoDBStack

import cdk_nag
from helper import config
# from aws_cdk import (
#     Aspects,
# )

app = cdk.App()
conf_app = config.Config(app.node.try_get_context('environment'))

image_bucket_stack = ImageBucketStack(app, 
                    "image-bucket-stack",
                    env=cdk.Environment(account=conf_app.get('account_id'),
                    region=conf_app.get('region')))

registration_lambda_role_stack = RegistrationLambdaRoleStack(app, 
                    "registration-lambda-role-stack",
                    env=cdk.Environment(account=conf_app.get('account_id'),
                    region=conf_app.get('region')))

registration_lambda_stack = RegistrationLambdaStack(app, 
                    "registration-lambda-stack",
                    env=cdk.Environment(account=conf_app.get('account_id'),
                    region=conf_app.get('region')))

dynamodb_stack = DynamoDBStack(app, 
                    "dynamodb-stack",
                    env=cdk.Environment(account=conf_app.get('account_id'),
                    region=conf_app.get('region')))

# Aspects.of(app).add(cdk_nag.AwsSolutionsChecks())
app.synth()
