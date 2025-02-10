import requests

MAILGUN_API_KEY = "3d68708dbdaefcce16f123aa92c756ee-1654a412-3ccae23d"
MAILGUN_API_URL = "https://api.mailgun.net/v3/sandboxf9d2bbcc2e1f49ee8c3f81c796549970.mailgun.org/messages"
FROM_EMAIL_ADDRESS = "mailgun@sandboxf9d2bbcc2e1f49ee8c3f81c796549970.mailgun.org"


def send_email(to_address: str, subject: str, message: str):
    resp = requests.post(
        MAILGUN_API_URL,
        auth=("api", MAILGUN_API_KEY),
        data={
            "from":FROM_EMAIL_ADDRESS,
            "to":to_address,
            "subject":subject,
            "text":message
        }
    )


    if resp.status_code == 200:
        print("Success! Email sent.")
    else:
        print(resp.status_code)
        print(resp.text)


send_email("j_chara@live.concordia.ca", "This is a test email", "This is a test message.")