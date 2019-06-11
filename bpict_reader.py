from bs4 import BeautifulSoup as soup
import requests as rqs
import re


class bpict_readnphase:

    def bpict_read():
        bpict_url = "https://twitter.com/bpict_"
        bpict_response = rqs.get(bpict_url)
        return(bpict_response.text)

    def bpict_phase(data):
        bpict_tweet_dat = {"text": [], "timestamp": [], "link": [], "pic": []}
        bpict_url = "https://twitter.com/bpict_"
        bpict_response = rqs.get(bpict_url)
        bpict_object = soup(bpict_response.text, 'html.parser')
        bpict_phased = bpict_object.select(".tweet > .content")

        bpict_timestamp = bpict_object.select(
            ".tweet > .content > .stream-item-header > .time > .tweet-timestamp > span")
        bpict_tweet = bpict_object.select(
            ".tweet > .content > .js-tweet-text-container > .tweet-text")
        bpict_tweetlink = bpict_object.select(
            ".tweet > .content > .stream-item-header > .time > .js-permalink")
        bpict_tweetpic = bpict_object.select(
            ".tweet > .content > .js-media-container > div > iframe > html > body > div > .CardContent > a > div > .tcu-imageContainer > .tcu-imageWrapper > img ")

        for dat in bpict_tweet:
            dattext = dat.text

            datt = re.sub('(..pic.twitter.com/.*)', "", dattext)
            try:
                linkfind = re.search('(https://.*)', datt).group()
                datt_1 = re.sub('(https://.*)', "&lt;br&gt;&lt;a href=&quot;" +
                                linkfind + "&quot;&gt;" + linkfind + "&lt;/a&gt;", datt)
            except:
                linkfind = ""
            print(linkfind)
            bpict_tweet_dat["text"].append(datt_1 + "&lt;br&gt;")

        for timestamp in bpict_timestamp:
            bpict_tweet_dat["timestamp"].append(timestamp.text)
        for link in bpict_tweetlink:
            bpict_tweet_dat["link"].append(
                "https://twitter.com"+link.get("href"))
        return bpict_tweet_dat