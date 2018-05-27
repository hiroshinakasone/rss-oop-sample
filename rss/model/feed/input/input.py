# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Iterator


class FeedUriInput(ABC):
    """ フィードのURIを取得するためのInterface """
    @abstractmethod
    def get_all(self) -> Iterator[str]:
        raise NotImplemented()
