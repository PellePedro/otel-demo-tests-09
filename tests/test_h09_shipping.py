import json  # noqa: F401


def test_h09_1ymwwn1n4o_x5_mxn_cupertino_0001(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_l9ecav7kim_x10_myr_seattle_0002(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_2zyfj3gm2n_x1_nok_toronto_0003(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_0puk6v6ev0_x2_nzd_mountain_view_0004(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_ls4psxunum_x3_php_redmond_0005(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_9siqt8tojo_x4_pln_cupertino_0006(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_6e92zmyyfz_x5_ron_seattle_0007(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_hqtgwgpnh4_x10_rub_toronto_0008(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_oljcespc7z_x1_sek_mountain_view_0009(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_66vchsjnup_x2_sgd_redmond_0010(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_1ymwwn1n4o_x3_thb_cupertino_0011(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_l9ecav7kim_x4_try_seattle_0012(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_2zyfj3gm2n_x5_usd_toronto_0013(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    assert cost["units"] == 44
    assert cost["nanos"] == 950000000


def test_h09_0puk6v6ev0_x10_zar_mountain_view_0014(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_ls4psxunum_x1_aud_redmond_0015(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_9siqt8tojo_x2_bgn_cupertino_0016(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_6e92zmyyfz_x3_brl_seattle_0017(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_hqtgwgpnh4_x4_cad_toronto_0018(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_oljcespc7z_x5_chf_mountain_view_0019(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_66vchsjnup_x10_cny_redmond_0020(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_1ymwwn1n4o_x1_czk_cupertino_0021(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_l9ecav7kim_x2_dkk_seattle_0022(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_2zyfj3gm2n_x3_eur_toronto_0023(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_0puk6v6ev0_x4_gbp_mountain_view_0024(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_ls4psxunum_x5_hkd_redmond_0025(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_9siqt8tojo_x10_hrk_cupertino_0026(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_6e92zmyyfz_x1_huf_seattle_0027(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"


def test_h09_hqtgwgpnh4_x2_idr_toronto_0028(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "IDR",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "IDR"


def test_h09_oljcespc7z_x3_ils_mountain_view_0029(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "ILS",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ILS"


def test_h09_66vchsjnup_x4_inr_redmond_0030(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "INR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "INR"


def test_h09_1ymwwn1n4o_x5_isk_cupertino_0031(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 5}]),
        "currencyCode": "ISK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ISK"


def test_h09_l9ecav7kim_x10_jpy_seattle_0032(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 10}]),
        "currencyCode": "JPY",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "JPY"


def test_h09_2zyfj3gm2n_x1_krw_toronto_0033(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 1}]),
        "currencyCode": "KRW",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "KRW"


def test_h09_0puk6v6ev0_x2_mxn_mountain_view_0034(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 2}]),
        "currencyCode": "MXN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MXN"


def test_h09_ls4psxunum_x3_myr_redmond_0035(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 3}]),
        "currencyCode": "MYR",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "MYR"


def test_h09_9siqt8tojo_x4_nok_cupertino_0036(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 4}]),
        "currencyCode": "NOK",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NOK"


def test_h09_6e92zmyyfz_x5_nzd_seattle_0037(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 5}]),
        "currencyCode": "NZD",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "NZD"


def test_h09_hqtgwgpnh4_x10_php_toronto_0038(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 10}]),
        "currencyCode": "PHP",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PHP"


def test_h09_oljcespc7z_x1_pln_mountain_view_0039(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 1}]),
        "currencyCode": "PLN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "PLN"


def test_h09_66vchsjnup_x2_ron_redmond_0040(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 2}]),
        "currencyCode": "RON",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RON"


def test_h09_1ymwwn1n4o_x3_rub_cupertino_0041(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 3}]),
        "currencyCode": "RUB",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "RUB"


def test_h09_l9ecav7kim_x4_sek_seattle_0042(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 4}]),
        "currencyCode": "SEK",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SEK"


def test_h09_2zyfj3gm2n_x5_sgd_toronto_0043(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 5}]),
        "currencyCode": "SGD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "SGD"


def test_h09_0puk6v6ev0_x10_thb_mountain_view_0044(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 10}]),
        "currencyCode": "THB",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "THB"


def test_h09_ls4psxunum_x1_try_redmond_0045(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 1}]),
        "currencyCode": "TRY",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "TRY"


