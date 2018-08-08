import sys
from DowloadSong import *


def notice_format():
    """
    提示格式
    :return:
    """
    print("-*-"*20)
    print("【解释器】【程序名】【歌曲名】")
    print("python3 main.py 体面")
    print("-*-"*20)


def main():
    # print(sys.argv)
    if len(sys.argv) != 2:
        print("【格式错误】")
        notice_format()
        return

    else:
        qqmusic(sys.argv[1])


if __name__ == "__main__":
    main()