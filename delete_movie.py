import boto3

table = boto3.resource('dynamodb').Table('Phucccc')

scan = table.scan()
with table.batch_writer() as batch:
    for each in scan['Items']:
        batch.delete_item(
            Key={
                'year': each['year'],
                'title': each['title']
            }
        )