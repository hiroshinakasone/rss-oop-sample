# -*- coding: utf-8 -*-

from injector import singleton

from ..infra.appconfig import app_config
from ..model.feed.input import FeedUriInput
from ..model.feed.output import FeedOutput
from ..model.feed.parser import FeedParser
from ..model.feed.converter import FeedConverter
from ..model.feed.input.console import ConsoleInput
from ..model.feed.output.console import ConsoleOutput, ConsoleOutputTitleOnly
from ..model.feed.parser.wrapped import WrappedFeedParser
from ..model.feed.converter.shortandjp import ShortAndJapaneseConverter


def configure_for_rss_service(binder):
    """ DIコンテナの設定をします """
    binder.bind(FeedUriInput, ConsoleInput, scope=singleton)
    binder.bind(FeedParser, WrappedFeedParser, scope=singleton)
    binder.bind(FeedConverter, ShortAndJapaneseConverter, scope=singleton)

    if app_config.options["title_only"]:
        binder.bind(FeedOutput, ConsoleOutputTitleOnly, scope=singleton)
    else:
        binder.bind(FeedOutput, ConsoleOutput, scope=singleton)
