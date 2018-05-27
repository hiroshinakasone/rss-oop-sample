# -*- coding: utf-8 -*-

from typing import Iterator

from ....infra.appconfig import app_config
from .input import FeedUriInput


class ConsoleInput(FeedUriInput):
    """ コンソールからフィードのURIを取得するクラス """
    def get_all(self) -> Iterator[str]:
        return iter(app_config.arguments["uris"])
