

'''
create sns
aws --endpoint-url=http://localhost:4566 sns create-topic --name order-creation-events --region ap-south-1 --profile test-profile --output table | cat
arn:aws:sns:ap-south-1:000000000000:order-creation-events
create sqs
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name dummy-queue --region ap-south-1 --profile test-profile --output table | cat
http://localhost:4566/000000000000/dummy-queue

create subscription
aws --endpoint-url=http://localhost:4566 sns subscribe --topic-arn arn:aws:sns:ap-south-1:000000000000:order-creation-events --protocol sqs --notification-endpoint arn:aws:sqs:ap-south-1:000000000000:dummy-queue --region ap-south-1 --profile test-profile --output table | cat

get queue arn
aws --endpoint-url=http://localhost:4566 sqs get-queue-attributes --queue-url http://localhost:4566/000000000000/dummy-queue --attribute-names QueueArn --region ap-south-1 --profile test-profile --output text | cut -f2


aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url http://localhost:4566/000000000000/dummy-queue --profile test-profile --region ap-south-1 --output json | cat

aws sns publish --endpoint-url=http://localhost:4566 --topic-arn arn:aws:sns:ap-south-1:000000000000:order-creation-events --message "Hello World" --profile test-profile --region ap-south-1 --output json | cat

'''