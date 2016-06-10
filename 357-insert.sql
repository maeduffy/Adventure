INSERT INTO Scores VALUES
(0, -50),
(10,-40),
(20,-30),
(30,-20),
(40,-10),
(50,0),
(60,10),
(70,20),
(80,30),
(90,40),
(100, 50);

INSERT INTO Tests VALUES
(1, 'Midterm 1'),
(2, 'Midterm 2'),
(3, 'Final');

INSERT INTO Questions VALUES 
(1, 1, 1, 'char* phrase = "I Love 357"; char* letter = char + 2; What is the value of letter[3]?', 'e'),
(2, 1, 2, 'Complete this sentence by Staley: "Coming back from a..."', 'pause'),
(3, 1, 3, 'How do you list all the files in your current directory?', 'ls'),
(4, 1, 4, 'What is 0x22 in binary?', '00100010'),
(5, 1, 5, 'What is 35 >> 1', '17'),
(6, 2, 1, 'What is Staley''s favorite theme of shirt?', 'hawaiian'),
(7, 2, 2, 'Who has both TAed for and taught 357?', 'Andrew Wang'),
(8, 2, 3, 'What language should you be very familiar with?', 'C'),
(9, 2, 4, 'How many bytes are in a char?', '1'),
(10, 2, 5, 'What is the name of the system call that can be used to create another process or can be used as a kitchen utensil?', 'fork'),
(11, 3, 1, 'What is 20 & 15', '4'),
(12, 3, 2, 'What should now be your favorite text editor?', 'vim'),
(13, 3, 3, 'How many bits are in a short?', '16'),
(14, 3, 4, 'What spooky name is given to a child whose parent exits without waiting for it?', 'zombie'),
(15, 3, 5, 'On a scale of 1-10, how much stress do you feel?', '10'),
(16, 3, 6, '0 is FALSE and 1 is true right?', '1');


INSERT INTO Health VALUES
(0, 'You just died'),
(10, 'You are on the verge of death. Better do better'),
(50, 'You better be careful, you are already at half life!'),
(90, 'That''s alright. You are still doing pretty well'),
(100, 'You are killing it. Keep going!');


INSERT INTO Items VALUES
(1, 'fork', 'You have obtained a fork.'),
(2, 'pipe', 'You have obtained a pipe.'),
(3, 'maple syrup', 'You have obtained maple syrup.'),
(4, 'alien', 'You have been obtained by an alien.'),
(5, 'deck of cards', 'You have obtained a deck of cards.'),
(6, 'vacuum', 'You have obtained a vacuum. '),
(7, 'bender', 'You have obtained bender.'),
(8, 'shell', 'You have obtained a shell');

INSERT INTO Projects VALUES
(1, 'Martian Poker', 'You have been tasked to create a new card game for your martian friend. '),
(2, 'Linear Sim', 'But you don''t need forks and knives for this project. You need forks and pipes in order to model computational fluid dynamics. Good luck with that.'),
(3, 'LZW', 'You have been tasked to write a compression algorithm to compress your hatred of this class.'),
(4, 'Calculon', 'You have been tasked to write an automated testing system to mimic Bender.');

INSERT INTO ProjectItems VALUES
(1, 1, 4),
(2, 1, 5),
(3, 2, 1),
(4, 2, 2),
(5, 2, 3),
(6, 3, 6),
(7, 4, 7),
(8, 4, 8);

