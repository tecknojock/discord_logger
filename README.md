# dumpbot
Discord bot to dump logs into an SQLite3 database

## Install
`pip install -r requirements.txt`
`python -m dumpbot`

## Database Structure
Each server in the table:
```sql
CREATE TABLE servers (
	INTEGER PRIMARY KEY id,
	TEXT name,
	TEXT server_id
);
```

Each server will also have a table:
```sql
CREATE TABLE server_id (
	INTEGER PRIMARY KEY id,
	TEXT channel_id,
	TEXT name
)
```

One table per channel, each table has the structure of:
```sql
CREATE TABLE channel_id (
	DATETIME timestamp,
	TEXT message_id,
	TEXT author_id,
	TEXT contents,
    TEXT attachment_hash,
	TEXT attachment_ext
);
```

Plus, a folder named `blobs/` outside of the DB that will have every attachement in the form of
`attachment_hash[0-1]/attachment_hash[2-3]/attachment_hash.attachment_ext`