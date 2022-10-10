from boto3 import resource
from os import getenv

dynamodb = resource("dynamodb",
                    aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
                    aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
                    region_name=getenv("REGION_NAME"))


tables = [
    {
        "TableName": "db_user",
        "KeySchema": [
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'userid',
                'KeyType': 'RANGE'
            },
        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'userid',
                'AttributeType': 'N'
            }
        ],
    },
]


def create_tables():
    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)
