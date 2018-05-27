# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Iterator

from ..item import FeedItem


class FeedParser(ABC):
    """ フィードのパース結果を取得するInterface """
    @abstractmethod
    def parse(self, uri) -> Iterator[FeedItem]:
        raise NotImplemented()
