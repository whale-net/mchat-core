CREATE TABLE Users (
uid INTEGER AUTO_INCREMENT,
username CHAR(24) NOT NULL,
global_display_name VARCHAR(64) NOT NULL,
global_avatar CHAR(64),
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
password CHAR(255) NOT NULL, /* alg+salt+hash = ~90-150b */
PRIMARY KEY(uid),
UNIQUE(username)
);

CREATE TABLE Groups (
    gid INTEGER AUTO_INCREMENT,
    creator_id INTEGER,
    owner_id INTEGER NOT NULL,
    name VARCHAR(128),
    PRIMARY KEY (gid),
    FOREIGN KEY (creator_id) REFERENCES Users(uid),
    FOREIGN KEY (owner_id) REFERENCES Users(uid)
);

CREATE TABLE Groups_Users (
    uid INTEGER,
    gid INTEGER,
    display_name VARCHAR(64) NOT NULL,
    avatar CHAR(64),
    PRIMARY KEY (uid, gid),
    FOREIGN KEY (uid) REFERENCES Users(uid),
    FOREIGN KEY (gid) REFERENCES Groups(gid)
);

/* when confused return to this https://stackoverflow.com/questions/2366854/can-table-columns-with-a-foreign-key-be-null */
CREATE TABLE Images (
    hash CHAR(64),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (hash)
);


/* TODO make it so a blank message is possible with an image. triggers? SIGNAL!  http://www.mysqltutorial.org/mysql-check-constraint/*/
CREATE TABLE Messages (
    mid INTEGER AUTO_INCREMENT,
    uid INTEGER NOT NULL,
    gid INTEGER NOT NULL,
    sent_display_name VARCHAR(64),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    content TEXT NOT NULL,
    img_hash VARCHAR(64),
    PRIMARY KEY (MID),
    FOREIGN KEY (img_hash) REFERENCES Images(hash)
);


