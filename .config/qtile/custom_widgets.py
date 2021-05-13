import locale

from libqtile.widget import base
from libqtile.widget.generic_poll_text import GenPollUrl

_DEFAULT_CURRENCY = str(locale.localeconv()['int_curr_symbol'])


class BitcoinTicker(GenPollUrl):
    """
    A bitcoin ticker widget, data provided by the coinbase.com API. Defaults to
    displaying currency in whatever the current locale is. Examples::

        # display the average price of bitcoin in local currency
        widget.BitcoinTicker()

        # display it in Euros:
        widget.BitcoinTicker(currency="EUR")
    """

    QUERY_URL = "https://api.coinbase.com/v2/prices/spot?currency=%s"

    orientations = base.ORIENTATION_HORIZONTAL

    defaults = [
        ('currency', _DEFAULT_CURRENCY.strip(),
         'The currency the value that bitcoin is displayed in'),
    ]

    def __init__(self, **config):
        GenPollUrl.__init__(self, **config)
        self.add_defaults(BitcoinTicker.defaults)

        # set up USD as the default if no locale is set
        if self.currency == "":
            locale.setlocale(locale.LC_MONETARY, "en_US.UTF-8")
            self.currency = locale.localeconv()['int_curr_symbol'].strip()
        self.symbol = locale.localeconv()['currency_symbol']

    @property
    def url(self):
        return self.QUERY_URL % self.currency.lower()

    def parse(self, body):
        HOLDINGS = 0.0013108
        PRICE_PER_BTC = float(body['data']['amount'])
        return " | {symbol}{amount:,} | Wallet: {symbol}{holdings:,}".format(symbol=self.symbol,
                                                                                 amount=PRICE_PER_BTC, holdings=round(
                HOLDINGS * PRICE_PER_BTC, 2))


class EthereumTicker(GenPollUrl):
    """
    A bitcoin ticker widget, data provided by the coinbase.com API. Defaults to
    displaying currency in whatever the current locale is. Examples::

        # display the average price of bitcoin in local currency
        widget.BitcoinTicker()

        # display it in Euros:
        widget.BitcoinTicker(currency="EUR")
    """

    QUERY_URL = "https://api.coinbase.com/v2/prices/ETH-USD/buy"

    orientations = base.ORIENTATION_HORIZONTAL

    defaults = [
        ('currency', _DEFAULT_CURRENCY.strip(),
         'The currency the value that ethereum is displayed in'),
    ]

    def __init__(self, **config):
        GenPollUrl.__init__(self, **config)
        self.add_defaults(EthereumTicker.defaults)

        # set up USD as the default if no locale is set
        if self.currency == "":
            locale.setlocale(locale.LC_MONETARY, "en_US.UTF-8")
            self.currency = locale.localeconv()['int_curr_symbol'].strip()
        self.symbol = locale.localeconv()['currency_symbol']

    @property
    def url(self):
        return self.QUERY_URL

    # f'{value:,}'  # For Python ≥3.6
    def parse(self, body):
        HOLDINGS = 0.003931
        PRICE_PER_ETH = float(body['data']['amount'])
        return "ETH | {symbol}{amount:,} | Wallet: {symbol}{holdings:,}".format(symbol=self.symbol,
                                                                                 amount=PRICE_PER_ETH, holdings=round(
                HOLDINGS * PRICE_PER_ETH, 2))
