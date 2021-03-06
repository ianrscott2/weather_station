# -*- coding:utf-8 -*-

import requests
import logging
import textwrap
import time

class News:
    def __init__(self,width):
        self.width = width

    def update(self, api_id):
        source = "the-washington-post"
        news_url = "https://newsapi.org/v2/top-headlines?source=" + source + "&apiKey=" + api_id + "&country=us"
        got_data = False

        logging.info("-------News Update Begin ")
        while got_data == False:
            logging.info("Checking News URL Status")
            try:
                self.news_data = requests.get(news_url)
            except:
                time.sleep(60)
                continue

            if self.news_data.ok:
                logging.info(self.news_data.status_code)
                got_data = True
                logging.info("Got data from News URL to return successfully")
                self.news_list = self.news_data.json()
            else:
                logging.info("Waiting for the News URL to return successfully")
                self.news_list = None
                time.sleep(15)
        logging.info("-------News Update End")
        return self.news_list


    def selected_title(self):
        list_news = []
        if self.news_list["status"] == "ok":
            for i in range(len(self.news_list["articles"])):
                line = self.news_list["articles"][i]["title"]
                line = textwrap.wrap(line, width=self.width)
                list_news.append(line)
        else:
            list_news = ["Problem getting the news"]
        return list_news
