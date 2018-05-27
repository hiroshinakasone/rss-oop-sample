# -*- coding: utf-8 -*-

from datetime import datetime as dt

from .converter import FeedConverter


class ShortAndJapaneseConverter(FeedConverter):
    """ フィードの内容をカスタマイズための設定を記述するクラス """

    weekday_mapper = {
        0: "月",
        1: "火",
        2: "水",
        3: "木",
        4: "金",
        5: "土",
        6: "日"
    }

    def convert_title(self, title):
        """ タイトルを10文字以下に変換します。 """
        return title[:10]

    def convert_summary(self, summary):
        """ 本文を30文字以下に変換します。 """
        return summary[:30]

    def convert_published(self, published):
        """ 公開日時を日本式表記に変換します。 """
        datetime = dt.strptime(published, "%a, %d %b %Y %H:%M:%S %z")
        return "{0}年{1}月{2}日({3}) {4}時{5}分{6}秒".format(
            datetime.year,
            datetime.month,
            datetime.day,
            self.weekday_mapper[datetime.weekday()],
            datetime.hour,
            datetime.minute,
            datetime.second
        )
