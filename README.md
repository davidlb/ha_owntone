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
You can also use the [Search endpoint](https://github.com/owntone/owntone-server/blob/master/README_JSON_API.md#search).

## Example

To find a specific track, I use this command:
```
curl -s -X GET "http://localhost:3689/api/search?type=tracks&query=magic" | jq -r '.[].items[] | .artist + " / " + .title, .uri'
```
It will give me uri for each matching the query (```magic``` in my case):
```
Brian Eno / Energy Fools the Magician
library:track:24994
Queen / A Kind Of 'A Kind Of Magic
library:track:20396
Omer Avital Quintet / Magic Carpet
library:track:14113
Red Hot Chili Peppers / Magic Johnson
library:track:18810
Jon Anderson / Magic Love
library:track:7636
Boards of Canada / Magic Teens
library:track:8605
Boards of Canada / Magic Window
library:track:8653
Keith Jarrett / The Magician in You
library:track:14447
```

In Home Assistant, call service ```media_player.play_media``` and the following example will play track ```Keith Jarrett / The Magician in You``` in my case.
```
entity_id: media_player.forked_daapd_server
media_content_id: 'library:track:14447'
media_content_type: music
```
