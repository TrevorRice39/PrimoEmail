CREATE DATABASE PrimoEmail;
USE PrimoEmail;



CREATE TABLE emails (
	email_id INT AUTO_INCREMENT,
	sender VARCHAR(100),
	receiver VARCHAR(100),
	subject TEXT,
	body TEXT,
	sentDate DATETIME,
	PRIMARY KEY (email_id)
	);
	
CREATE TABLE messages (
	message_id INT AUTO_INCREMENT,
	message TEXT,
	PRIMARY KEY (message_id)
);primoemailemails