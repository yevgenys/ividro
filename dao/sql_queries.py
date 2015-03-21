INSERT_DATA = """INSERT INTO update_log (price) VALUES ({VALUES});"""
SELECT_DATA = """
SELECT last_update, price
FROM (
  SELECT * FROM update_log GROUP BY price ORDER BY last_update DESC LIMIT {LIMIT}
) sub
ORDER BY last_update ASC;"""
DELETE_DUPLICATED_ROWS = """
    DELETE u1
    FROM update_log u1, update_log u2
      WHERE u1.id > u2.id AND u1.price = u2.price;"""