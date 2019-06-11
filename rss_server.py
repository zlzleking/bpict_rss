def rssize(data):
    rss_data = []
    rss_header = '''<?xml version="1.0" encoding="UTF-8"?>
                    <rss version="2.0">
	                <channel>
                    <title>bpict rss feed</title>
                    <link>https://t.me/bpict</link>
                    <description>bpict의 rss 피드입니다</description>
                    <language>ko</language>
                    <generator>Zlzleking</generator>'''
    rss_footer = "</channel></rss>"

    for i in range(0, len(data["text"])):
        rss_temp = "<item><title>bpict</title><link>" + \
            data["link"][i] + "</link><description>" + data["text"][i] + \
            "</description><guid>" + data["link"][i] + "</guid></item>"
        rss_data.append(rss_temp)

    rss_temp_2 = "".join(rss_data)
    rss_out = rss_header + rss_temp_2 + rss_footer
    return rss_out
