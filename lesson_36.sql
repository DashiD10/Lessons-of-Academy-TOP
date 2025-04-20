SELECT DISTINCT HAIR
FROM MarvelCharacters;

SELECT HAIR
FROM MarvelCharacters
GROUP BY HAIR; 

SELECT COUNT(*)
FROM MarvelCharacters;

SELECT COUNT(DISTINCT HAIR)
FROM MarvelCharacters;

SELECT HAIR, COUNT(HAIR)
FROM MarvelCharacters
WHERE HAIR = 'Bald';

SELECT HAIR, COUNT(*) AS hair_count
FROM MarvelCharacters
WHERE HAIR IS NOT NULL
GROUP BY HAIR
ORDER BY hair_count DESC;

SELECT EYE, COUNT(*) AS eye_count
FROM MarvelCharacters
WHERE EYE IS NOT NULL
GROUP BY EYE
ORDER BY eye_count DESC;

--SUM - сумма значений в столбце

SELECT EYE, COUNT(*) AS eye_count, SUM(APPEARANCES) AS total_appearances
FROM MarvelCharacters
WHERE EYE IS NOT NULL
GROUP BY EYE
ORDER BY total_appearances DESC;

SELECT year, COUNT(*) AS year_count, MAX(APPEARANCES) AS max_appearances, AVG(APPEARANCES) AS avg_appearances, SUM(APPEARANCES) AS total_appearances
FROM MarvelCharacters
GROUP BY year;

-- TODO - Сделайте группировку по identify - Посчитайте количество персонажей в каждом году
-- TODO - Сделайте группировку по Alive - Посчитайте количество персонажей, сделайте сорировку по количеству персонажей

-- ПОДЗАПРОСЫ



SELECT
    Year,
    COUNT(*) AS num_characters,
    SUM(APPEARANCES) AS total_appearances,
    MAX(APPEARANCES) AS max_appearances,
    ROUND(AVG(APPEARANCES), 2) AS avg_appearances;



WITH AverageAppearances AS (
    SELECT AVG(APPEARANCES) AS avg_appearances
    bFROM MarvelCharacters
)

SELECT name, APPEARANCES
FROM MarvelCharacters, AverageAppearances
WHERE APPEARANCES > avg_appearances
ORDER BY APPEARANCES DESC;


SELECT name, eye_id
FROM MarvelCharacters;

SELECT eye_id, color
FROM EyeColor
WHERE eye_id = 1;

SELECT name, color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id;


