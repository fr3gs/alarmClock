#!/usr/bin/python3
import sys
import vlc
from time import sleep

def play_radio(url, parameters):

    vlcinstance = vlc.Instance()

    player = vlcinstance.media_player_new()
    media = vlcinstance.media_new(url, parameters)
    media.get_mrl()

    player.set_media(media)
    player.play()
    return media

radioURL = 'http://icecast.vrtcdn.be/stubru-high.mp3'

parameters = " network-caching=1000"

play_radio(radioURL, parameters)
while True:
    try:
        sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)