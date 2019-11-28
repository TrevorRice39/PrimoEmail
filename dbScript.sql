CREATE DATABASE PrimoEmail;
USE PrimoEmail;



CREATE TABLE emails (
	email_id INT AUTO_INCREMENT,
	message TEXT,
	PRIMARY KEY (email_id)
	);
	
CREATE TABLE messages (
	message_id INT AUTO_INCREMENT,
	message TEXT,
	PRIMARY KEY (message_id)
);