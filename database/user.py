from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("db_user")


def create_user(user: dict):
    try:
        table.put_item(Item=user)
        return user
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_user(id: int):
    try:
        response = table.query(
            KeyConditionExpression=Key("id").eq(id)
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_users():
    try:
        response = table.scan(
            Limit=100,
            AttributesToGet=["id", "username", "userid", "age"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def delete_user(user: dict):
    try:
        response = table.delete_item(
            Key={
                "id": user["id"],
                "userid": user["userid"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def update_user(user: dict):
    try:
        response = table.update_item(
            Key={
                "id": user["id"],
                "userid": user["userid"]
            },
            UpdateExpression="SET username = :username, age = :age",
            ExpressionAttributeValues={
                ":username": user["username"],
                ":age": user["age"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)
