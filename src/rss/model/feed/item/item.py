# -*- coding: utf-8 -*-

from ..converter import FeedConverter


class FeedItem(object):
    """ フィードの内容を保持するクラス """
    def __init__(self, title: str, summary: str, published: str, converter: FeedConverter):
        self.title = title
        self.summary = summary
        self.published = published
        self._converter = converter

    def convert(self):
        """
        フィードの内容をルールにしたがって変換して返します。
        自分自身の内容を書き換える破壊的メソッドです。
        """
        self.title = self._converter.convert_title(self.title)
        self.summary = self._converter.convert_summary(self.summary)
        self.published = self._converter.convert_published(self.published)
        return self
