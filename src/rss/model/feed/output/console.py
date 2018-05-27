# -*- coding: utf-8 -*-

from ...feed import FeedItem
from .output import FeedOutput


class ConsoleOutput(FeedOutput):
    """ コンソール表示用の出力クラス """
    def output(self, feed_item: FeedItem) -> None:
        print("タイトル: {0}".format(feed_item.title))
        print("本文: {0}".format(feed_item.summary))
        print("公開日時: {0}".format(feed_item.published))
        print("")


class ConsoleOutputTitleOnly(FeedOutput):
    """ タイトルのみを表示 """
    def output(self, feed_item: FeedItem) -> None:
        print("タイトル: {0}".format(feed_item.title))