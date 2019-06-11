import time
from datetime import datetime


def rssize(data):
    rss_data = []
    nowtime = time.time()
    timestamp = datetime.utcfromtimestamp(
        int(nowtime)+32400).strftime('%A, %d %m %y %H:%M:%S +0900')
    rss_header = '''<?xml version="1.0" encoding="UTF-8"?>
                    <rss version="2.0">
	                <channel>
                    <title>bpict rss feed</title>
                    <link>https://t.me/bpict</link>
                    <managingEditor>https://t.me/bpict</managingEditor>
                    <webMaster>zlzleking@gmail.com</webMaster>
                    <description>bpict의 rss 피드입니다</description>
                    <language>ko</language>
                    <image>
                        <url>https://bpict.zlzleking.tk/img/bpict_logo.jpg</url>
                        <width>400</width>
                        <height>400</height>
                        <title>bpict 로고</title>
                        <link>https://t.me/bpict</link>
                    </image>
                    <generator>https://github.com/zlzleking/bpict_rss</generator><pubDate>''' + timestamp + "</pubDate><lastBuildDate>" + timestamp + "</lastBuildDate>"
    rss_footer = "</channel></rss>"

    for i in range(0, len(data["text"])):
        rss_temp = "<item><title>bpict</title><link>" + \
            data["link"][i] + "</link><description>" + data["text"][i] + \
            "</description><guid>" + \
            data["link"][i] + " </guid><pubDate>" + \
            data["timestamp"][i] + "</pubDate></item >"
        rss_data.append(rss_temp)

    rss_temp_2 = "".join(rss_data)
    rss_out = rss_header + rss_temp_2 + rss_footer
    return rss_out
