insert into words(letter_id, word_english, word_hausa, hausa_description, english_description) values
(1, 'prayer', 'aduwa', 'zan yi aduwa yanzu', 'i want to pray now'),
(2, 'father', 'baba', 'ina baba sun?', 'where is their father?'),
(3, 'spoon', 'cokali', 'kawo wancan cokali', 'bring me that spoon'),
(4, 'thousand', 'dubu', 'mallam isa ya kawo dubu goma', 'Mr Isa brought ten thousand'),
(6, 'face', 'fuska', 'salamatu ta wanke fuska ta', 'Salamatu washed her face'),
(16, 'water', 'ruwa', 'mama ta bani ruwa', 'Mother gave me water'),
(20, 'fire', 'wuta', 'kashe mun wuta', 'quench the fire for me'),
(16, 'sun', 'rana', 'rana ya fita' ,'the sun has risen'),
(18, 'bird', 'tsuntsu', 'mai gona ya kama tsuntsu', 'the farmer caught a bird'),
(7, 'finish', 'gama', 'mama na ta gama giriki', 'my mother has finished cooking'),
(8, 'light', 'haske', 'gidan na de haske', 'the house has light'),
(9, 'engineer', 'injiniya', 'injiniya ya yi aikin ma caw', 'the engineer did a good job'),
(10, 'baby', 'jiriri', 'wani jiriri na cuca', 'certain baby is crying'),
(11, 'market', 'kasuwa', 'yaron ya je kasuwa', 'the boy went to the market'),
(12, 'story', 'labari', 'a na labari a kan radio', 'they are telling stories on the radio'),
(13, 'school', 'makaranta', 'lami ta je makaranta', 'Lami went to school'),
(14, 'victory', 'nasara', 'Nigeria ta samu nasara', 'Nigeria has gotten victory'),
(15, 'i see!', 'oho', 'oho isa sai zo gobe', 'I see Isa will come tomorrow'),
(17, 'secretary', 'sakatare', 'wancan mata na nima sekatare', 'that woman is looking for the secretary'),
(18, 'turkey', 'talotalo', 'mun ci talotalo jiya', 'we ate turkey yesterday'),
(19, 'fan', 'vat', 'kunnan mu vat', 'turn on the fan'),
(20, 'trouser', 'wando', 'zan sai wando', 'i want to buy trouser'),
(21, 'elder brother', 'yaya', 'yaya na ya dawo daga america', 'my elder brother is back from America'),
(22, 'lion', 'zaki', 'mai gona ya kashe zaki yau', 'the farmer killed a lion today.');



--select word_hausa, word_english, word_description from main.words inner join main.letters on letters.letter_id = words.letter_id
CREATE TABLE words(
  word_id integer primary key autoincrement,
  letter_id integer(2),
  word_english varchar(50),
  word_hausa varchar(50),
  hausa_description varchar(500),
  english_description varchar(500),
  image_name varchar(50) default '\resources\images\blank.png',
  foreign key(letter_id) references letters(letter_id)
  )