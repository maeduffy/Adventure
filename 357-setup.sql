DROP TABLE IF EXISTS Leaderboard;

DROP TABLE IF EXISTS CurrentItems;

DROP TABLE IF EXISTS CompletedProjects;

DROP TABLE IF EXISTS CompletedTests;

DROP TABLE IF EXISTS Characters;

DROP TABLE IF EXISTS ProjectItems;

DROP TABLE IF EXISTS Health;

DROP TABLE IF EXISTS Rooms;

DROP TABLE IF EXISTS Projects;

DROP TABLE IF EXISTS Scores;

DROP TABLE IF EXISTS Items;

DROP TABLE IF EXISTS Questions;

DROP TABLE IF EXISTS Tests;


CREATE TABLE Tests (
	id INT,
	name VARCHAR(32),
	CONSTRAINT T_PK PRIMARY KEY (id)
);

CREATE TABLE Questions(
	id INT,
	test INT,
	testQuestion INT,
	question VARCHAR(255),
	answer VARCHAR(255),
	CONSTRAINT Q_PK PRIMARY KEY (id),
	CONSTRAINT Q_UNIQUE1 UNIQUE(test, testQuestion),
	CONSTRAINT Q_UNIQUE2 UNIQUE(question),
	CONSTRAINT Q_FK FOREIGN KEY(test) REFERENCES Tests(id)
);

CREATE TABLE Health (
	percent INT,
	meaning VARCHAR(128),
	CONSTRAINT H_PK PRIMARY KEY(percent),
	CONSTRAINT H_UNIQUE UNIQUE (meaning)
);

CREATE TABLE Items (
	id INT,
	name VARCHAR(32),
	message VARCHAR(255),
	CONSTRAINT I_PK PRIMARY KEY (id),
	CONSTRAINT I_UNIQUE UNIQUE(name)
);

CREATE TABLE Scores(
	score INT,
	healthEffect INT,
	CONSTRAINT S_PK PRIMARY KEY(score)
);

CREATE TABLE Projects(
	id INT,
	name VARCHAR(32),
	message VARCHAR(255),
	CONSTRAINT P_PK PRIMARY KEY(id)
);

CREATE TABLE ProjectItems (
	id INT,
	projectID INT,
	itemID INT,
	CONSTRAINT PI_PK PRIMARY KEY (id),
	CONStRAINT PI_UNIQUE UNIQUE(projectID, itemID)
);

CREATE TABLE Rooms (
	id INT,
	pass1 INT,
	pass2 INT,
	pass3 INT,
	itemID INT,
	projectID INT,
	phrase TEXT,
	CONSTRAINT R_PK PRIMARY KEY(id),
-- 	CONSTRAINT R_FK_P1 FOREIGN KEY (pass1) REFERENCES Rooms(id),
-- 	CONSTRAINT R_FK_P2 FOREIGN KEY (pass2) REFERENCES Rooms(id),
--	CONSTRAINT R_FK_P3 FOREIGN KEY (pass3) REFERENCES Rooms(id),
	CONSTRAINT R_FK_I FOREIGN KEY (itemID) REFERENCES Items(id),
	CONSTRAINT R_FK_P FOREIGN KEY (projectID) REFERENCES Projects(id),
	CONSTRAINT R_UNIQUE UNIQUE(pass1, pass2, pass3, itemID, projectID)
);

CREATE TABLE Characters (
	id INT AUTO_INCREMENT,
	name VARCHAR(32),
	health INT,
	currentRoom INT,
	CONSTRAINT C_PK PRIMARY KEY (id),
	CONSTRAINT C_UNIQUE UNIQUE (name),
	CONSTRAINT C_FK_H FOREIGN KEY(health) REFERENCES Health(percent),
	CONSTRAINT C_FK_R FOREIGN KEY(currentRoom) REFERENCES Rooms(id)
);

CREATE TABLE CompletedTests (
	CharId INT,
	id INT,
	score INT,
	CONSTRAINT CT_PK PRIMARY KEY (CharId, id),
	CONSTRAINT CT_FK_S FOREIGN KEY (score) REFERENCES Scores(score),
	CONSTRAINT CT_FK_C FOREIGN KEY (CharId) REFERENCES Characters(id),
	CONSTRAINT CT_FK_T FOREIGN KEY (id) REFERENCES Tests(id)
);

CREATE TABLE CompletedProjects (
	CharId INT,
	id INT,
	score INT,
	CONSTRAINT CP_PK PRIMARY KEY (CharId, id),
	CONSTRAINT CP_FK_C FOREIGN KEY (CharId) REFERENCES Characters(id),
	CONSTRAINT CP_FK_P FOREIGN KEY (id) REFERENCES Projects(id),
	CONSTRAINT CP_FK_S FOREIGN KEY (score) REFERENCES Scores(score)
);

CREATE TABLE CurrentItems (
	CharId INT,
	id INT,
	CONSTRAINT CI_PK PRIMARY KEY (CharId, id),
	CONSTRAINT CI_FK_I FOREIGN KEY (id) REFERENCES Items(id),
	CONSTRAINT CI_FK_C FOREIGN KEY (CharId) REFERENCES Characters(id)
);

CREATE TABLE Leaderboard (
	id INT AUTO_INCREMENT,
	charID INT,
	score INT,
	CONSTRAINT L_PK PRIMARY KEY(id),
	CONSTRAINT L_UNIQUE UNIQUE (charID),
	CONSTRAINT L_FK_C FOREIGN KEY(charID) REFERENCES Characters(id)
);
