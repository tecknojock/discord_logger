# dumpbot
Discord bot to dump logs into an SQLite3 database

## Install
`pip install -r requirements.txt`
`python -m dumpbot`

## Database Structure
Every server in the database will be stored in a table named `servers`,
that is using the schema in `sql/mkserverlist.sql`.

Each *individual* server will also have a table named after its server ID,
using the schema in `sql/mkserver.sql`.

Then, each channel in each server
Plus, a folder named `blobs/` outside of the DB that will have every attachement in the form of
`attachment_hash[0-1]/attachment_hash[2-3]/attachment_hash.attachment_ext`
