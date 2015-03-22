INSERT_DATA = """INSERT INTO update_log (price) VALUES ({values}) ON DUPLICATE KEY UPDATE last_update = NOW();"""
SELECT_DATA = """
SELECT last_update, price
FROM (
  SELECT * FROM update_log GROUP BY price ORDER BY last_update DESC LIMIT {limit}
) sub
ORDER BY last_update ASC;"""