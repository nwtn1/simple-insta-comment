# change <POST_ID> and put your login cookie
# and put in data-comment_text what u want to comment
from requests import post
from time import sleep

url = 'https://www.instagram.com/web/comments/<POST_ID>/add/'
cookie = ''

header = {
    'Host': 'www.instagram.com',
    'Cookie': f'{cookie}',
    'Content-Length': '48',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="92"',
    'X-Ig-Www-Claim': 'hmac.AR0dHmhiQ-UtR-lxtd_YFKf9OftHo3ZGGic1hWx5G8K0D7cp',
    'Sec-Ch-Ua-Mobile': '?0',
    'X-Instagram-Ajax': '0dca4f1f6f03',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Asbd-Id': '437806',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'X-Csrftoken': 'Oy2mVAFYhCcQ5TTWRrFdHiYCqagglsG4',
    'X-Ig-App-Id': '936619743392459',
    'Origin': 'https://www.instagram.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/p/CSp5NKvLOPv/',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

data = {
    'comment_text': 'my comment',
    'replied_to_comment_id': ''
}

block = 0
msg = 0
while True:
    r = post(url, data=data, headers=header)
    if(r.status_code == 200):
        msg += 1
        print(f'[+] Comentado - {msg}')
        sleep(90)
    else:
        if(block == 0):
            print('[-] Bloqued, wait 30m')
            sleep(1800)
            block += 1
        elif (block == 1):
            print('[-] Bloqued, wait 1h')
            sleep(3600)
            block += 1
        elif (block == 2):
            print('[-] Bloqued, wait 4h')
            sleep(7200)
            block = 0
