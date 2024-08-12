import whois
from datetime import datetime, timedelta
import requests
import sys

def get_domain_expiry(domain_name, slack_webhook_url):
    try:
        domain_info = whois.whois(domain_name)
        expiry_date = domain_info.expiration_date

        if isinstance(expiry_date, list):
            expiry_date = expiry_date[0]

        today = datetime.now()
        if expiry_date and isinstance(expiry_date, datetime):
            time_difference = expiry_date - today
            if time_difference <= timedelta(days=30):
                notify_slack(domain_name, expiry_date, time_difference.days, slack_webhook_url)
            else:
                print(f"The domain {domain_name} is safe. Expiry date: {expiry_date}")
        else:
            print(f"Unable to determine the expiry date for {domain_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def notify_slack(domain_name, expiry_date, days_left, slack_webhook_url):
    message = (f"⚠️ *Domain Expiry Alert*: The domain *{domain_name}* expires on *{expiry_date}* "
               f"(in {days_left} days). Please take necessary action.")
    slack_data = {'text': message}

    response = requests.post(
        slack_webhook_url, json=slack_data,
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, "
                         f"the response is:\n{response.text}")

if __name__ == "__main__":
    domains = sys.argv[1]
    slack_webhook_url = sys.argv[2]
    domain_list = domains.split(',')
    
    for domain_name in domain_list:
        domain_name = domain_name.strip()
        if domain_name:
            get_domain_expiry(domain_name, slack_webhook_url)
