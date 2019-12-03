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
	message_id INT AUTO_INCREMENT,
	chatroom_id INT,
	message TEXT,
	sent_date DATETIME,
	PRIMARY KEY (message_id)
);