# -*- coding: utf-8 -*-

import click
from injector import Injector

from rss.infra.appconfig import app_config
from rss.infra.di import configure_for_rss_service
from rss.app.service import RssService


@click.command()
@click.argument("uris", nargs=-1, type=click.STRING)
@click.option("--title-only", is_flag=True, default=False, help="タイトルのみを表示します", type=click.BOOL)
def command(uris, title_only):
    app_config.arguments["uris"] = uris
    app_config.options["title_only"] = title_only
    injector = Injector([configure_for_rss_service])
    service = injector.get(RssService)
    service.convert_feeds()


def main():
    command()


if __name__ == "__main__":
    main()
