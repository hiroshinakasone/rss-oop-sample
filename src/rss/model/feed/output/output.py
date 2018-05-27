# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

from ..item import FeedItem


class FeedOutput(ABC):
    """ フィードの内容を出力するためのInterface """
    @abstractmethod
    def output(self, feed_item: FeedItem) -> None:
        raise NotImplemented()
