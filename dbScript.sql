CREATE DATABASE PrimoEmail;
USE PrimoEmail;



CREATE TABLE emails (
	email_id INT AUTO_INCREMENT,
	sender VARCHAR(100),
	receiver VARCHAR(100),
	subject TEXT,
	body TEXT,
	sent_date DATETIME,
	PRIMARY KEY (email_id)
	);
	
CREATE TABLE messages (
	sender_address VARCHAR(100),
	message_id INT AUTO_INCREMENT,
	chatroom_id INT,
	message TEXT,
	sent_date DATETIME,
	PRIMARY KEY (message_id)
);

CREATE TABLE emaiL_chatroom (
	chatroom_id INT,
	address VARCHAR(100)
);

CREATE TABLE chatroom (
	chatroom_id INT UNIQUE,
	chatroom_name VARCHAR(50),
	PRIMARY KEY (chatroom_id)
);
