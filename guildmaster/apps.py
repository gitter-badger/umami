# -*- coding: utf-8 -*-
from django.apps import AppConfig


class GuildmasterConfig(AppConfig):
    name = 'guildmaster'
    verbose_name = 'Guildmaster'

    def ready(self):
        import guildmaster.conf
