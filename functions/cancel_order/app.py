import boto3
# This is a comment.

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # order_processing_request = event['order_processing_request']
    order_id = event['order_details']['order_id']
    print(f'Cancelling order {order_id}...')
    
    # cancel order in DynamoDB
    cancel_order(order_id)
    
    return {
        'message': f'Order {order_id} cancelled'
    }

def cancel_order(order_id):
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
            ':s': 'cancelled'
        }
    )
