import re

import requests


pricePattern = re.compile('.*?<span\sclass="price"\sitemprop="price">\s?(\d*)\s?<i>.*</i>', re.MULTILINE)


class ValidationException(Exception): pass


class PriceReceiver(object):
    _uri = "http://stylus.com.ua/ru/products/details/185692/index.html"

    def get_current_price(self):
        resp = self._do_get_req()
        self._validate_http_ok(resp)
        return self._parse_response_and_get_current_price(resp)

    def _do_get_req(self):
        return requests.get(self._uri)

    def _validate_http_ok(self, resp):
        if resp.status_code != 200:
            raise ValidationException("Not HTTP 200 OK code received")

    def _parse_response_and_get_current_price(self, resp):
        return pricePattern.search(resp.text).group(1)


if __name__ == '__main__':
    pr = PriceReceiver()
    print pr.get_current_price()