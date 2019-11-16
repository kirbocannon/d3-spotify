#!/usr/bin/env python
import os
import yaml
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def read_yaml_file(filepath):
    """ Read YAML file """

    with open(filepath, 'r') as stream:
        data = yaml.safe_load(stream)

    return data


def get_tracks_from_playlist(track_results):
    tracks = set()

    for i, item in enumerate(track_results['items']):
        track = item['track']
        tracks.add(track['name'])

    return list(tracks)


def create_json_file(data):
    with open(os.path.join(
            'app',
            'static',
            'data',
            'spotifyData.json'), 'w+') as f:
        f.write(json.dumps(data, indent=4))

    return True


def main():
    config = read_yaml_file('credentials.yaml')
    USERNAME = config['username']
    client_credentials_manager = SpotifyClientCredentials(
        client_id=config['client_id'],
        client_secret=config['client_secret']
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlists = sp.user_playlists(USERNAME)
    graph = {'nodes': [], 'links': []}
    all_tracks = []

    while True:
        for playlist in playlists['items']:
            graph['nodes'].append({'id': playlist['name'], 'nodeType': 'playlist'})
            track_results = sp.user_playlist(
                USERNAME, playlist['id'],
                fields="tracks,next")['tracks']
            tracks = get_tracks_from_playlist(track_results)
            graph['links'].extend([{'source': track_name, 'target': playlist['name']} for track_name in tracks])
            all_tracks.extend(tracks)
            while track_results['next']:
                track_results = sp.next(track_results)
                tracks = get_tracks_from_playlist(track_results)
                graph['links'].extend([{'source': track_name, 'target': playlist['name']} for track_name in tracks])
                all_tracks.extend(tracks)

        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            break

    graph['nodes'].extend({'id': track, 'nodeType': 'track', 'playlists': []} for track in list(set(all_tracks)))

    for link in graph['links']:
        for node in graph['nodes']:
            if node['nodeType'] == 'track':
                if link['source'] == node['id']:
                    node['playlists'].append(link['target'])

    _ = create_json_file(graph)


if __name__ == '__main__':
    main()
