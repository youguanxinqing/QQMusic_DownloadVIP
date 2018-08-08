URL_FOR_SEARCH = "https://shc.y.qq.com/soso/fcgi-bin/client_search_cp?"

URL_FOR_SONGMID = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg?"

URL_FOR_VKEY = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?"

URL_FOR_VIPSONG = "http://dl.stream.qqmusic.qq.com/C400000Md1wq0vnwzE.m4a?"



HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}


PARAMS_FOR_SEARCH = {
    "ct": 24,
    "qqmusic_ver": 1298,
    "new_json": 1,
    "remoteplace": "txt.yqq.center",
    "searchid": 51033819347312583,
    "t": 0,
    "aggr": 1,
    "cr": 1,
    "catZhida": 1,
    "lossless": 0,
    "flag_qc": 0,
    "p": 1,
    "n": 1,
    "w": "说好的幸福呢",
    "g_tk": 5381,
    "jsonpCallback": "MusicJsonCallback976107311063823",
    "loginUin": 0,
    "hostUin": 0,
    "format": "jsonp",
    "inCharset": "utf8",
    "outCharset": "utf-8",
    "notice": 0,
    "platform": "yqq",
    "needNewCode": 0,
}

PARAMS_FOR_SONGMID = {
    "albummid": "",
    "g_tk": 5381,
    "jsonpCallback": "albuminfoCallback",
    "loginUin": 0,
    "hostUin": 0,
    "format": "jsonp",
    "inCharset": "utf8",
    "outCharset": "utf-8",
    "notice": 0,
    "platform": "yqq",
    "needNewCode": 0
}

PARAMS_FOR_VKEY = {
    "g_tk": 5381,
    "jsonpCallback": "MusicJsonCallback8068498502205605",
    "loginUin": 0,
    "hostUin": 0,
    "format": "json",
    "inCharset": "utf8",
    "outCharset": "utf-8",
    "notice": 0,
    "platform": "yqq",
    "needNewCode": 0,
    "cid": 205361747,
    "callback": "MusicJsonCallback8068498502205605",
    "uin": 0,
    "songmid": "",
    "filename": "",
    "guid": 128924851
}

PARAMS_FOR_VIPSONG = {
    "vkey": "",
    "guid": 128924851,
    "uin": 0,
    "fromtag": 66
}


SONGNAME = ""
SINGER = ""