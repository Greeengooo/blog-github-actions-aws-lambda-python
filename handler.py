import json
import pyjokes


def get_joke(event, context):
   s = 'Hello World!!!'
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

