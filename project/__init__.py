import json

def lambda_handler(event, context):
    print("this is lambda")
    ret = {}

    return {
         "statusCode": 200,
         "body": json.dumps(ret)
     }
