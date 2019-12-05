CREATE DATABASE PrimoEmailLocal;
USE PrimoEmailLocal;



CREATE TABLE emails (
	email_id INT UNIQUE,
	sender VARCHAR(100),
	receiver VARCHAR(100),
	subject TEXT,
	body TEXT,
	sent_date DATETIME,
	PRIMARY KEY (email_id)
	);
	
CREATE TABLE messages (
	sender_address VARCHAR(100),
	message_id INT UNIQUE,
	chatroom_id INT,
	message TEXT,
	sent_date DATETIME,
	PRIMARY KEY (message_id)
);

CREATE TABLE emaiL_chatroom (
	chatroom_id INT,
	address VARCHAR(100),
	PRIMARY KEY(chatroom_id, address)
);

CREATE TABLE chatroom (
	chatroom_id INT UNIQUE,
	chatroom_name VARCHAR(50),
	PRIMARY KEY (chatroom_id)
);