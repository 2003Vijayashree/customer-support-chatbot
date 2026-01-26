def lambda_handler(event, context):
    email = event["sessionState"]["intent"]["slots"]["email"]["value"]["interpretedValue"]

    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": "PasswordResetIntent",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": f"Your password reset request is received. A reset link will be sent to {email}."
            }
        ]
    }
