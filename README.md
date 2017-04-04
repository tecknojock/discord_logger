# Discord Logger
Logging for Discord, álá IRC

## Dependencies

 * Python +3.5
 * `discord.py` to connect to Discord servers

## Installation

### Recommended Method

 * Run `pip install discord-logger`, or `pipsi install discord-logger` if you have [`pipsi`](https://github.com/mitsuhiko/pipsi) installed (which I strongly recommend you do).
 * That's it!


### Advanced Method

 * Clone the repository with `git clone https://github.com/anodium/discord-logger.git`.
 * Navigate to the newly cloned repository
 * Install the dependencies with `pip install -r requirements.txt`.
 * Install `discord-logger` itself with `python setup.py install`.

## Running

 * Set the `DISCORD_TOKEN` environment variable to your personal login token (Note: this *cannot* be a bot token, or an alt-account's token, it must be **your** user token).
  * You can log in on the Discord client, pop open the web inspector with Ctrl-Shift-I, and type `localStorage.token` in the console to get your auth token.
  * **WARNING:** As the console may warn you, do **NOT** give your auth token to *anyone*, as it can be easily used to access the entirety of your account!
 * Navigate to the root directory of your logs.
 * Run `python discord-logger.py` and leave it running in the background.
