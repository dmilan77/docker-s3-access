from flask import Flask
from flask_restplus import Resource, Api,reqparse
import socket, os
import json
import boto3, io
from io import BytesIO



app = Flask(__name__)
api = Api(app)

s3_parser = api.parser()
s3_parser.add_argument('aws_access_key_id', required=True)
s3_parser.add_argument('aws_secret_access_key', required=True)
s3_parser.add_argument('bucket', required=True)
s3_parser.add_argument('bucketObj', required=True)

@api.route('/ping')
class PingWorld(Resource):
    def get(self):
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)

        outPut={
            'hostname': host_name,
            'host_ip': host_ip
        }
        # return json.dumps(outPut)
        return outPut

@api.route('/s3')
@api.expect(s3_parser)
class S3World(Resource):

    def post(self):
        args = s3_parser.parse_args()
        aws_access_key_id=args['aws_access_key_id']
        aws_secret_access_key=args['aws_secret_access_key']
        bucket=args['bucket']
        bucketObj=args['bucketObj']
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name='us-east-1'
        )
        # s3_client = boto3.client('s3',
        #                          aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
        #                          aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY,
        #                          region_name=REGION_NAME
        #                          )
        client = boto3.client('s3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

        resource = boto3.resource('s3')
        my_bucket = resource.Bucket(bucket)

        obj = client.get_object(Bucket=bucket, Key=bucketObj)
        print (obj)

        return json.loads(obj['Body'].read())

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080",debug=True)