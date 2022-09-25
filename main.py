from twilio.rest import Client
import os


def sending_sms(text='Wake up Neo...', receiver=os.getenv('RECEIVER_PHONE')):
    try:
        account_sid = os.getenv('SID')
        auth_token = os.getenv('AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=text,
            from_=os.getenv('SENDER_PHONE_NUMBER'),
            to=receiver
        )

        return 'The message was successfully sent!'
    except Exception as ex:
        return 'Something was wrong... :(', ex


def main():
    receiver = input('Please enter receiver phone: ')
    text = input('Please enter your message: ')
    print(sending_sms(text=text, receiver=receiver))


if __name__ == '__main__':
    main()
