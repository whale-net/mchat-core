/* sha512$3ae2fd1b23c0404487df8bc1ec97f7d1$82dd508a6b4541e33da7e0b3a381c85211935bbfaf68e4289d9e99dda3871c545e5d76d2c78b6215c07ee259ef79b0aefb5da9f5880582c5cd15618a8f66a289
   this above string is db string for 'password' */
INSERT INTO Users(username, global_display_name, password)
VALUES ('alex', 'alex_the_king', 'sha512$3ae2fd1b23c0404487df8bc1ec97f7d1$82dd508a6b4541e33da7e0b3a381c85211935bbfaf68e4289d9e99dda3871c545e5d76d2c78b6215c07ee259ef79b0aefb5da9f5880582c5cd15618a8f66a289'),
('koni', 'koni_the_queen', 'sha512$3ae2fd1b23c0404487df8bc1ec97f7d1$82dd508a6b4541e33da7e0b3a381c85211935bbfaf68e4289d9e99dda3871c545e5d76d2c78b6215c07ee259ef79b0aefb5da9f5880582c5cd15618a8f66a289'),
('joebigs', 'joebigs_the_god', 'sha512$3ae2fd1b23c0404487df8bc1ec97f7d1$82dd508a6b4541e33da7e0b3a381c85211935bbfaf68e4289d9e99dda3871c545e5d76d2c78b6215c07ee259ef79b0aefb5da9f5880582c5cd15618a8f66a289');

INSERT INTO Groups(creator_id, owner_id, name)
VALUES (1, 1, 'm-chat the group'),
(2, 3, 'alex is dumb');

INSERT INTO Groups_Users(uid, gid, display_name)
VALUES (1, 1, 'alex'),
(2, 1, 'koni'),
(3, 1, 'bigs'),
(2, 2, 'koni hates alex'),
(3, 2, 'bigs hates alex');

