# -*- coding: utf-8 -*-

from typing import Iterator

from injector import inject

from ...feed import FeedItem
from ..converter import FeedConverter
from .parser import FeedParser


class WrappedFeedParser(FeedParser):
    """ フィードのパーサクラス """
    @inject
    def __init__(self, converter: FeedConverter):
        import feedparser
        self._parser = feedparser
        self._converter = converter

    def parse(self, uri) -> Iterator[FeedItem]:
        """ フィードのパーサ結果を返します """
        for parsed in self._parser.parse(uri)["entries"]:
            yield FeedItem(
                title=parsed["title"],
                summary=parsed["summary"],
                published=parsed["published"],
                converter=self._converter
            )
