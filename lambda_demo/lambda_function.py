import json


#def lambda_handler(event, context):
def lambda_handler():
    print('This is lambda handler function')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def my_function():
    print("My Function ")

def main():
    lambda_handler()


if __name__ == "__main__":
    main()