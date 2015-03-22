DELETE u1
FROM update_log u1, update_log u2
WHERE u1.id > u2.id AND u1.price = u2.price;

ALTER TABLE update_log
CHANGE price price INT(11) NOT NULL DEFAULT '0' UNIQUE;