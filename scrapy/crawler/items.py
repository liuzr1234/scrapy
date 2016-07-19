# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ActorItem(Item):
    platform = Field()
    liked = Field()
    followed = Field()
    exp = Field()
    level = Field()
    uid = Field()
    nickname = Field()
    page = Field()
    status = Field()
    tags = Field()
    description = Field()
    avatar = Field()
    gender = Field()
    location = Field()
    raw_data = Field()
    weibo = Field()


class ShowItem(Item):
    # 动态数据
    liked = Field()
    watched = Field()
    status = Field()
    duration = Field()  # 直播时长
    start_time = Field()
    end_time = Field()
    platform = Field()
    cate1 = Field()
    cate1_alias = Field()
    cate2 = Field()
    cate2_alias = Field()
    show_id = Field()
    actor_id = Field()
    thumb = Field()
    title = Field()
    live_url = Field()
    live_url_m = Field()
    location = Field()
    quality = Field()
    raw_data = Field()
