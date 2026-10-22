from pathlib import Path

from rasm.core.account_store import AccountStore
from rasm.models.account import RobloxAccount


def _sample(uid: str = "123") -> RobloxAccount:
    return RobloxAccount(
        user_id=uid,
        username="testuser",
        roblosecurity="_|fake-cookie-" + "z" * 80,
        robux=500,
    )


def test_roundtrip(tmp_path: Path):
    store = AccountStore(tmp_path, "test-key")
    store.upsert(_sample())
    assert len(store) == 1

    reloaded = AccountStore(tmp_path, "test-key")
    reloaded.load()
    assert reloaded.get("123").username == "testuser"


def test_remove(tmp_path: Path):
    store = AccountStore(tmp_path, "test-key")
    store.upsert(_sample("abc"))
    assert store.remove("abc") is True
    assert store.get("abc") is None