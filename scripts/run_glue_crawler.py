import boto3
import os
from dotenv import load_dotenv

load_dotenv()

crawler_name = os.getenv("GLUE_CRAWLER_NAME")
region = os.getenv("AWS_REGION")

client = boto3.client("glue", region_name=region)

response = client.start_crawler(Name=crawler_name)
print(f"Started Glue Crawler: {crawler_name}")
