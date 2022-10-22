import datetime,urllib
import random
import requests

# fetch("https://hz.ft12.com/multi.php?url=www.ft12.comhttps://www.bilibili.com/video/BV1GJ411x7h7", {
#   "headers": {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
#     "cache-control": "no-cache",
#     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "pragma": "no-cache",
#     "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "cookie": "Hm_lvt_be83c4c98bd599b8b8d237723a429d18=1665836329; Hm_lpvt_be83c4c98bd599b8b8d237723a429d18=1665836393",
#     "Referer": "https://www.ft12.com/",
#     "Referrer-Policy": "strict-origin-when-cross-origin"
#   },
#   "body": "url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1GJ411x7h7&host=985.so&random=339234789952197&token=",
#   "method": "POST"
# });
session = requests.Session()


class Ft12(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def short(link):
        #e.g. 173562087130938
        rnum = "".join(str(random.randint(1, 9) if i == 0 else random.randint(0, 9)) for i in range(15))
        req = session.post(
            f"https://hz.ft12.com/multi.php?url=www.ft12.com{urllib.parse.quote(link)}",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "pragma": "no-cache",
                "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "cookie": "Hm_lvt_be83c4c98bd599b8b8d237723a429d18=1665836329; Hm_lpvt_be83c4c98bd599b8b8d237723a429d18=1665836393",
                "Referer": "https://www.ft12.com/",
                "Referrer-Policy": "strict-origin-when-cross-origin",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
            },
            data=f"url={urllib.parse.quote(link)}&host=985.so&random={rnum}&token=",
        )
        return req.json().get("url")
