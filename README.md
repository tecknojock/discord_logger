# dumpbot
Discord bot to dump logs into an SQLite3 database

## Install
`pip install -r requirements.txt`
`python -m dumpbot`

## Table Structure
One table per server, each table has the structure of
```sql
CREATE TABLE server_id (
	DATETIME timestamp,
	INTEGER channel_id,
	INTEGER message_id,
	INTEGER author_id,
	TEXT contents,
    TEXT attachment_hash,
	TEXT attachment_ext
);
```
plus a folder named `blobs/` that will have every attachement in the form of
`attachment_hash.attachment_ext`