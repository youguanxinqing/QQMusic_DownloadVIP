import re
import sys
import requests

from urllib import parse

from CONFIG import *


def get_one_html(url):
    """
    根据url下载对应网页内容，这里是JSON数据
    :param url:
    :return:
    """
    try:
        response = requests.get(url=url, headers=HEADERS)
        response.raise_for_status()
    except:
        return None

    else:
        return response.text

def extract_albummid(data):
    """
    用于提取albummid
    :param data:
    :return:
    """
    result = re.search(r'"mid":"(\w+?)"', data)
    if result:
        return result.group(1)
    else:
        return None

def extract_songmid(data):
    """
    1. 用于提取songid
    2. 用于提取歌手名字
    :param data:
    :return:
    """
    global SONGNAME
    global SINGER

    SINGER = re.search(r'"singername":"(.+?)"', data).group(1)
    results = re.findall(r'"songmid":"(\w+?)","songname":"(.+?)"', data)

    print("【歌曲名字：{songname}】".format(songname=SONGNAME))
    print("【歌手名字：{singer}】".format(singer=SINGER))

    if results:
        for result in results:
            if SONGNAME in result:
                return result[0]
        else:
            return None
    else:
        return None

def extract_vkey(data):
    """
    用于提取vkey
    :param data:
    :return:
    """
    result = re.search(r'"vkey":"(\w+?)"', data)
    if result:
        return result.group(1)
    else:
        return None

def download_song(url):
    """
    下载歌曲
    :param url:
    :return:
    """
    global SINGER # 声明SINGER是全局变量

    try:
        response = requests.get(url=url, headers=HEADERS)
        response.raise_for_status()
    except:
        print("【下载歌曲失败】")
        return None
    else:
        with open(
            "{filename}-{singer}.mp3".format(filename=SONGNAME, singer=SINGER), "wb") as file:

            file.write(response.content)

        print("【下载歌曲成功】")
        return True

def qqmusic(songname):
    """
    执行整个下载歌曲过程的主要逻辑
    :param songname:
    :return:
    """

    global SONGNAME # 声明SONGNAME是全局变量
    SONGNAME = songname

    # 构建请求albumid的query参数
    PARAMS_FOR_SEARCH["w"] = SONGNAME
    dataAlbum = get_one_html(URL_FOR_SEARCH+parse.urlencode(PARAMS_FOR_SEARCH))
    if not dataAlbum:
        print("请求ablummid的网页数据失败")
        return None

    else:
        # 提取albummid
        albummid = extract_albummid(dataAlbum)
        if not albummid:
            print("提取albummid失败")
            return None

        # 构建请求songmid的query参数
        PARAMS_FOR_SONGMID["albummid"] = albummid
        dataSong = get_one_html(URL_FOR_SONGMID+parse.urlencode(PARAMS_FOR_SONGMID))
        if not dataSong:
            print("请求songmid的网页数据失败")
            return None

        songmid = extract_songmid(dataSong)


        # 构建请求vke的query参数
        PARAMS_FOR_VKEY["songmid"] = songmid
        PARAMS_FOR_VKEY["filename"] = "C400{songmid}.m4a".format(songmid=songmid)
        dataVkey = get_one_html(URL_FOR_VKEY+parse.urlencode(PARAMS_FOR_VKEY))
        if not dataVkey:
            print("请求vkey的网页数据失败")
            return None

        vkey = extract_vkey(dataVkey)


        # 构建下载歌曲的query参数
        PARAMS_FOR_VIPSONG["vkey"] = vkey
        url = parse.urljoin(URL_FOR_VIPSONG, "C400"+songmid+".m4a?")

        # 下载歌曲
        download_song(url+"?"+parse.urlencode(PARAMS_FOR_VIPSONG))
