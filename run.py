import requests
import time
import json
import random
import os
from datetime import datetime

# --------- CẤU HÌNH CỐ ĐỊNH ------------
PROVIDER = {
    "name": "SubGiaSale.Vn",
    "token": "DvZGKXaiuCHQCzPwC7I0ClohRVofIMvk7kSdoYEnySKWy0afIgUCWPf0yHgU",
    "api_url": "https://subgiasale.cfd/api/v2"
}

REQUEST_DATA = {
    "link": "https://vt.tiktok.com/ZSrj8sR28/",
    "service": 27712,
    "quantity": 100,
    "minutes": 30,
    "comments": "Vip",
    "reaction": "like"
}

NUM_ORDERS = 1000          # Số đơn cần tạo
DELAY_SECONDS = 0       # Thời gian chờ giữa các đơn (giây)

# --------------------------------------

def create_order(provider, request_data):
    post_data = {
        'key': provider['token'],
        'action': 'add',
        'service': request_data['service'],
        'link': request_data['link'],
        'minutes': request_data.get('minutes', 0),
        'quantity': request_data['quantity'],
        'comments': request_data.get('comments', ''),
        'reaction': request_data.get('reaction', 'like').lower()
    }

    try:
        response = requests.post(provider['api_url'], data=post_data, timeout=20)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def generate_order_code():
    return 'INV_' + datetime.now().strftime('%d%m%y') + str(random.randint(10000, 99999))

def main():
    for i in range(NUM_ORDERS):
        print(f"\n🚀 Đang tạo đơn thứ {i+1}...")

        result = create_order(PROVIDER, REQUEST_DATA)

        if 'order' in result:
            order_code = generate_order_code()
            print(f"✅ Thành công! Mã đơn: {order_code} - ID đơn: {result['order']}")
        else:
            print(f"❌ Lỗi: {result.get('error') or result.get('message') or 'Không rõ nguyên nhân'}")

        if i < NUM_ORDERS - 1:
            time.sleep(DELAY_SECONDS)

if __name__ == "__main__":
    main()
