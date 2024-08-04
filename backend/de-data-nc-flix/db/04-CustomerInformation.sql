\c nc_flix

SELECT *,
CASE
    WHEN loyalty_points = 0 THEN 'doesnt even go here'
    WHEN loyalty_points < 10 THEN 'bronze status'
    WHEN loyalty_points < 99 THEN 'silver status'
    ELSE 'gold status'
END AS loyalty_membership_status
FROM customers
ORDER BY location, loyalty_points DESC
;

