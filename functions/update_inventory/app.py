import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # order_processing_request = event['order_processing_request']
    item_no = event['item']['item_no']
    quantity = event['item']['num_of_items']
    inventory = event['inventory']['num_of_items']


    quantity_in_stock = inventory-quantity
    print(f'Updating inventory for item {item_no}...')
    
    # update inventory in DynamoDB
    update_inventory(item_no, quantity_in_stock)
    
    return {
        'message': f'Inventory updated for item {item_no}'
    }

def update_inventory(item_no, quantity):
    table = dynamodb.Table('Inventory')
    response = table.update_item(
        Key={
            'item_id': item_no
        },
        UpdateExpression='SET #q = :q',
        ExpressionAttributeNames={
            '#q': 'quantity_in_stock'
        },
        ExpressionAttributeValues={
            ':q': quantity
        }
    )