INSERT INTO Rooms VALUES
(1, 2, 3, 7, NULL, NULL, 'You have always been good with computers? That is funny. This class will make or break you. After this class, you will no longer be good with computers, you will be a good computer, become one with the machine. In each room, you will have up to 3 choices. You may move to the left, to the right, or backwards. Choose wisely and you will come out victorious, ready for bigger and better (or worse, let’'s be real) things. Good luck!'),
(2, 1, 10, 14, 7, NULL, 'Suddenly you are teleported to a new planet and land on a piece of metal. As you walk off the sheet of metal you hear a grunt from below you, "Bite my shiny metal ass!" You realize that you found BENDER!!!'),
(3, 1, 4, 16, NULL, NULL, 'YOU CAN DO IT!'),
(4, 3, 5, 19, NULL, NULL, 'Real programmers count from 0'),
(5, 4, 6, 22, NULL, NULL, 'Don''t fork this up.'),
(6, 5, 7, 25, NULL, NULL, 'Wandering around the halls of Pilling, you see the ghosts of students past. "FOOOOOORRRKS", they say. "FOOOOOOORKS". One ghost wanders into the room to the left, and the rest go to the right.'),
(7, 1, 6, 8, 1, NULL, 'You have entered a room made of forks. No, seriously. Forks. Forks on the ceiling. Forks on the walls. No, wait. The walls are literally forks. Their tines poking out into the middle of the room, it is hard not to be impaled.'),
(8, 7, 9, 27, NULL, NULL, 'Another day in the life of a 357 student. Here''s hoping you make it through the day'),
(9, 8, 10, 30, NULL, NULL, 'Maybe you can go to the P today... Wait. Nope, you are still taking this class.'),
(10, 2, 9, 11, NULL, NULL, 'Hey. If you fail, you can always retake it. Except it will be a completely different class'),
(11, 10, 12, 32, NULL, NULL, 'Do you feel the pain? This is why we get hired by Apple'),
(12, 11, 13, NULL, NULL, NULL, 'Just 125-135 hours of studying this week!'),
(13, 12, 14, 33, NULL, NULL, '"Vim is better!" "No! Nano is better" Better put your head down and walk away while you still can.'),
(14, 2, 13, 15, NULL, NULL, '"This way or that?" you ask. I will give you some pointers.'),
(15, 14, 16, 35, NULL, 1, 'The room is dark and smokey. Through the dense smoke, you see what appears to be a table. "A table in a dark smoky room?" you mutter to yourself. What am I doing here?'),
(16, 3, 15, 17, NULL, NULL, 'Sometimes, you just need to pass out on Dexter for a couple of hours'),
(17, 16, 18, 37, 2, NULL, 'It looks as though you have stumbled into the architecture building. The building seems to be inside out, with pipes on the outsides of walls. Who puts pipes outside of walls? Silly architects. Trying to be cool and shit.'),
(18, 17, 19, 40, NULL, NULL, 'After another meeting at 7 am, you drag yourself out of the CSL and head toward Subway for some much deserved food. '),
(19, 4, 18, 20, NULL, NULL, 'Time for a break! You are headed down the 101 South. If you turn off now, you might be able to hit Avila Beach for a little bit.'),
(20, 19, 21, 42, 8, NULL, 'She sells sea shells by the sea shore. Oh look! A sea shell.'),
(21, 20, 22, NULL, NULL, NULL, 'On the road again, I just can''t wait to be out on the road again'),
(22, 5, 21, 23, NULL, NULL, 'It''s not as easy as 123, it''s as hard as finding a pop culture reference for 357'),
(23, 22, 24, NULL, NULL, 2, 'Time for some food! From the other side of the restaurant you hear "forks and knives, forks and knives," just like that one joke from middle school.'),
(24, 23, 25, 43, NULL, NULL, 'Don''t worry about getting classes next quarter on PASS, you probably won'' pass this class anyway.'),
(25, 6, 24, 26, NULL, NULL, 'My heart beats SLO -wer and the slower the further into this all-nighter I get.'),
(26, 25, 27, 45, NULL, 3, 'Mom always warned you to pick up a vacuum at Target but there never seemed to be a good reason for it until now, when you have to cram a lot of stuff in a little space. '),
(27, 8, 26, 28, NULL, NULL, 'It''s time for some Engi-beer-ing'),
(28, 27, 29, 47, NULL, NULL, 'You get to the tutoring center 30 minutes before it starts and are already the 20th person on the waitlist. So, no; no help for you today.'),
(29, 28, 30, NULL, NULL, NULL, 'A foo walks into a bar, looks around, and says "hello, world"'),
(30, 9, 29, 31, NULL, NULL, 'First thing in the morning, it is time for a nutritious breakfast. No. Really. Go make yourself some pancakes to keep that big old brain of yours working. '),
(31, 30, 32, NULL, 3, NULL, 'What good are pancakes without maple syrup? Did you know that if you put a straw through a stack of pancakes and pour maple syrup in, it is like how pipes work in C? Interesting'),
(32, 11, 31, NULL, NULL, NULL, 'That moment when you have more private messages to the TAs than there are public messages period on PIAZZA.'),
(33, 13, 34, NULL, NULL, NULL, 'You hear loud noises. What could that be? Probably a bunch of non-CS majors actually enjoying their college experience instead of taking this class'),
(34, 33, 35, NULL, 4, NULL, 'ALIENS! Well, I think they are aliens. They don''t have green heads or big eyes but their heads are on backward and they each have a 10 foot long tail. Maybe you should be nice and make friends with one of them. It may prove to be useful to know their customs...'),
(35, 15, 34, 36, NULL, NULL, 'Mammen, you spicy asshole.'),
(36, 35, 37, NULL, NULL, NULL, 'Are you a programmer yet? Can you turn coffee and monster into code?'),
(37, 17, 36, 38, NULL, NULL, 'Just cry. You know you want to. All the cool kids are doing it these days.'),
(38, 37, 39, NULL, NULL, NULL, 'After some point, they stop being all nighters and become all day-ers'),
(39, 38, 40, NULL, NULL, NULL, 'No coding today, the Bachelor is on'),
(40, 18, 39, 41, NULL, NULL, 'After a long Pause... it is time to get back to work.'),
(41, 40, 42, NULL, NULL, 4, 'We have been enjoying the wonder that is Bender all quarter, now it is time to make him for yourself. '),
(42, 20, 41, NULL, NULL, NULL, 'Is it time for pizza? Chicken and white sauce?'),
(43, 24, 44, NULL, 5, NULL, 'Another round of late night poker in the security lab.  Peter left his deck of cards. You might want to pick that up...'),
(44, 43, 45, NULL, NULL, NULL, 'There is someone sobbing in the corner. We could go help them but that might be breaking non-colab'),
(45, 26, 44, 46, NULL, NULL, 'I hate my life'),
(46, 45, 47, NULL, 6, NULL, 'Vroom Vroom motherfucker!'),
(47, 46, 28, NULL, NULL, NULL, 'Just remember, after this, it only goes downhill. Except 365 ;)');
