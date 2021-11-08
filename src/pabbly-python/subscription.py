import requests
from requests.auth import HTTPBasicAuth
import json

headers = {
    'Content_type': 'application/json'
}


class Pabbly:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.auth = HTTPBasicAuth(self.api_key, self.api_secret)

    def list_customers(self):
        url = 'https://payments.pabbly.com/api/v1/customers'
        response = requests.get(url=url, auth=self.auth, headers=headers)
        return response.text

    def get_customer_by_id(self, customer_id):
        url = "https://payments.pabbly.com/api/v1/customer/" + customer_id
        response = requests.request("GET", url, headers=headers, auth=self.auth)
        return response.text

    def get_customer_by_email(self, customer_email):
        url = "https://payments.pabbly.com/api/v1/customer/?email=" + customer_email
        response = requests.request("GET", url, headers=headers, auth=self.auth)
        return response.text

    def get_customer_purchase_info(self, customer_id):
        url = "https://payments.pabbly.com/api/v1/customer/purchase-info/" + customer_id
        response = requests.request("GET", url, headers=headers, auth=self.auth)
        return response

    def delete_customer(self, customer_id):
        url = "https://payments.pabbly.com/api/v1/customers/" + customer_id
        response = requests.request("DELETE", url, headers=headers, auth=self.auth)
        return response

    def create_customer(self, first_name, last_name, email_id, **kwargs):
        url = "https://payments.pabbly.com/api/v1/customer"
        payload = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "email_id": email_id,
            **kwargs,
        })
        response = requests.request("POST", url, auth=self.auth, headers=headers, data=payload)
        return response

    def create_customer_with_subscription(self, first_name, last_name, email_id, plan_id, card_number, exp_month,
                                          exp_year, cvv, gateway_type, gateway_id, **kwargs):
        url = "https://payments.pabbly.com/api/v1/subscription"
        payload = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "email": email_id,
            "card_number": card_number,
            "month": exp_month,
            "year": exp_year,
            "cvv": cvv,
            "gateway_type": gateway_type,
            "gateway_id": gateway_id,
            "plan_id": plan_id,
            **kwargs
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, auth=self.auth, data=payload)
        return response

    def update_customer_detail(self, customer_id, **kwargs):
        url = "https://payments.pabbly.com/api/v1/customer/" + customer_id

        payload = json.dumps({
            **kwargs
        })
        response = requests.request("PUT", url, headers=headers, auth=self.auth, data=payload)
        return response

