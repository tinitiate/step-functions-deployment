import boto3
import json 

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # order_processing_request = event['order_processing_request']
    order = event['order_details']['order_id']
    print(f'Marking order {order} as complete...')
    
    # update order status in DynamoDB
    update_order_status(order, 'complete')
    
    return {
        'message': f'Order {order} marked as complete'
    }

def update_order_status(order_id, status):
    table = dynamodb.Table('Orders')
    response = table.update_item(
        Key={
            'order_id': order_id
        },
        UpdateExpression='SET #s = :s',
        ExpressionAttributeNames={
            '#s': 'status'
        },
        ExpressionAttributeValues={
            ':s': status
        }
    )
