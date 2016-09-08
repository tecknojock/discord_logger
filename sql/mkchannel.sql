CREATE TABLE IF NOT EXISTS channel_id (
	PRIMARY KEY TEXT message_id,
	DATETIME timestamp,
	TEXT author_id,
	TEXT contents,
	TEXT attachment_name,
    TEXT attachment_hash
);
