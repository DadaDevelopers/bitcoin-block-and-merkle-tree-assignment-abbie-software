#!/usr/bin/env python3
"""
Merkle Tree Calculator
"""

import hashlib

def double_sha256(data):
    """Double SHA-256 hash"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def hash_pair(hash1, hash2):
    """Hash two hashes together"""
    bytes1 = bytes.fromhex(hash1)
    bytes2 = bytes.fromhex(hash2)
    combined = bytes1 + bytes2
    result = double_sha256(combined)
    return result.hex()


tx_a = "5ecffdb73872911773b0316a6be3b0148f2e57f272f659237c4334b6c97ec2f7 "
tx_b = "f6dfd5b3b0dc2c5ea42e3b424ee6377c8070d011acc6b24ddc25a6491a3ffbdf"
tx_c = "595c018fded6c7fcfc25730b34adb02c306a5a444132ab195e089dee72428207"
tx_d = "5c3795afa3f404ddf268f5528b5f9dbc6c42ad6440d2d24cfbf6214b2f37f961"

print("=== Merkle Tree Calculation ===")
print()
print("Leaf Nodes:")
print(f"  TxA: {tx_a}")
print(f"  TxB: {tx_b}")
print(f"  TxC: {tx_c}")
print(f"  TxD: {tx_d}")
print()

print("Level 1: Hash Pairs")
hash_ab = hash_pair(tx_a, tx_b)
hash_cd = hash_pair(tx_c, tx_d)
print(f"  Hash(AB): {hash_ab}")
print(f"  Hash(CD): {hash_cd}")
print()

print("Level 2: Merkle Root")
merkle_root = hash_pair(hash_ab, hash_cd)
print(f"  Merkle Root: {merkle_root}")
