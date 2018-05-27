# -*- coding: utf-8 -*-

from injector import inject

from rss.model.feed.input import FeedUriInput
from rss.model.feed.output import FeedOutput
from rss.model.feed.parser import FeedParser
from rss.model.feed.converter import FeedConverter


class RssService(object):
    """ RSSのアプリケーションサービスクラス """
    @inject
    def __init__(self,
                 uri_input: FeedUriInput,
                 output: FeedOutput,
                 parser: FeedParser,
                 converter: FeedConverter):
        self._input = uri_input
        self._output = output
        self._parser = parser
        self._converter = converter

    def convert_feeds(self):
        """ フィードを取得し、加工して出力します """
        for uri in self._input.get_all():
            for feed_item in self._parser.parse(uri):
                self._output.output(feed_item.convert())
