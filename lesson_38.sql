-- Lesson 38 - Создание собственной системы таблиц 
-- Students - Таблица студентов
-- Groups - Таблица групп
-- Teachers - Таблица преподавателей
-- TeacherGroups - Таблица групп преподавателей
-- StudentsCards - Таблица студенческих карточек

-- Students создать если не существует

CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER DEFAULT 0,
    group_name TEXT NOT NULL
);


-- 2. Добавляем одного студента в БД
INSERT INTO Students (first_name, last_name, group_name)
VALUES ('Филлип', 'Киркоров', 'python411');

INSERT INTO Students (first_name, middle_name, last_name, age, group_name)
-- 3. Перечисляем пять студентов в группу
VALUES 
('Светозара', 'Питоновна', 'Джангова', 20, 'python412'),
('Кодислав', 'Гитович', 'Коммитов', 21, 'python412'),
('Серверина', 'Базоданных', 'Селектова', 22, 'python412'),
('Фронтендий', 'Вебович', 'Реактов', 23, 'python412'),
('Линуксина', 'Убунтовна', 'Баширова', 24, 'python412'),

-- 4. Еще 5 студнтов в 413
('Алгоритм', 'Сортирович', 'Рекурсионов', 20, 'python413'),
('Нейросеть', 'Вижновна', 'Трансформерова', 20, 'python413'),
('Блокчейн', 'Криптович', 'Токенов', 20, 'python413'),
('Явана', 'Скриптовна', 'Ноутация', 20, 'python413'),
('Облакос', 'Докерович', 'Кубернетов', 20, 'python413');

-- 5. Удалим лишнего студента
DELETE FROM Students
WHERE id = 2;

DELETE FROM Students 
WHERE ID = (SELECT id
            FROM Students
            WHERE first_name = 'Филлип'
            AND last_name = 'Киркоров'
            AND group_name ='python411'
            LIMIT 1);

-- 6. Можно удалить двух студентов по айди
-- DELETE FROM Students 
-- WHERE id IN (23, 2)

-- 6. Обновим данные студента 1
UPDATE Students 
SET middle_name = 'Бедровсович', age = 45 
WHERE id = 1;


-- Светозара Питоновна Джангова - девушка, которая обожает Python и фреймворк Django.
-- Кодислав Гитович Коммитов - студент, который всегда держит свой код в идеальном порядке с помощью Git.
-- Серверина Базоданных Селектова - молодая девушка с удивительными навыками в SQL-запросах.
-- Фронтендий Вебович Реактов - парень, который предпочитает работать с интерфейсами и React.
-- Линуксина Убунтовна Баширова - студентка, влюбленная в операционные системы на базе Linux и Bash-скрипты.
-- Алгоритм Сортирович Рекурсионов - талантливый студент, который может оптимизировать любой код.
-- Нейросеть Вижновна Трансформерова - дама, увлечённая искусственным интеллектом и компьютерным зрением.
-- Блокчейн Криптович Токенов - студент, который постоянно рассказывает о перспективах децентрализованных систем.
-- Явана Скриптовна Ноутация - девушка, одинаково хорошо владеющая и Java, и JavaScript.
-- Облакос Докерович Кубернетов - молодой человек, фанатеющий от облачных технологий и контейнеризации.

-- 7. Cоздание таблица Groups
CREATE TABLE IF NOT EXISTS Groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL UNIQUE,
    start_date DATE DEFAULT CURRENT_TIMESTAMP,
    end_date DATE
);


-- 8. Добавляем группы в БД
INSERT INTO Groups (group_name)
VALUES
('python411'),
('python412'),
('python413');