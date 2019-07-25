from __future__ import print_function
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Phucccc')

with open("movie-data.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )

