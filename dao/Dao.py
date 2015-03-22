import MySQLdb
import logging as log
import os

from dao.sql_queries import SELECT_DATA, INSERT_DATA


def connect_db():
    return MySQLdb.connect(os.environ["OPENSHIFT_MYSQL_DB_HOST"],
                           os.environ["OPENSHIFT_MYSQL_DB_USERNAME"],
                           os.environ["OPENSHIFT_MYSQL_DB_PASSWORD"],
                           "boroda",
                           int(os.environ["OPENSHIFT_MYSQL_DB_PORT"]))


def connect_before_function_and_disconnect_after(f):
    def wrapper(self, *args, **kwargs):
        self._connect()
        res = f(self, *args, **kwargs)
        self._close_connection()
        return res
    return wrapper


class Dao(object):
    def __init__(self):
        self._con = None
        self._cursor = None

    def get(self, limit=10):
        log.debug("get limit: %s" % limit)
        return self._execute_get(limit)

    def insert(self, current_price):
        log.debug("inserting: " + current_price)
        self._execute_insert(current_price)

    @connect_before_function_and_disconnect_after
    def _execute_get(self, limit):
        self._execute(SELECT_DATA.format(limit=limit))
        res = self._get_data_after_execute()
        log.debug("res: " + str(res))
        return res

    @connect_before_function_and_disconnect_after
    def _execute_insert(self, data):
        self._execute(INSERT_DATA.format(values=data))
        self._commit()

    def _commit(self):
        self._con.commit()

    def _get_data_after_execute(self):
        return self._cursor.fetchall()

    def _close_connection(self):
        self._con.close()
        self._con = None
        self._cursor = None

    def _execute(self, sql):
        self._cursor.execute(sql)

    def _connect(self):
        self._con = connect_db()
        self._cursor = self._con.cursor()
