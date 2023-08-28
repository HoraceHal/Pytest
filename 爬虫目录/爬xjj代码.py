import time
import requests
from lxml import etree
import os
import concurrent.futures


def download_image(url, img_path):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Referer': 'https://www.xiezhen.xyz/'
    }
    response = requests.get(url, headers=headers)
    img_name = url.split('/')[-1]
    with open(os.path.join(img_path, img_name), 'wb') as f:
        f.write(response.content)
        print(f'图片：{img_path}' + '/' + f'{img_name}下载完成！')


def process_page(page):
    url = f'https://www.xiezhen.xyz/page/{page}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Referer': 'https://www.xiezhen.xyz/'
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content)
    mail_url = html.xpath('//div[@class="excerpts"]/article/a/@href')
    for url in mail_url:
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.content)
        sub_url = html.xpath('//article/p/img')
        img_title = html.xpath('//title/text()')[0].split('-')[0]
        img_path = f'D:/BCTB/{img_title}'
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for s_url in sub_url:
                img_url = s_url.attrib['src']
                futures.append(executor.submit(download_image, img_url, img_path))
            for future in concurrent.futures.as_completed(futures):
                pass
        time.sleep(0.5)


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for page in range(1, 573):
            futures.append(executor.submit(process_page, page))
        for future in concurrent.futures.as_completed(futures):
            pass
