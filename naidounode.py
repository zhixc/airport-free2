import requests
import datetime
import base64

# 设置请求头信息
headers = {
    'Cookie': '_ga=GA1.1.1307483079.1729739808; _ga_Y18GQ0V9RB=GS1.1.1729739808.1.1.1729739949.0.0.0; de12a86fcd0a8cf9c03fee2a7c500b57=1; e5c772364b521f15a0d3c889d043f05d=1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
}

# 获取当前日期
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

# 构建URL列表
urls = [
    f"https://www.naidounode.com/node/{year}{month}{day}-v2ray.txt"
]

# 发起请求并打印结果
for url in urls:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        data64 = base64.b64decode(response.text)
        data8 = data64.decode('utf-8')
        print(data8)
    except requests.exceptions.RequestException as e:
        print(f"未获取到到节点，错误代码：{e}")