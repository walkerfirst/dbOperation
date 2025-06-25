import requests
from bs4 import BeautifulSoup

def fetch_page_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
        'Referer': 'https://www.chemicalbook.com/',  # 模拟 Referer
        'Origin': 'https://www.chemicalbook.com',  # 模拟 Origin
    }

    try:
        # 发送 GET 请求
        response = requests.get(url, headers=headers)

        # 检查是否成功
        if response.status_code == 200:
            return response.text
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"请求过程中出错: {e}")
        return None

def extract_data(html_content):
    # 解析页面内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 假设页面中有一个包含我们所需数据的表格
    table = soup.find('table')

    if table:
        rows = table.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            data.append(cols)

        return data
    else:
        print("没有找到数据表格")
        return None

def process_data(keyword):
    url = f"https://www.chemicalbook.com/Search.aspx?keyword={keyword}"
    print(f"访问网址：{url}")

    # 获取页面内容
    html_content = fetch_page_data(url)

    if html_content:
        # 提取表格数据
        data = extract_data(html_content)
        if data:
            # 打印提取的数据，查看格式
            print("提取到的数据:")
            #for row in data:
                #print(row)

            # 提取英文名称、中文名称和CAS
            english_name = ""
            chinese_name = ""
            cas = ""

            for row in data:
                if "CBNumber：" in row:
                    cb_number = row[row.index("CBNumber：") + 1].strip()
                if '英文名称：' in row:
                    english_name = row[row.index('英文名称：') + 1].strip()
                if '中文名称：' in row:
                    chinese_name = row[row.index('中文名称：') + 1].strip()
                if 'CAS：' in row:
                    cas = row[row.index('CAS：') + 1].strip()

            # 打印提取的字段
            print(f"CBNumber: {cb_number}")
            print(f"英文名称: {english_name}")
            print(f"中文名称: {chinese_name}")
            print(f"CAS: {cas}")

        else:
            print("没有提取到有效数据")
    else:
        print("无法加载页面")

def test():
    print('开始测试...')
    keyword = '358-23-6'
    process_data(keyword)

if __name__ == '__main__':
    test()
