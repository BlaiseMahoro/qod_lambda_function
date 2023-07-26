# qod_lambda_function
Lambda function that gets the quote of the day and create a file that can be passed to a user via SNS/SES or HTTP.

# Setup
- Create constants.py file and set your API_TOKEN and API_BASE_URL constants:
  QOD_API_TOKEN = "<YOUR_API_KEY>"
  QOD_BASE_URL = "https://quotes.rest/"
- Run pip install requests

# Running the program
- Go into qod_lambda_function and run `py main.py`
- A new html file with name `file_*.html` should be created.

# To run this code as part of AWS Lambda function. We will need the following:
- Create a lambda function whose trigger is an EventBridge service with a schedule. (daily/hourly...)
- This lambda function's handler should redirect user to the page with the new html page.
Next steps:
- Add an event that adds this file to S3 and return a signed-URL for it. The user should be able to view this page/file for a limited time.
- Add caching to avoid fetching QOD every time the lambda funcion is created. To be more cost-effective, we will use Dynamo DB and set ttl to delete the QOD after the day ends.
- Add SNS to asynchronously send the QOD to subsribers. Hard-code them to a few e-mails you own.
- More Advanced: Create another lambda function that lets users subsribe to the QOD service. This one will need an API Gateway to expose the lambda function's api `/subscribe`.