def test_h09_9siqt8tojo_x2_usd_cupertino_0046(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 2}]),
        "currencyCode": "USD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "USD"
    assert cost["units"] == 17
    assert cost["nanos"] == 980000000


def test_h09_6e92zmyyfz_x3_zar_seattle_0047(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 3}]),
        "currencyCode": "ZAR",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "ZAR"


def test_h09_hqtgwgpnh4_x4_aud_toronto_0048(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 4}]),
        "currencyCode": "AUD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "AUD"


def test_h09_oljcespc7z_x5_bgn_mountain_view_0049(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 5}]),
        "currencyCode": "BGN",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BGN"


def test_h09_66vchsjnup_x10_brl_redmond_0050(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 10}]),
        "currencyCode": "BRL",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "BRL"


def test_h09_1ymwwn1n4o_x1_cad_cupertino_0051(api):
    params = {
        "itemList": json.dumps([{"productId": "1YMWWN1N4O", "quantity": 1}]),
        "currencyCode": "CAD",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CAD"


def test_h09_l9ecav7kim_x2_chf_seattle_0052(api):
    params = {
        "itemList": json.dumps([{"productId": "L9ECAV7KIM", "quantity": 2}]),
        "currencyCode": "CHF",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CHF"


def test_h09_2zyfj3gm2n_x3_cny_toronto_0053(api):
    params = {
        "itemList": json.dumps([{"productId": "2ZYFJ3GM2N", "quantity": 3}]),
        "currencyCode": "CNY",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CNY"


def test_h09_0puk6v6ev0_x4_czk_mountain_view_0054(api):
    params = {
        "itemList": json.dumps([{"productId": "0PUK6V6EV0", "quantity": 4}]),
        "currencyCode": "CZK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "CZK"


def test_h09_ls4psxunum_x5_dkk_redmond_0055(api):
    params = {
        "itemList": json.dumps([{"productId": "LS4PSXUNUM", "quantity": 5}]),
        "currencyCode": "DKK",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "DKK"


def test_h09_9siqt8tojo_x10_eur_cupertino_0056(api):
    params = {
        "itemList": json.dumps([{"productId": "9SIQT8TOJO", "quantity": 10}]),
        "currencyCode": "EUR",
        "address": json.dumps({"streetAddress": "1 Infinite Loop", "zipCode": "95014", "city": "Cupertino", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "EUR"


def test_h09_6e92zmyyfz_x1_gbp_seattle_0057(api):
    params = {
        "itemList": json.dumps([{"productId": "6E92ZMYYFZ", "quantity": 1}]),
        "currencyCode": "GBP",
        "address": json.dumps({"streetAddress": "410 Terry Ave N", "zipCode": "98109", "city": "Seattle", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "GBP"


def test_h09_hqtgwgpnh4_x2_hkd_toronto_0058(api):
    params = {
        "itemList": json.dumps([{"productId": "HQTGWGPNH4", "quantity": 2}]),
        "currencyCode": "HKD",
        "address": json.dumps({"streetAddress": "100 Queen St W", "zipCode": "M5H 2N2", "city": "Toronto", "state": "ON", "country": "Canada"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HKD"


def test_h09_oljcespc7z_x3_hrk_mountain_view_0059(api):
    params = {
        "itemList": json.dumps([{"productId": "OLJCESPC7Z", "quantity": 3}]),
        "currencyCode": "HRK",
        "address": json.dumps({"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HRK"


def test_h09_66vchsjnup_x4_huf_redmond_0060(api):
    params = {
        "itemList": json.dumps([{"productId": "66VCHSJNUP", "quantity": 4}]),
        "currencyCode": "HUF",
        "address": json.dumps({"streetAddress": "One Microsoft Way", "zipCode": "98052", "city": "Redmond", "state": "WA", "country": "United States"}),
    }
    resp = api.get("/api/shipping", params=params)
    assert resp.status_code == 200
    cost = resp.json()
    assert cost["currencyCode"] == "HUF"
