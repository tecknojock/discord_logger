CREATE TABLE IF NOT EXISTS ? (
	message_id PRIMARY KEY TEXT,
	timestamp DATETIME,
	author_id TEXT,
	contents TEXT,
	attachment_name TEXT,
    attachment_hash TEXT
);