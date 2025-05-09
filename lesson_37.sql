SELECT name, eye_id
FROM MarvelCharacters;

SELECT name, color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id;

SELECT MarvelCharacters.name, EyeColor.color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id;

SELECT mc.name, ec.color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;

SELECT mc.name AS character_name, ec.color AS eye_color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;

SELECT mc.id AS character_id, mc.name AS character_name, mc.eye_id AS mc_eye_id, ec.eye_id AS eye_id, ec.color AS eye_color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;

-- TODO - Сделайте запрос JOIN для получения персонажей с их цветом волос и цветом глаз
-- Вам надо сделать 2 JOIN и явно указать названия таблиц и столбцов

-- SELECT mc.id AS characters_id, characters.name, hair_colors.color AS hair_color, eye_colors.color AS eye_color
-- FROM MarvelCharacters AS mc
-- JOIN hair_colors ON characters.hair_color_id = hair_colors.id
-- JOIN eye_colors ON characters.eye_color_id = eye_colors.id;

SELECT hc.color AS hair_color, ec.color AS eye_color, COUNT(*) AS num_characters
FROM MarvelCharacters AS mc
JOIN HairColor AS hc ON mc.hair_id = hc.hair_id
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id
WHERE mc.APPEARANCES > 50
GROUP BY hc.color, ec.color
HAVING num_characters > 10
ORDER BY num_characters DESC;

SELECT s.name AS sex_name, i.identity AS char_identity, a.name AS char_aligment, COUNT(*) AS num_characters
FROM MarvelCharacters AS mc
JOIN sex AS s ON mc.sex_id = s.sex_id
JOIN Identity AS i ON mc.identity_id = i.identity_id
JOIN Alignment AS a ON mc.align_id = a.align_id
WHERE mc.APPEARANCES > 10
GROUP BY sex_name, char_identity, char_aligment
HAVING num_characters > 1
ORDER BY num_characters DESC;







