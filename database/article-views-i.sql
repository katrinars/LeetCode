# Write your MySQL query statement below
SELECT author_id as id
From Views
WHERE viewer_id = author_id
GROUP By author_id
ORDER BY author_id ASC;