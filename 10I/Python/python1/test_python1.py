# --- START OF FILE test_python1.py ---
import pytest
import math
from unittest.mock import patch
from python1 import (
    osszead,
    kisebb,
    nagyobb,
    szamtani_kozep,
    negyzet_kerulet,
    negyzet_terulet,
    teglalap_kerulet,
    teglalap_terulet,
    kulonbseg,
    maradek,
    paros,
    kettovel_oszthato,
    harommal_oszthato,
    hettel_oszthato,
    kocka_terfogat,
    teglatest_terfogat,
    derekszogu_haromszog_terulet,
    derekszogu_haromszog_atfogo,
    negyzet_atloja,
    teglalap_atloja,
    abszolut,
    kor_kerulete,
    kor_terulete,
)

def test_osszead():
    assert osszead(2, 3) == 5
    assert osszead(-1, 1) == 0
    assert osszead(0, 0) == 0
    assert osszead(2.5, 3.5) == 6

    @patch('python1.sum')
    def test_sum_not_called(mock_sum):
        osszead(1, 2)
        mock_sum.assert_not_called()


def test_kisebb():
    assert kisebb(2, 3) == 2
    assert kisebb(3, 2) == 2
    assert kisebb(-1, 1) == -1
    assert kisebb(1, -1) == -1
    assert kisebb(0, 0) == 0
    assert kisebb(2.5, 3.5) == 2.5
    assert kisebb(3.5, 2.5) == 2.5


    @patch('python1.min')
    def test_min_not_called(mock_min):
        kisebb(1, 2)
        mock_min.assert_not_called()


def test_nagyobb():
    assert nagyobb(2, 3) == 3
    assert nagyobb(3, 2) == 3
    assert nagyobb(-1, 1) == 1
    assert nagyobb(1, -1) == 1
    assert nagyobb(0, 0) == 0
    assert nagyobb(2.5, 3.5) == 3.5
    assert nagyobb(3.5, 2.5) == 3.5


    @patch('python1.max')
    def test_max_not_called(mock_max):
        nagyobb(1, 2)
        mock_max.assert_not_called()



def test_szamtani_kozep():
    assert szamtani_kozep(2, 4) == 3
    assert szamtani_kozep(-1, 1) == 0
    assert szamtani_kozep(0, 0) == 0
    assert szamtani_kozep(2.5, 3.5) == 3.0


def test_negyzet_kerulet():
    assert negyzet_kerulet(5) == 20
    assert negyzet_kerulet(2.5) == 10.0
    assert negyzet_kerulet(0) == 0


def test_negyzet_terulet():
    assert negyzet_terulet(5) == 25
    assert negyzet_terulet(2.5) == 6.25
    assert negyzet_terulet(0) == 0


def test_teglalap_kerulet():
    assert teglalap_kerulet(2, 3) == 10
    assert teglalap_kerulet(2.5, 3.5) == 12.0
    assert teglalap_kerulet(0, 5) == 10


def test_teglalap_terulet():
    assert teglalap_terulet(2, 3) == 6
    assert teglalap_terulet(2.5, 3.5) == 8.75
    assert teglalap_terulet(0, 5) == 0


def test_kulonbseg():
    assert kulonbseg(5, 2) == 3
    assert kulonbseg(2, 5) == -3
    assert kulonbseg(-1, 1) == -2
    assert kulonbseg(1, -1) == 2
    assert kulonbseg(0, 0) == 0
    assert kulonbseg(5.5, 2.5) == 3.0


def test_maradek():
    assert maradek(5, 2) == 1
    assert maradek(10, 3) == 1
    assert maradek(7, 7) == 0
    assert maradek(0, 5) == 0


def test_paros():
    assert paros(2) == True
    assert paros(4) == True
    assert paros(0) == True
    assert paros(1) == False
    assert paros(3) == False
    assert paros(-2) == True


def test_kettovel_oszthato():
    assert kettovel_oszthato(2) == True
    assert kettovel_oszthato(4) == True
    assert kettovel_oszthato(0) == True
    assert kettovel_oszthato(1) == False
    assert kettovel_oszthato(3) == False
    assert kettovel_oszthato(-2) == True


def test_harommal_oszthato():
    assert harommal_oszthato(3) == True
    assert harommal_oszthato(6) == True
    assert harommal_oszthato(0) == True
    assert harommal_oszthato(1) == False
    assert harommal_oszthato(4) == False


def test_hettel_oszthato():
    assert hettel_oszthato(7) == True
    assert hettel_oszthato(14) == True
    assert hettel_oszthato(0) == True
    assert hettel_oszthato(1) == False
    assert hettel_oszthato(8) == False


def test_kocka_terfogat():
    assert kocka_terfogat(2) == 8
    assert kocka_terfogat(5) == 125
    assert kocka_terfogat(0) == 0
    assert kocka_terfogat(2.5) == 15.625


def test_teglatest_terfogat():
    assert teglatest_terfogat(2, 3, 4) == 24
    assert teglatest_terfogat(1, 1, 1) == 1
    assert teglatest_terfogat(0, 5, 5) == 0
    assert teglatest_terfogat(2.5, 3.5, 1.5) == 13.125


def test_derekszogu_haromszog_terulet():
    assert derekszogu_haromszog_terulet(3, 4) == 6
    assert derekszogu_haromszog_terulet(5, 12) == 30
    assert derekszogu_haromszog_terulet(0, 5) == 0
    assert derekszogu_haromszog_terulet(2.5, 3.5) == 4.375


def test_derekszogu_haromszog_atfogo():
    assert derekszogu_haromszog_atfogo(3, 4) == 5
    assert derekszogu_haromszog_atfogo(5, 12) == 13
    assert derekszogu_haromszog_atfogo(0, 0) == 0
    assert derekszogu_haromszog_atfogo(1, 1) == math.sqrt(2)


def test_negyzet_atloja():
    assert negyzet_atloja(5) == 5 * math.sqrt(2)
    assert negyzet_atloja(0) == 0
    assert negyzet_atloja(2.5) == 2.5 * math.sqrt(2)


def test_teglalap_atloja():
    assert teglalap_atloja(3, 4) == 5
    assert teglalap_atloja(5, 12) == 13
    assert teglalap_atloja(0, 0) == 0
    assert teglalap_atloja(1, 1) == math.sqrt(2)


def test_abszolut():
    assert abszolut(5) == 5
    assert abszolut(-5) == 5
    assert abszolut(0) == 0
    assert abszolut(-2.5) == 2.5


def test_kor_kerulete():
    assert kor_kerulete(5) == 2 * math.pi * 5
    assert kor_kerulete(0) == 0
    assert kor_kerulete(2.5) == 2 * math.pi * 2.5


def test_kor_terulete():
    assert kor_terulete(5) == math.pi * 5 ** 2
    assert kor_terulete(0) == 0
    assert kor_terulete(2.5) == math.pi * 2.5 ** 2
