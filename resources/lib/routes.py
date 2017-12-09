# -*- coding: utf-8 -*-
"""
     
    Copyright (C) 2016 anxdpanic
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import kodi
import log_utils
from constants import DISPATCHER, MODES

i18n = kodi.i18n
addon_id = 'plugin.video.embycon'


@DISPATCHER.register(MODES.MAIN, kwargs=['content_type'])
def main_route(content_type=''):
    kodi.show_settings()


@DISPATCHER.register(MODES.PLAY, args=['video_type', 'title', 'year'], kwargs=['trakt_id', 'episode_id', 'season_id', 'season', 'episode', 'ep_title', 'imdb_id', 'tmdb_id', 'tvdb_id'])
def play_route(video_type, title, year, trakt_id=None, episode_id=None, season_id=None, imdb_id=None, tmdb_id=None, tvdb_id=None, season=None, episode=None, ep_title=None):
    plugin_url = None

    if video_type == 'episode':
        plugin_url = 'plugin://{addon_id}/?mode=TRAKTTOKODI&action=play&video_type={video_type}&season={season}&episode={episode}&imdb_id={imdb_id}&year={year}&title={title}' \
            .format(addon_id=addon_id, video_type=video_type, season=season, episode=episode, imdb_id=imdb_id, year=year, title=title)

    elif video_type == 'movie':
        plugin_url = 'plugin://{addon_id}/?mode=TRAKTTOKODI&action=play&video_type={video_type}&imdb_id={imdb_id}&year={year}&title={title}' \
            .format(addon_id=addon_id, video_type=video_type, imdb_id=imdb_id, year=year, title=title)

    if plugin_url:
        kodi.execute_builtin('ActivateWindow(Videos,{plugin_url})'.format(plugin_url=plugin_url))


@DISPATCHER.register(MODES.OPEN, args=['video_type', 'title', 'year'], kwargs=['trakt_id', 'episode_id', 'season_id', 'season', 'episode', 'ep_title', 'imdb_id', 'tmdb_id', 'tvdb_id'])
def open_route(video_type, title, year, trakt_id=None, episode_id=None, season_id=None, imdb_id=None, tmdb_id=None, tvdb_id=None, season=None, episode=None, ep_title=None):
    plugin_url = None

    if video_type == 'episode':
        play_route(video_type, title, year, trakt_id, episode_id, season_id, imdb_id, tmdb_id, tvdb_id, season, episode, ep_title)

    elif video_type == 'movie':
        play_route(video_type, title, year, trakt_id, episode_id, season_id, imdb_id, tmdb_id, tvdb_id, season, episode, ep_title)

    elif video_type == 'season':
        plugin_url = 'plugin://{addon_id}/?mode=TRAKTTOKODI&action=open&video_type={video_type}&season={season}&imdb_id={imdb_id}&year={year}&title={title}' \
            .format(addon_id=addon_id, video_type=video_type, season=season, imdb_id=imdb_id, year=year, title=title)

    elif video_type == 'show':
        plugin_url = 'plugin://{addon_id}/?mode=TRAKTTOKODI&action=open&video_type={video_type}&imdb_id={imdb_id}&year={year}&title={title}' \
            .format(addon_id=addon_id, video_type=video_type, imdb_id=imdb_id, year=year, title=title)

    if plugin_url:
        kodi.execute_builtin('RunPlugin({plugin_url})'.format(plugin_url=plugin_url))
