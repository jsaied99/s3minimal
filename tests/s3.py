from s3minimal import S3Sync
import os


s3 = S3Sync(
    endpoint_url=os.environ["S3_ENDPOINT_URL"],
    region_name=os.environ["S3_REGION_NAME"],
    aws_access_key_id=os.environ["S3_ACCESS_KEY"],
    aws_secret_access_key=os.environ["S3_SECRET_KEY"],
    bucket=os.environ["S3_BUCKET"],
)
