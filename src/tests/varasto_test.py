import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastolla_virheellinen_tilavuus(self):
        self.varasto = Varasto(-1, 10)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_virheellinen_alkusaldo(self):
        self.varasto = Varasto(10, -2)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_oikea_alkusaldo(self):
        self.varasto = Varasto(10, 5)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_liian_suuri_alkusaldo(self):
        self.varasto = Varasto(10, 15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_mahtuuko(self):
        self.varasto = Varasto(10, 5)

        self.varasto.lisaa_varastoon(6)

        self.assertAlmostEqual(self.varasto.saldo, 10)

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

    def test_virheellisen_maaran_ottaminen(self):
        self.varasto = Varasto(10)

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liikaa_ottaminen(self):
        self.varasto = Varasto(10)

        self.varasto.ota_varastosta(15)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_onko_tilaa_jaljella(self):
        self.varasto = Varasto(10, 4)

        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")

