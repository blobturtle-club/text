from mastodon import Mastodon
import config

mastodon = Mastodon(
    client_id=config.id,
    client_secret=config.secret,
    access_token=config.token,
    api_base_url=config.url
)
