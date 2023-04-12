create table bot_user (
    telegram_id bigint primary key,
    created_at timestamp default current_timestamp
);

create table book_category (
    id integer primary key,
    created_at timestamp default current_timestamp,
    name varchar(60) not null,
    ordering integer not null
);

create table book (
    id integer primary key,
    created_at timestamp default current_timestamp,
    name text,
    category_id integer,
    ordering integer not null,
    read_start timestamp,
    read_finish timestamp,
    foreign key(category_id) references book_category(id)
);

--СТАТУСЫ КНИГ
--1. не прочитана 
--2. будет читаться следующей
--3. читается сейчас

create table voting (
    id integer primary key,
    voting_start timestamp not null, 
    voting_finish timestamp not null
);

create table vote (
    id integer primary key,
    vote_id integer,
    user_id integer,
    first_book integer,
    second_book integer,
    third_book integer,
    foreign key(vote_id) references voting(id),
    foreign key(user_id) references bot_user(telegram_id),
    foreign key(first_book) references book(id),
    foreign key(second_book) references book(id),
    foreign key(third_book) references book(id)
);

insert into book_category (name, ordering) values 
    ('Python', 10),
    ('Алгоритмы', 20),
    ('Тестирование', 30),
    ('Django', 40),
    ('DRF', 50), 
    ('Data Since', 60),
    ('Machine Learning', 70),   
    ('Hacking', 80),
    ('Паттерны проектирования', 90), 
    ('Other interesting', 100), 
    ('Асинхронное программирование', 110);



insert into book (name, ordering, category_id) values
    ('Начинаем программировать на Python :: Тонни Гэддис', 1, 10),
    ('Python исчерпывающее руководство :: Дэвид Бизли', 2, 10),
    ('Python к вершинам мастерства 2 :: Лусиану Рамальо', 3, 10),
    ('Изучаем Python :: Эрие Мэтиз', 4, 10),


    ('Грокаем алгоритмы :: Адитья Бхаргава', 1, 20),

    ('Python. Разработка на основе тестирования :: Гари Персиваль', 1, 30),

    ('Django 3.0 Практика создания веб-сайтов :: Владимир Дронов', 1, 40),

    ('Основы Data Since :: Дэви Силен, Арно Мейсман, Мохамед Али', 1, 60),

    ('Python для сложных задач :: Дж. Вандер Плас', 1, 70),

    ('Python глазами хакера :: Журналл Хаккер', 1, 80),

    ('Банда 4-х :: Э.Гамма, Р.Хелм, Р.Джонсон, Дж. Влиссидес', 1, 90),

    ('Глубокое обучение :: Я.Гудфеллоу, И.Бенджио, А.Курвилль', 1, 100),

    ('Асинхронное программирование :: Мэттью Фаулер', 1, 110);
