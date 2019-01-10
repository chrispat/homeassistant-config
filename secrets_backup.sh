#!/bin/bash

pushd /config

scp .ios.conf peter@home-nas.lan:~/home-assistant-secrets
scp .ring_cache.pickle peter@home-nas.lan:~/home-assistant-secrets
scp ecobee.conf peter@home-nas.lan:~/home-assistant-secrets
scp home-assistant_v2.db peter@home-nas.lan:~/home-assistant-secrets
scp home-assistant.log peter@home-nas.lan:~/home-assistant-secrets
scp ip_bans.yaml peter@home-nas.lan:~/home-assistant-secrets
scp known_devices.yaml peter@home-nas.lan:~/home-assistant-secrets
scp life360.conf peter@home-nas.lan:~/home-assistant-secrets
scp OZW_Log.txt peter@home-nas.lan:~/home-assistant-secrets
scp plex.conf peter@home-nas.lan:~/home-assistant-secrets
scp pyozw.sqlite peter@home-nas.lan:~/home-assistant-secrets
scp sabnzbd.conf peter@home-nas.lan:~/home-assistant-secrets
scp secrets.yaml peter@home-nas.lan:~/home-assistant-secrets
scp ui-lovelace.yaml peter@home-nas.lan:~/home-assistant-secrets
scp zwcfg_0xc13cc76f.xml peter@home-nas.lan:~/home-assistant-secrets
scp zwscene.xml peter@home-nas.lan:~/home-assistant-secrets

popd