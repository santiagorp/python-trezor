import common
import unittest

from trezorlib.tx_api import TxApiBitcoin, TxApiTestnet


class TestTxApi(unittest.TestCase):

    def test_get(self):
        tx = TxApiBitcoin.get_tx('39a29e954977662ab3879c66fb251ef753e0912223a83d1dcb009111d28265e5')
        tx = TxApiBitcoin.get_tx('54aa5680dea781f45ebb536e53dffc526d68c0eb5c00547e323b2c32382dfba3')
        tx = TxApiBitcoin.get_tx('58497a7757224d1ff1941488d23087071103e5bf855f4c1c44e5c8d9d82ca46e')
        tx = TxApiBitcoin.get_tx('6189e3febb5a21cee8b725aa1ef04ffce7e609448446d3a8d6f483c634ef5315')
        tx = TxApiBitcoin.get_tx('a6e2829d089cee47e481b1a753a53081b40738cc87e38f1d9b23ab57d9ad4396')
        tx = TxApiBitcoin.get_tx('c6091adf4c0c23982a35899a6e58ae11e703eacd7954f588ed4b9cdefc4dba52')
        tx = TxApiBitcoin.get_tx('c63e24ed820c5851b60c54613fbc4bcb37df6cd49b4c96143e99580a472f79fb')
        tx = TxApiBitcoin.get_tx('c6be22d34946593bcad1d2b013e12f74159e69574ffea21581dad115572e031c')
        tx = TxApiBitcoin.get_tx('d1d08ea63255af4ad16b098e9885a252632086fa6be53301521d05253ce8a73d')
        tx = TxApiBitcoin.get_tx('d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882')
        tx = TxApiBitcoin.get_tx('e4bc1ae5e5007a08f2b3926fe11c66612e8f73c6b00c69c7027213b84d259be3')

        tx = TxApiTestnet.get_tx('6f90f3c7cbec2258b0971056ef3fe34128dbde30daa9c0639a898f9977299d54')
        tx = TxApiTestnet.get_tx('d6da21677d7cca5f42fbc7631d062c9ae918a0254f7c6c22de8e8cb7fd5b8236')


if __name__ == '__main__':
    unittest.main()
