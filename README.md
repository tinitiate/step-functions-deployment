# Step-Functions Deployment

- The GitHub Actions workflow will execute when a push event occurs on the main branch..
- The workflow is executed on an Ubuntu-based virtual machine.
- The workflow starts with checking out the code from the repository.
- The workflow then configures AWS credentials using the aws-actions/configure-aws-credentials action.
- AWS CLI is installed using the pip package manager.
- The sam deploy command is used to deploy the OrderProcessing stack using AWS SAM.
- The sam deploy command is passed the following parameters:
  - template-file: The path to the SAM template file
  - stack-name: The name of the CloudFormation stack to create/update
  - capabilities: The capabilities required by CloudFormation to create/update the stack
  - parameter-overrides: The values for stack parameters defined in the template file
  - s3-bucket: The name of the S3 bucket to upload deployment artifacts
- The stack parameters UserPoolArn, DynamoDBPolicyArn, and S3_BUCKET_NAME are retrieved from GitHub secrets.
- The AWS credentials are passed to the sam deploy command using environment variables.
