import json  # noqa: F401


def test_h01_cur_try_0001(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0002(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0003(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0004(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0005(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0006(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0007(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0008(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0009(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0010(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes
