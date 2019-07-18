```bash
docker build -t dmilan/docker-s3-access:latest .
docker run -p 8080:8080 dmilan/docker-s3-access

curl http://localhost:8080/s3 -d "aws_access_key_id=xxxxxxx" -d "aws_secret_access_key=xxxxx" -d "bucket=yourbucketname" -d "bucketObj=yoursamplejson.json"
```