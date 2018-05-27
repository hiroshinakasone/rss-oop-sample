# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class FeedConverter(ABC):
    """ フィードの内容をカスタマイズするためのInterface """
    @abstractmethod
    def convert_title(self, title):
        raise NotImplemented()

    @abstractmethod
    def convert_summary(self, summary):
        raise NotImplemented()

    @abstractmethod
    def convert_published(self, published):
        raise NotImplemented()
