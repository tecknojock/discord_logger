# dumpbot
Dump Discord logs into an SQLite3 DB

## Install
 * `pip install -r requirements.txt`
 * Modify `config.json` to add a login token
 * `python -m dumpbot.bot`

## Database Structure
Every server in the database will be stored in a table named `servers`,
that is using the schema in `sql/mkserverlist.sql`.

Each *individual* server will also have a table named after its server ID,
using the schema in `sql/mkserver.sql`.

Then, each channel in each server will have a table named after its ID, they
use the schema in `sql/mkchannel.sql`.

Plus, a folder named `blobs/` outside of the DB that will have every attachement in the form of
`attachment_hash[0-1]/attachment_hash[2-3]/attachment_hash.attachment_ext`
