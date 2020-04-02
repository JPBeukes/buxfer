import requests
import sys
import os

import pandas as pd
import matplotlib.pyplot as plt

username = os.environ['BUXFER_USERNAME']
password = os.environ['BUXFER_PASSWORD']
base = "https://www.buxfer.com/api"


def process_response(response):
    content = response.json()['response']
    if content['status'] != "OK":
        print("An error occured: %s" % content['status'].replace('ERROR: ', ''))
        sys.exit(1)
    return content


def get_login_token():
    url = base + "/login?userid=" + username + "&password=" + password
    response = requests.get(url)
    content = process_response(response)
    return content['token']


def get_transactions(token):
    url = base + '/transactions?token=' + token
    response = requests.get(url)
    content = process_response(response)
    return content['transactions']


token = get_login_token()
transactions = get_transactions(token)
transactions_df = pd.DataFrame(transactions)
sum_df = transactions_df.groupby('tags').sum()
sum_df.drop(index=['Income', ''], inplace=True)
sum_df.plot(y='expenseAmount', kind='bar')
plt.show()