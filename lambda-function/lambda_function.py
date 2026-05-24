def handler(event, context):
    name = event.get('name','Guest')

    return {
        'statusCode':200,
        'message':f'Hello {name}, Lambda Functions is working.'
    }