import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_varastoon1(self):
        # muutos
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    def test_lisaa_varastoon2(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
    def test_lisaa_varastoon3(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ota_varastosta1(self):
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    def test_ota_varastosta2(self):
        saatu_maara = self.varasto.ota_varastosta(12)
        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_init1(self):
        varasto1 = Varasto(-1, alku_saldo=-1)
        self.assertAlmostEqual(varasto1.saldo, 0.0)
        self.assertAlmostEqual(varasto1.tilavuus, 0.0)

    def test_init2(self):
        varasto1 = Varasto(10, alku_saldo=8)
        self.assertAlmostEqual(varasto1.saldo, 8)
        self.assertAlmostEqual(varasto1.tilavuus, 10)

    def test_init3(self):
        varasto1 = Varasto(10, alku_saldo=12)
        self.assertAlmostEqual(varasto1.saldo, 10)
        self.assertAlmostEqual(varasto1.tilavuus, 10)

    def test_str(self):
        varasto1 = Varasto(10, alku_saldo=1)
        str = varasto1.__str__()
        print(str)
        self.assertTrue(str == "saldo = 1, vielä tilaa 9")