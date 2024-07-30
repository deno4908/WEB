import requests,re
def FB(cookiesX):
    cookies = {
        'sb': cookiesX.split('sb=')[1].split(';')[0],
        'datr': cookiesX.split('datr=')[1].split(';')[0],
        'c_user': cookiesX.split('c_user=')[1].split(';')[0],
        'xs': cookiesX.split('xs=')[1].split(';')[0],
        'fr': cookiesX.split('fr=')[1].split(';')[0],
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'datr=LimoZiOW78YJ1BBxxxntecZy; ps_l=1; ps_n=1; sb=XyqoZl_z-ywr74mdUcCFFcaf; dpr=1.5625; c_user=100041984710675; fr=1uyXez4qxUG5dXcbW.AWUqQTHhSyE03muEnVo2gYI5mcs.BmqGPk..AAA.0.0.BmqGPk.AWULXjnGn2M; xs=4%3AFIBR8ibhPU70xg%3A2%3A1722309827%3A-1%3A6312%3A%3AAcU26-9RnH7GJdNRmbOf_IHCmeNUUbbs9rXCXpOK3g; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1722311654685%2C%22v%22%3A1%7D; wd=678x584',
        'origin': 'https://www.facebook.com',
        'priority': 'u=1, i',
        'referer': 'https://www.facebook.com/photo/?fbid=417986634414551&set=a.112237031656181',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.73", "Chromium";v="127.0.6533.73"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'CometUFIFeedbackReactMutation',
        'x-fb-lsd': 'XoO-HPUEBt2-pU3v3WYBIL',
    }
    url2 = requests.get('https://www.facebook.com/reel/100015530232485_1799884437205880',headers=headers,cookies=cookies).url
    # url = 'https://www.facebook.com/permalink.php?story_fbid=pfbid026eozzf7SGYvsnRdwbfoFsb4iBiekvJmh6w8HAFtB7Zw67dKaxyYE3ECHrRsczDuKl&id=100014740183335'
    response = requests.get(url2,headers=headers,cookies=cookies).text

    print(response)
    baseurl = requests.get('https://mbasic.facebook.com',headers=headers,cookies=cookies).text
    # av = re.findall('action="/composer.*?&',baseurl)
    # ACTOR_ID = str(av).split('av=')[1].split('&')[0]
    dtsgget = re.findall('{"u".*?}',check)
    fb_dtsg = str(dtsgget).split('"f":"')[1].split('"')[0]
    print(fb_dtsg)
FB('sb=0_48Zfh1G5VRMugzfUdCF_Cq; ps_n=1; ps_l=1; datr=rDmhZkMHE4zu18zDj17i7Miq; locale=vi_VN; wl_cbv=v2%3Bclient_version%3A2574%3Btimestamp%3A1722224224; vpd=v1%3B915x412x2.6249998807907104; dpr=1.25; c_user=100054285126320; xs=31%3AgQVLQ4Pm802x2g%3A2%3A1722313936%3A-1%3A6308; fr=18WUw1C9ki8jwyB3F.AWUfc8H6hHcTJdCJEvKSqx3epDk.BmqGy3..AAA.0.0.BmqGzT.AWU48B6SLS8; m_page_voice=100054285126320; wd=692x740; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1722314480078%2C%22v%22%3A1%7D')