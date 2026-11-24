-- Q 620 - https://leetcode.com/problems/not-boring-movies/
SELECT 
    * 
FROM Cinema 
WHERE id % 2 != 0 AND description != 'boring'
ORDER BY rating DESC;

-- Q 1757 - https://leetcode.com/problems/recyclable-and-low-fat-products/
SELECT product_id FROM Products WHERE low_fats ='Y' AND recyclable = 'Y';

--Q 595 - https://leetcode.com/problems/big-countries/
SELECT name,area, population FROM World WHERE area >= 3000000 OR population >= 25000000;