"""Const for forked-daapd."""
from homeassistant.components.media_player import MediaPlayerEntityFeature

CALLBACK_TIMEOUT = 8  # max time between command and callback from forked-daapd server
CONF_LIBRESPOT_JAVA_PORT = "librespot_java_port"
CONF_MAX_PLAYLISTS = "max_playlists"
DEFAULT_PORT = 3689
DEFAULT_SERVER_NAME = "My Server"
DEFAULT_UNMUTE_VOLUME = 0.6
DOMAIN = "owntone_dleb"  # key for hass.data
FD_NAME = "Owntone"
HASS_DATA_REMOVE_LISTENERS_KEY = "REMOVE_LISTENERS"
HASS_DATA_UPDATER_KEY = "UPDATER"
KNOWN_PIPES = {"librespot-java"}
PIPE_FUNCTION_MAP = {
    "librespot-java": {
        "async_media_play": "player_resume",
        "async_media_pause": "player_pause",
        "async_media_stop": "player_pause",
        "async_media_previous_track": "player_prev",
        "async_media_next_track": "player_next",
    }
}
SIGNAL_ADD_ZONES = "forked-daapd_add_zones {}"
SIGNAL_CONFIG_OPTIONS_UPDATE = "forked-daapd_config_options_update {}"
SIGNAL_UPDATE_DATABASE = "forked-daapd_update_database {}"
SIGNAL_UPDATE_MASTER = "forked-daapd_update_master {}"
SIGNAL_UPDATE_OUTPUTS = "forked-daapd_update_outputs {}"
SIGNAL_UPDATE_PLAYER = "forked-daapd_update_player {}"
SIGNAL_UPDATE_QUEUE = "forked-daapd_update_queue {}"
SOURCE_NAME_CLEAR = "Clear queue"
SOURCE_NAME_DEFAULT = "Default (no pipe)"
STARTUP_DATA = {
    "player": {
        "state": "stop",
        "repeat": "off",
        "consume": False,
        "shuffle": False,
        "volume": 0,
        "item_id": 0,
        "item_length_ms": 0,
        "item_progress_ms": 0,
    },
    "queue": {"version": 0, "count": 0, "items": []},
    "outputs": [],
}
SUPPORTED_FEATURES = (
    MediaPlayerEntityFeature.PLAY
    | MediaPlayerEntityFeature.PAUSE
    | MediaPlayerEntityFeature.STOP
    | MediaPlayerEntityFeature.SEEK
    | MediaPlayerEntityFeature.VOLUME_SET
    | MediaPlayerEntityFeature.VOLUME_MUTE
    | MediaPlayerEntityFeature.PREVIOUS_TRACK
    | MediaPlayerEntityFeature.NEXT_TRACK
    | MediaPlayerEntityFeature.CLEAR_PLAYLIST
    | MediaPlayerEntityFeature.SELECT_SOURCE
    | MediaPlayerEntityFeature.SHUFFLE_SET
    | MediaPlayerEntityFeature.TURN_ON
    | MediaPlayerEntityFeature.TURN_OFF
    | MediaPlayerEntityFeature.PLAY_MEDIA
    | MediaPlayerEntityFeature.BROWSE_MEDIA
)
SUPPORTED_FEATURES_ZONE = (
    MediaPlayerEntityFeature.VOLUME_SET
    | MediaPlayerEntityFeature.VOLUME_MUTE
    | MediaPlayerEntityFeature.TURN_ON
    | MediaPlayerEntityFeature.TURN_OFF
)
