import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    order_processing_request = event['order_processing_request']
    item_id = order_processing_request['item']['item_no']
    quantity = order_processing_request['item']['num_of_items']
    shipping_date = order_processing_request['item']['shipping_date']
    shipping_address = order_processing_request['item']['shipping_address']
    order_id = order_processing_request['order_details']['order_id']
    
    # fetch inventory info from DynamoDB
    inventory_data = get_inventory_data_for_item(item_id, quantity)
    
    output = {
        "item": {
            "item_no": item_id,
            "num_of_items": quantity,
            "shipping_date": shipping_date,
            "shipping_address": shipping_address
        },
        # "ItemsAvailable": "true/false",
        "order_details" : {
            "order_id": order_id
        },
        "inventory": {
            "num_of_items": inventory_data['quantity_in_stock'],
            "item_sku": inventory_data['sku']
        }
    }
    
    return output

def get_inventory_data_for_item(item_id, quantity):
    table_name = 'Inventory'
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={'item_id': item_id})
    if 'Item' in response:
        item = response['Item']
        inventory = {
            'sku': item['sku'],
            'quantity_in_stock': item['quantity_in_stock'],
            'warehouse_no': item['warehouse_no'],
            'age_of_stock_in_days': item['age_of_stock_in_days'],
            'quantity_requested': quantity
        }
        return inventory
    else:
        return None
