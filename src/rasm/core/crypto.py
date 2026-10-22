from __future__ import annotations

import base64
import hashlib
import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class VaultCipher:
    """AES-256-GCM wrapper used to protect the accounts vault at rest."""

    NONCE_SIZE = 12
    TAG_SIZE = 16

    def __init__(self, secret_key: str) -> None:
        self._key = hashlib.sha256(secret_key.encode("utf-8")).digest()

    def encrypt(self, plaintext: bytes) -> bytes:
        nonce = get_random_bytes(self.NONCE_SIZE)
        cipher = AES.new(self._key, AES.MODE_GCM, nonce=nonce)
        ct, tag = cipher.encrypt_and_digest(plaintext)
        return base64.b64encode(nonce + tag + ct)

    def decrypt(self, blob: bytes) -> bytes:
        data = base64.b64decode(blob)
        nonce, tag, ct = data[: self.NONCE_SIZE], data[self.NONCE_SIZE : self.NONCE_SIZE + self.TAG_SIZE], data[self.NONCE_SIZE + self.TAG_SIZE :]
        cipher = AES.new(self._key, AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ct, tag)