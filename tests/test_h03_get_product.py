import json  # noqa: F401


def test_h03_1ymwwn1n4o_dkk_0001(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_l9ecav7kim_eur_0002(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_2zyfj3gm2n_gbp_0003(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_0puk6v6ev0_hkd_0004(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_ls4psxunum_hrk_0005(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_9siqt8tojo_huf_0006(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_6e92zmyyfz_idr_0007(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_hqtgwgpnh4_ils_0008(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_oljcespc7z_inr_0009(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_66vchsjnup_isk_0010(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_1ymwwn1n4o_jpy_0011(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_l9ecav7kim_krw_0012(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_2zyfj3gm2n_mxn_0013(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_0puk6v6ev0_myr_0014(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_ls4psxunum_nok_0015(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_9siqt8tojo_nzd_0016(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_6e92zmyyfz_php_0017(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_hqtgwgpnh4_pln_0018(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_oljcespc7z_ron_0019(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_66vchsjnup_rub_0020(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_1ymwwn1n4o_sek_0021(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_l9ecav7kim_sgd_0022(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_2zyfj3gm2n_thb_0023(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_0puk6v6ev0_try_0024(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_ls4psxunum_usd_0025(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 57
    assert product["priceUsd"]["nanos"] == 80000000


def test_h03_9siqt8tojo_zar_0026(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_6e92zmyyfz_aud_0027(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_hqtgwgpnh4_bgn_0028(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_oljcespc7z_brl_0029(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_66vchsjnup_cad_0030(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_1ymwwn1n4o_chf_0031(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_l9ecav7kim_cny_0032(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_2zyfj3gm2n_czk_0033(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_0puk6v6ev0_dkk_0034(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_ls4psxunum_eur_0035(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_9siqt8tojo_gbp_0036(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_6e92zmyyfz_hkd_0037(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_hqtgwgpnh4_hrk_0038(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_oljcespc7z_huf_0039(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_66vchsjnup_idr_0040(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_1ymwwn1n4o_ils_0041(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_l9ecav7kim_inr_0042(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_2zyfj3gm2n_isk_0043(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_0puk6v6ev0_jpy_0044(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_ls4psxunum_krw_0045(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_9siqt8tojo_mxn_0046(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_6e92zmyyfz_myr_0047(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_hqtgwgpnh4_nok_0048(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_oljcespc7z_nzd_0049(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_66vchsjnup_php_0050(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_1ymwwn1n4o_pln_0051(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_l9ecav7kim_ron_0052(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_2zyfj3gm2n_rub_0053(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_0puk6v6ev0_sek_0054(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_ls4psxunum_sgd_0055(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_9siqt8tojo_thb_0056(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_6e92zmyyfz_try_0057(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_hqtgwgpnh4_usd_0058(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 0
    assert product["priceUsd"]["nanos"] == 990000000


def test_h03_oljcespc7z_zar_0059(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_66vchsjnup_aud_0060(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_1ymwwn1n4o_bgn_0061(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_l9ecav7kim_brl_0062(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_2zyfj3gm2n_cad_0063(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_0puk6v6ev0_chf_0064(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_ls4psxunum_cny_0065(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_9siqt8tojo_czk_0066(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_6e92zmyyfz_dkk_0067(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_hqtgwgpnh4_eur_0068(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_oljcespc7z_gbp_0069(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_66vchsjnup_hkd_0070(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_1ymwwn1n4o_hrk_0071(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_l9ecav7kim_huf_0072(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_2zyfj3gm2n_idr_0073(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_0puk6v6ev0_ils_0074(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_ls4psxunum_inr_0075(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_9siqt8tojo_isk_0076(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_6e92zmyyfz_jpy_0077(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_hqtgwgpnh4_krw_0078(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_oljcespc7z_mxn_0079(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_66vchsjnup_myr_0080(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_1ymwwn1n4o_nok_0081(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_l9ecav7kim_nzd_0082(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_2zyfj3gm2n_php_0083(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_0puk6v6ev0_pln_0084(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_ls4psxunum_ron_0085(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_9siqt8tojo_rub_0086(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_6e92zmyyfz_sek_0087(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_hqtgwgpnh4_sgd_0088(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_oljcespc7z_thb_0089(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_66vchsjnup_try_0090(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_1ymwwn1n4o_usd_0091(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 129
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_l9ecav7kim_zar_0092(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_2zyfj3gm2n_aud_0093(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_0puk6v6ev0_bgn_0094(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_ls4psxunum_brl_0095(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_9siqt8tojo_cad_0096(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_6e92zmyyfz_chf_0097(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_hqtgwgpnh4_cny_0098(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_oljcespc7z_czk_0099(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_66vchsjnup_dkk_0100(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_1ymwwn1n4o_eur_0101(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_l9ecav7kim_gbp_0102(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_2zyfj3gm2n_hkd_0103(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_0puk6v6ev0_hrk_0104(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_ls4psxunum_huf_0105(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_9siqt8tojo_idr_0106(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_6e92zmyyfz_ils_0107(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_hqtgwgpnh4_inr_0108(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_oljcespc7z_isk_0109(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_66vchsjnup_jpy_0110(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_1ymwwn1n4o_krw_0111(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_l9ecav7kim_mxn_0112(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_2zyfj3gm2n_myr_0113(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_0puk6v6ev0_nok_0114(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_ls4psxunum_nzd_0115(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_9siqt8tojo_php_0116(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_6e92zmyyfz_pln_0117(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_hqtgwgpnh4_ron_0118(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_oljcespc7z_rub_0119(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_66vchsjnup_sek_0120(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SEK"
