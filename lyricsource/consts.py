# -*- coding: utf-8 -*-
#
# Copyright (C) 2011  Tiger Soldier
#
# This file is part of OSD Lyrics.
#
# OSD Lyrics is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OSD Lyrics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OSD Lyrics.  If not, see <http://www.gnu.org/licenses/>.
#

# D-Bus names, interfaces and object paths
DAEMON_INTERFACE = 'org.lyricsource.Daemon'
DAEMON_BUS_NAME = 'org.lyricsource.Daemon'
DAEMON_OBJECT_PATH = '/org/lyricsource/Daemon'
MPRIS2_PREFIX = 'org.mpris.MediaPlayer2.'
DAEMON_MPRIS2_NAME = 'org.mpris.MediaPlayer2.lyricsource'

CONFIG_BUS_NAME = 'org.lyricsource.Config'
CONFIG_OBJECT_PATH = '/org/lyricsource/Config'
PLAYER_PROXY_INTERFACE = 'org.lyricsource.PlayerProxy'
PLAYER_PROXY_OBJECT_PATH_PREFIX = '/org/lyricsource/PlayerProxy/'
MPRIS2_PLAYER_INTERFACE = 'org.mpris.MediaPlayer2.Player'
MPRIS2_OBJECT_PATH = '/org/mpris/MediaPlayer2'
LYRIC_SOURCE_PLUGIN_INTERFACE = 'org.lyricsource.LyricSourcePlugin'
LYRIC_SOURCE_PLUGIN_OBJECT_PATH_PREFIX = '/org/lyricsource/LyricSourcePlugin/'

# Metadata keys
METADATA_TITLE = 'title'
METADATA_ARTIST = 'artist'
METADATA_ALBUM = 'album'
METADATA_TRACKNUM = 'tracknum'
METADATA_URI = 'location'
