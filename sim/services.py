# core/services.py
import os
import gspread
from typing import List
from django.conf import settings

def initialize_gspread() -> gspread.client.Client:
    return gspread.service_account_from_dict(get_credentials())

def get_credentials() -> dict:
    return {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN")
    }

# sim/services.py
def get_all_rows(sheet_name, expected_headers=None, return_row_numbers=False):
    client = initialize_gspread()
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()
    if expected_headers:
        data = [{key: row.get(key, '') for key in expected_headers} for row in data]
    if return_row_numbers:
        row_numbers = list(range(2, len(data) + 2))  # Assuming the first row is the header
        return list(zip(data, row_numbers))
    return data

