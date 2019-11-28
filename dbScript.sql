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
	message_id INT AUTO_INCREMENT,
	chatroom_id INT,
	message TEXT,
	sent_date DATETIME,
	PRIMARY KEY (message_id)
);