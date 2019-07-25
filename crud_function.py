import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Phucccc')

#DELETE
# event = {
#     'action': 'delete',
#     'key': {
#         'year': 2013,
#         'title': 'After Earth'
#     }
# }

#CREATE
# event = {
#     'action': 'create',
#     'item': {
#         'year': 2013,
#         'title': 'Gravity',
#         'info': {
#             'directors': ['Alfonso Cuaron'],
#             'release_date': '2013-08-28T00:00:00Z',
#             'rating': 8.2,
#             'genres': [
#                 'Drama',
#                 'Sci-Fi',
#                 'Thriller'
#             ],
#             'image_url': 'http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_SX400_.jpg',
#             'plot': 'A medical engineer and an astronaut work together to survive after an accident leaves them adrift in space.',
#             'rank': 12,
#             'running_time_secs': 5400,
#             'actors': [
#                 'Sandra Bullock',
#                 'George Clooney',
#                 'Ed Harris'
#             ]
#         }
#     }
# }

# UPDATE
# event = {
#     'action': 'update',
#     'key': {
#         'year': 2013,
#         'title': 'Gravity' 
#     },
#     'updateExpression': 'set info.rating = :r',
#     'expressionAttributeValues': {
#         ':r': 1
#     },
#     'returnValues': 'UPDATED_NEW'
# }

# READ
# event = {
#     'action': 'read',
#     'key': {
#         'year': 2013,
#         'title': 'Gravity'
#     }
# }

# READ_ALL
# event = {
#     'action': 'readall'
# }




def delete_movie(event, table):
    try:
        result = table.delete_item(
            Key=event['key']
        )
        print('Deleted!')
    except Exception as ex:
        return ex
    return result


def create_movie(event, table):
    try:
        result = table.put_item(
            Item=event['item']
        )
        print('Created!')
    except Exception as ex:
        return ex
    return result


def read_movie(event, table):
    try:
        result = table.get_item(
            Key=event['key']
        )
        print(result)
    except Exception as ex:
        return ex
    return result


def update_movie(event, table):
    try:
        result = table.update_item(
            Key=event['key'],
            UpdateExpression=event['updateExpression'],
            ExpressionAttributeValues=event['expressionAttributeValues'],
            ReturnValues=event['returnValues']
        )
        print('Updated!')
    except Exception as ex:
        return ex
    return result

def read_movie_all(event, table):
    try:
        result = table.scan()
    except Exception as ex:
        return ex
    return result


def lambda_handler(event, context):
    action = event.get('action')
    if action == 'delete':
        return delete_movie(event, table)
    elif action == 'create':
        return create_movie(event, table)
    elif action == 'update':
        return update_movie(event, table)
    elif action == 'read':
        return read_movie(event, table)
    elif action == 'readall':
        # print(read_movie_all(event, table))
        return read_movie_all(event, table)
    

