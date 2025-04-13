SELECT *
FROM MarvelCharacters;

-- SELECT - выбираем данные таблицы
-- FROM - из какой таблицы
-- WHERE - условие
-- GROUP BY - группируем
-- HAVING - условие для групп
-- ORDER BY - сортировка
-- LIMIT - ограничение вывода
-- OFFSET - пропустить
-- LIMIT - ограничение вывода
-- LIKE - похоже на или КАК
-- DISTINCT - выбираем только уникальные значения

SELECT name, EYE, HAIR, SEX, Appearances
FROM MarvelCharacters
WHERE APPEARANCES > 1000
ORDER BY APPPEARANCES DESC;

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald' AND APPEARANCES > 10
ORDER BY APPEARANCES DESC;

SELECT DISTINCT HAIR
FROM MarvelCharacters;

SELECT DISTINCT EYE
FROM MarvelCharacters;

SELECT DISTINCT EYE, HAIR
FROM MarvelCharacters
WHERE EYE IS NOT NULL AND HAIR IS NOT NULL;

-- ПРАКТИКА Добудьте уникальные значения по полу
-- Выберитте интересное вам значение и найдите всех персонажей этим полом

SELECT DISTINCT SEX
FROM MarvelCharacters;

SELECT name, APPEARANCES, year, SEX
FROM MarvelCharacters
WHERE SEX = 'Genderfluid Characters' OR SEX = 'Agender Characters'
ORDER BY APPEARANCES DESC;

SELECT * 
FROM MarvelCharacters
WHERE year IS NOT NULL
ORDER BY year DESC

SELECT *FROM MarvelCharacters
WHERE
    year IS NOT NULL
    AND yaer > 1939
    AND year < 1946;

SELECT * FROM MarvelCharacters
WHERE
    year IS NOT NULL
    AND year IN (1939, 1940, 1941, 1942, 1943, 1944, 1945);


-- ищем злодеев в базе (hitler, stalin, lenin)
-- ищем по цвету волос (Black Hair, White Hair, Red Hair)
-- Попробуйте сделать запрос похожий, но hair in этот кортеж

SELECT * FROM MarvelCharacters
WHERE 
    hair IN ('Black Hair', 'White Hair', 'Red Hair')
    AND APPEARANCES > 10
ORDER BY hair, APPEARANCES DESC;

SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE name LIKE '%Spider%man%'

