# -*- coding: utf-8 -*-
from django.conf import settings
from appconf import AppConf


class GuildmasterAppConf(AppConf):
    class Meta:
        prefix = 'guildmaster'
        proxy = False
