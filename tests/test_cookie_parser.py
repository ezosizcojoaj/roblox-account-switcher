from rasm.utils.cookie_parser import extract_roblosecurity, mask_cookie


def test_extract_from_header_dump():
    raw = "Cookie: .ROBLOSECURITY=" + "A" * 120 + "; other=1"
    assert extract_roblosecurity(raw) == "A" * 120


def test_extract_from_bare_cookie():
    cookie = "_|WARNING:-DO-NOT-SHARE-THIS." + "x" * 100
    assert extract_roblosecurity(cookie) == cookie


def test_extract_returns_none_for_garbage():
    assert extract_roblosecurity("hello world") is None


def test_mask_cookie():
    assert mask_cookie("ABCDEFGHIJKLMNOP") == "ABCD...MNOP"