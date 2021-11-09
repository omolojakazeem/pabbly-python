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
        return response.text

    def delete_customer(self, customer_id):
        url = "https://payments.pabbly.com/api/v1/customers/" + customer_id
        response = requests.request("DELETE", url, headers=headers, auth=self.auth)
        return response.text

    def create_customer(self, first_name, last_name, email_id, **kwargs):
        url = "https://payments.pabbly.com/api/v1/customer"
        payload = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "email_id": email_id,
            **kwargs,
        })
        response = requests.request("POST", url, auth=self.auth, headers=headers, data=payload)
        return response.text

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

        response = requests.request("POST", url, headers=headers, auth=self.auth, data=payload)
        return response.text

    def update_customer_detail(self, customer_id, **kwargs):
        url = "https://payments.pabbly.com/api/v1/customer/" + customer_id

        payload = json.dumps({
            **kwargs
        })
        response = requests.request("PUT", url, headers=headers, auth=self.auth, data=payload)
        return response.text

    def create_product(self, product_name, redirect_url, description="Product Description"):
        url = "https://payments.pabbly.com/api/v1/product/create"

        payload = json.dumps({
            "product_name": product_name,
            "description": description,
            "redirect_url": redirect_url,
        })

        response = requests.request("POST", url, headers=headers, auth=self, data=payload)
        return response.text

    def list_all_products(self):
        url = "https://payments.pabbly.com/api/v1/products"
        response = requests.request("GET", url, headers=headers, auth=self.auth)
        return response.text

    def update_product(self, product_id, **kwargs):
        url = "https://payments.pabbly.com/api/v1/product/update/" + product_id

        payload = json.dumps({
            **kwargs
        })

        response = requests.request("PUT", url, headers=headers, data=payload, auth=self.auth)
        return response.text

    def delete_product(self, product_id):
        url = "https://payments.pabbly.com/api/v1/products/" + product_id

        response = requests.request("DELETE", url, headers=headers, auth=self.auth)
        return response.text

    # Coupons
    def create_coupon(self, coupon_name, coupon_code, discount, discount_type, redemption_type, valid_upto, **kwargs):
        url = "https://payments.pabbly.com/api/v1/coupon/{product_id}"

        payload = json.dumps({
            "coupon_name": coupon_name,
            "coupon_code": coupon_code,
            "discount": discount,
            "discount_type": discount_type,
            "redemption_type": redemption_type,
            "valid_upto": valid_upto,
            **kwargs
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text

    def get_coupon_of_product(self, product_id):
        url = "https://payments.pabbly.com/api/v1/coupon/" + product_id
        response = requests.request("GET", url, headers=headers, auth=self.auth)
        return response.text

    def delete_coupon(self, coupon_id):
        url = "https://payments.pabbly.com/api/v1/coupons/" + coupon_id
        response = requests.request("DELETE", url, headers=headers, auth=self.auth)
        return response.text

    # Checkout Pages
    def create_checkout_page(self, product_id):
        url = "https://payments.pabbly.com/api/v1/checkoutpage/" + product_id
        response = requests.request("GET", url, headers=headers, auth=self.auth)
        return response.text

    def verify_hosted_page(self, hostedpage):
        url = "https://payments.pabbly.com/api/v1/verifyhosted"
        payload = json.dumps({
            "hostedpage": hostedpage,
        })
        response = requests.request("POST", url, headers=headers, auth=self.auth, data=payload)
        return response.text

    def get_hosted_page(self, hostedpage):
        url = "https://payments.pabbly.com/api/v1/hostedpage"

        payload = json.dumps({
            "hostedpage": hostedpage,
        })

        response = requests.request("POST", url, headers=headers, auth=self.auth, data=payload)
        return response.text

    # Portal Session
    def create_portal_session(self, customer_id, redirect_url=None):
        url = "https://payments.pabbly.com/api/v1/portal_sessions/"

        payload = json.dumps({
            "customer_id": customer_id,
            "redirect_url": redirect_url
        })
        response = requests.request("POST", url, headers=headers, auth=self.auth, data=payload)
        return response.text



