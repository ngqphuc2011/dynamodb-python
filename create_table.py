from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal


def create_table():
    dynamodb = boto3.resource("dynamodb")
    dynamodb.create_table(
        TableName="Phucccc",
        KeySchema=[
            {
                "AttributeName": "year",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "title",
                "KeyType": "RANGE"
            },
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "year",
                "AttributeType": "N"
            },
            {
                "AttributeName": "title",
                "AttributeType": "S"
            },

        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )

create_table()