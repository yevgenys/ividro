import logging as log
from threading import Thread

from dao.Dao import Dao
from updaters.ividro.PriceReceiver import PriceReceiver


log.basicConfig(level=log.DEBUG)


class Updater(Thread):

    def __init__(self, receiver, dao):
        super(Updater, self).__init__()
        self._receiver = receiver
        self._dao = dao

    def run(self):
        log.debug("run")
        self._update()

    def _update(self):
        log.debug("update")
        current_price = self._receiver.get_current_price()
        log.debug("current_price: " + current_price)
        self._dao.insert(current_price)


if __name__ == '__main__':
    dao = Dao()
    receiver = PriceReceiver()
    updater = Updater(receiver, dao)
    updater.start()
