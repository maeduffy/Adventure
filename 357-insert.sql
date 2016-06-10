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
(1, 'fork', 'you have obtained a fork.'),
(2, 'pipe', 'you have obtained a pipe.'),
(3, 'maple syrup', 'you have obtained maple syrup'),
(4, 'alien', 'you have been obtained by an alein. I wonder where he is from'),
(5, 'deck of cards', 'you have obtained a deck of cards. Maybe you can play a game'),
(6, 'vaccuum', 'you have obtained a vaccuum. ')
;

INSERT INTO Projects VALUES
(1, 'Martian Poker', 'you have been tasked to create a new card game for your martian friend. '),
(2, 'Linear Sim', 'You have been tasked to use forks and pipes to ...'),
(3, 'LZW', 'You have been tasked to write a compression algorithm to compress your hatred of this class'),
(4, 'Calculon', 'You have been tasked to write a compiler');

INSERT INTO ProjectItems VALUES
(1, 1, 4),
(2, 1, 5),
(3, 2, 1),
(4, 2, 2),
(5, 2, 3),
(6, 3, 6);

INSERT INTO Rooms VALUES
(1, 2, 3, 7, NULL, NULL, 'You have always been good with computers? That is funny. This class will make or break you. After this class, you will no longer be good with computers, you will be a good computer, become one with the machine. In each room, you will have up to 3 choices. You may move to the left, to the right, or backwards. Choose wisely and you will come out victorious, ready for bigger and better (or worse, let\'s be real) things. Good luck!'),
(2, 1, 10, 14, NULL, NULL, ''),
(3, 1, 4, 16, NULL, NULL, ''),
(4, 3, 5, 19, NULL, NULL, ''),
(5, 4, 6, 22, NULL, NULL, ''),
(6, 5, 7, 25, NULL, NULL, 'Wandering around the halls of Pilling, you see the ghosts of students past. "FOOOOOORRRKS", they say. "FOOOOOOORKS". One ghost wanders into the room to the left, and the rest go to the right.'),
(7, 1, 6, 8, 1, NULL, 'You have entered a room made of forks. No, seriously. Forks. Forks on the ceiling. Forks on the walls. No, wait. The walls are literally forks. Their tines poking out into the middle of the room, it is hard not to be impailed.'),
(8, 7, 9, 27, NULL, NULL, ''),
(9, 8, 10, 30, NULL, NULL, ''),
(10, 2, 9, 11, NULL, NULL, ''),
(11, 10, 12, 32, NULL, NULL, ''),
(12, 11, 13, NULL, NULL, NULL, ''),
(13, 12, 14, 33, NULL, NULL, ''),
(14, 2, 13, 15, NULL, NULL, ''),
(15, 14, 16, 35, NULL, 1, 'The room is dark and smokey. Through the dense smoke, you see what appears to be a table. "A table in a dark smokey room?" you mutter to yourself. What am I doing here?'),
(16, 3, 15, 17, NULL, NULL, ''),
(17, 16, 18, 37, 2, NULL, 'It looks as though you have stumbled into the architecture building. The building seems to be inside out, with pipes on the outsides of walls. Who puts pipes outside of walls? Silly architects. Trying to be cool and shit.'),
(18, 17, 19, 40, NULL, NULL, 'After another meeting at 7 am, you drag yourself out of the CSL and head toward Subway for some much deserved food. '),
(19, 4, 18, 20, NULL, NULL, ''),
(20, 19, 21, 42, NULL, NULL, ''),
(21, 20, 22, NULL, NULL, NULL, ''),
(22, 5, 21, 23, NULL, NULL, ''),
(23, 22, 24, NULL, NULL, 2, 'Time for some food! From the other side of the restaurant you hear "forks and knives, forks and knives," just like that one joke from middle school.'),
(24, 23, 25, 43, NULL, NULL, ''),
(25, 6, 24, 26, NULL, NULL, ''),
(26, 25, 27, 45, NULL, 3, ''),
(27, 8, 26, 28, NULL, NULL, ''),
(28, 27, 29, 47, NULL, NULL, ''),
(29, 28, 30, NULL, NULL, NULL, ''),
(30, 9, 29, 31, NULL, NULL, 'First thing in the morning, it is time for a nutritious breakfast. No. Really. Go make yourself some pancakes to keep that big old brain of yours working. '),
(31, 30, 32, NULL, 3, NULL, 'What good are pancakes without maple syrup? Did you know that if you put a straw through a stack of pancakes and pour maple syrup in, it is like how pipes work in C? Interesting'),
(32, 11, 31, NULL, NULL, NULL, ''),
(33, 13, 34, NULL, NULL, NULL, 'You hear loud noises. What could that be? Probably a bunch of non-CS majors actually enjoying their college experience instead of taking this class'),
(34, 33, 35, NULL, 4, NULL, 'ALIENS! Well, I think they are aliens. They don''t have green heads or big eyes but their heads are on backward and they each have a 10 foot long tail. Maybe you should be nice and make friends with one of them. It may prove to be useful to know their customs...'),
(35, 15, 34, 36, NULL, NULL, ''),
(36, 35, 37, NULL, NULL, NULL, ''),
(37, 17, 36, 38, NULL, NULL, ''),
(38, 37, 39, NULL, NULL, NULL, ''),
(39, 38, 40, NULL, NULL, NULL, ''),
(40, 18, 39, 41, NULL, NULL, ''),
(41, 40, 42, NULL, NULL, 4, ''),
(42, 20, 41, NULL, NULL, NULL, ''),
(43, 24, 44, NULL, 5, NULL, 'Another round of late night poker in the security lab.  Peter left his deck of cards. You might want to pick that up...'),
(44, 43, 45, NULL, NULL, NULL, ''),
(45, 26, 44, 46, NULL, NULL, ''),
(46, 45, 47, NULL, 6, NULL, ''),
(47, 46, 28, NULL, NULL, NULL, '');
