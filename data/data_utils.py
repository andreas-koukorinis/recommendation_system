#!/usr/bin/env python
# coding=utf-8
import os
import random
from pymongo import MongoClient


class TvrainData():
    def __init__(self):
        """
        :param data: Pandas Frame with data.
        Just load data from Mongo.
        """
        mongodb_items = list(MongoClient(os.environ['MONGODB_URL']).tvrain.tvrain.find())
        self.dataframe = pd.DataFrame.from_dict(mongodb_items)

        # This shit is about mongo can't save id -> str.
        self.dataframe._id = list(map(str, self.dataframe._id.values))

    def get_random_articles(self, n):
        """Returns N of topics for index.html"""
        sorted_time = sorted(self.dataframe.time.values)
        # We need indexes for slice in time
        index = sorted_time.index(random.choice(sorted_time))
        times = sorted_time[index:index+n]

        articles = []
        for val in self.dataframe[self.dataframe.time.isin(times)].values:
            articles.append({'_id': val[0], 'title': val[3]})

        return articles

    def get_articles_data(self, articles_ids):
        """
        Get data from MongoDB for articles_ids
        :param articles_ids: ['article_id', ...]
        :return: list of MongoDB documents
        """
        raise NotImplemented()

    def iterate_articles(self, except_articles):
        """
        Iteate throw all articles without ids of except articles
        :param except_articles: list of ids
        :return:
        """
        raise NotImplemented()


