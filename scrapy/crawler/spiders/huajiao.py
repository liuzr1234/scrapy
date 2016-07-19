# -*- coding: utf-8 -*-

import re
import json

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawler.items import ActorItem, ShowItem


class HuajiaoSpider(CrawlSpider):
    name = "huajiao"
    allowed_domains = ["huajiao.com"]
    start_urls = (
        'http://www.huajiao.com/',
    )

    rules = (
        # 分析首页热门数据
        # Rule(LinkExtractor(allow=r'/$'), callback='parse_index', follow=True),
        # 直播详情页，抓取关键信息
        Rule(LinkExtractor(allow=r'/l/\d+'), callback='parse_show', follow=False),
        # 分类列表页，不分析数据，只是为了不断翻页找到新的直播详情页
        Rule(LinkExtractor(allow=r'/category/\d+'), follow=True),
    )

    def parse_index(self, response):
        '''先不管'''
        for feed in response.css(".g-box.feed-list > div.box-bd > ul > li.feed"):
            actor = ActorItem()
            actor['nickname'] = feed.css("p.user .username::text").extract_first()
            actor['avatar'] = feed.css("p.user .avatar img::attr(src)").extract_first()
            actor['page'] = feed.css("a::attr(href)").extract_first()
            yield actor

    def parse_show(self, response):
        for script in response.css("script"):
            author_re = re.search(r'var author = (.+);\n', script.extract())
            if author_re:
                actor = ActorItem()
                author_json_str = author_re.group(1)
                author_json_python = json.loads(author_json_str)
                actor['uid'] = author_json_python['uid']
                actor['nickname'] = author_json_python['nickname']
                actor['avatar'] = author_json_python['avatar']
                yield actor

            feed_re = re.search(r'var feed = (.+);\n', script.extract())
            if feed_re:
                show = ShowItem()
                feed_json_str = feed_re.group(1)
                feed_json_python = json.loads(feed_json_str)
                show['show_id'] = feed_json_python['feed']['relateid']
                show['thumb'] = feed_json_python['feed']['image']
                show['title'] = feed_json_python['feed']['title']
                yield show
