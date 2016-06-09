INSERT INTO Scores VALUES
(0, -20),
(100, 50);

INSERT INTO Tests VALUES
(1, 'Midterm 1'),
(2, 'Midterm 2'),
(3, 'Final');

INSERT INTO Health VALUES
(0, "You just died"),
(5, "You are on the verge of death. Better do better"),
(90, "That's alright. You are still doing pretty week"),
(100, "You are killing it. Keep going!");

INSERT INTO Items VALUES
(0, 'nothing', 'nothing'),
(1, 'fork', 'you have obtained a fork.'),
(2, 'pipe', 'you have obtained a pipe.'),
(3, 'maple syrup', 'you have obtained maple syrup'),
(4, 'alien', 'you have been obtained by an alein. I wonder where he is from'),
(5, 'deck of cards', 'you have obtained a deck of cards. Maybe you can play a game'),
(6, 'vaccuum', 'you have obtained a vaccuum. ')
;

INSERT INTO Projects VALUES
(0, 'nothing', 'nothing'),
(1, 'Martian Poker', 'you have been tasked to create a new card game for your martian friend. '),
(2, 'Linear Sim', 'You have been tasked to use forks and pipes to ...'),
(3, 'LZW', 'You have been tasked to write a compression algorithm to compress your hatred of this class'),
(4, 'Calculon', 'You have been tasked to write a compiler');

INSERT INTO ProjectItems VALUES
(0, 0, 0),
(1, 1, 4),
(2, 1, 5),
(3, 2, 1),
(4, 2, 2),
(5, 2, 3),
(6, 3, 6);

INSERT INTO Rooms VALUES
(1, 2, 3, 7, 0, 0, 'You have always been good with computers? That is funny. This class will make or break you. After this class, you will no longer be good with computers, you will be a good computer, become one with the machine. In each room, you will have up to 3 choices. You may move to the left, to the right, or backwards. Choose wisely and you will come out victorious, ready for bigger and better (or worse, let\'s be real) things. Good luck!'),
(2, 1, 10, 14, 0, 0, ''),
(3, 1, 4, 16, 0, 0, ''),
(4, 3, 5, 19, 0, 0, ''),
(5, 4, 6, 22, 0, 0, ''),
(6, 5, 7, 25, 0, 0, 'Wandering around the halls of Pilling, you see the ghosts of students past. "FOOOOOORRRKS", they say. "FOOOOOOORKS". One ghost wanders into the room to the left, and the rest go to the right.'),
(7, 1, 6, 8, 1, 0, 'You have entered a room made of forks. No, seriously. Forks. Forks on the ceiling. Forks on the walls. No, wait. The walls are literally forks. Their tines poking out into the middle of the room, it is hard not to be impailed.'),
(8, 7, 9, 27, 0, 0, ''),
(9, 8, 10, 30, 0, 0, ''),
(10, 2, 9, 11, 0, 0, ''),
(11, 10, 12, 32, 0, 0, ''),
(12, 11, 13, NULL, 0, 0, ''),
(13, 12, 14, 33, 0, 0, ''),
(14, 2, 13, 15, 0, 0, ''),
(15, 14, 16, 35, 0, 1, ''),
(16, 3, 15, 17, 0, 0, ''),
(17, 16, 18, 37, 2, 0, 'It looks as though you have stumbled into the architecture building. The building seems to be inside out, with pipes on the outsides of walls. Who puts pipes outside of walls? Silly architects. Trying to be cool and shit.'),
(18, 17, 19, 40, 0, 0, ''),
(19, 4, 18, 20, 0, 0, ''),
(20, 19, 21, 42, 0, 0, ''),
(21, 20, 22, NULL, 0, 0, ''),
(22, 5, 21, 23, 0, 0, ''),
(23, 22, 24, NULL, 0, 2, ''),
(24, 23, 25, 43, 0, 0, ''),
(25, 6, 24, 26, 0, 0, ''),
(26, 25, 27, 45, 0, 3, ''),
(27, 8, 26, 28, 0, 0, ''),
(28, 27, 29, 47, 0, 0, ''),
(29, 28, 30, NULL, 0, 0, ''),
(30, 9, 29, 31, 0, 0, ''),
(31, 30, 32, NULL, 3, 0, ''),
(32, 11, 31, NULL, 0, 0, ''),
(33, 13, 34, NULL, 0, 0, ''),
(34, 33, 35, NULL, 4, 0, ''),
(35, 15, 34, 36, 0, 0, ''),
(36, 35, 37, NULL, 0, 0, ''),
(37, 17, 36, 38, 0, 0, ''),
(38, 37, 39, NULL, 0, 0, ''),
(39, 38, 40, NULL, 0, 0, ''),
(40, 18, 39, 41, 0, 0, ''),
(41, 40, 42, NULL, 0, 4, ''),
(42, 20, 41, NULL, 0, 0, ''),
(43, 24, 44, NULL, 5, 0, ''),
(44, 43, 45, NULL, 0, 0, ''),
(45, 26, 44, 46, 0, 0, ''),
(46, 45, 47, NULL, 6, 0, ''),
(47, 46, 28, NULL, 0, 0, '');
