# Forked-Daapd Component
Forked from Core component to be able to play playlist, album or track by calling HA service  
**TTS is not working**

## How to get the uri for media_content_id?

First you need to get the id of what you want to listen to using JSON API in your browser or curl. You will need probably to play with these endpoints:

| Method | Endpoint | Description |
|---|---|---|
|GET|/api/library/playlists|Get a list of playlists|
|GET|/api/library/playlists/{id}/tracks|Get list of tracks for a playlist|
|GET|/api/library/artists|Get a list of artists|
|GET|/api/library/artists/{id}/albums|Get list of albums for an artist|
|GET|/api/library/albums|Get a list of albums|
|GET|/api/library/albums/{id}/tracks|Get list of tracks for an album|
For the full list of endpoints, check this [page](https://github.com/owntone/owntone-server/blob/master/README_JSON_API.md#library)

Uri format is library:xxxx:9999, you will create it by concatenating:
1. Start with the term ```library```
2. Add one of the resource identifiers according of what you searched for previously: track, playlist, artist or album
3. The id you got using JSON API

## Example

In Home Assistant, call service ```media_player.play_media``` and the following example will play track with id 62.
```
entity_id: media_player.forked_daapd_server
media_content_id: 'library:track:25904'
media_content_type: music
```
