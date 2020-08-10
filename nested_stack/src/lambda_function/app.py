import os


def handler(event, context):
    print(os.environ['NESTED_LAMBDA_FUNCTION'])