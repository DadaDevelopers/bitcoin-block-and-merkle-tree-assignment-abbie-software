# Assignment 6: Bitcoin Block and Merkle Tree Assignment

## Overview
This assignment explores Bitcoin's block structure and Merkle tree construction through hands-on exploration and visualization.

---

## Task 1: Block Inspection

**Status:** ✅ Complete

**Block Details:**
- **Block Height:** 964736
- **Block Hash:** [PASTE YOUR BLOCK HASH]
- **Previous Block Hash:** [PASTE PREVIOUS BLOCK HASH]
- **Merkle Root:** [PASTE BLOCK MERKLE ROOT]
- **Number of Transactions:** 4,967
- **Timestamp:** 2026-08-30 17:06:39

**Explorer Used:** mempool.space

**Key Findings:**
- The block contains 4,967 transactions.
- The Merkle root is a cryptographic summary of all transactions.
- The previous block hash links this block to the one before it, forming the blockchain.

---

## Task 2: Merkle Tree Visualization

**Status:** ✅ Complete

**Transaction Hashes Used:**
| Transaction | Hash |
|-------------|------|
| TxA | e9ee0979de734876ad947f5520f2ace187067d6f89f9811ebaf5794511b05ffb |
| TxB | 282a6a67c44b40ff3735017653b59661ac3a76fc64df5d071dc1e2e9ee913f7a |
| TxC | 50b68501465d2ce2681900f73ae5e922a07e45c81cfa9e7981520d155bcc30ea |
| TxD | 3016c455b2db500764eb32a957fe98fad3b0b747fce99175af6acae9f8e69d68 |

**Merkle Tree Structure:**
Merkle Root
|
+------------+------------+
| |
Hash(AB) Hash(CD)
| |
+---+---+ +---+---+
| | | |
TxA TxB TxC TxD

text

**Calculated Values:**
- Hash(AB): [PASTE HASH(AB)]
- Hash(CD): [PASTE HASH(CD)]
- Merkle Root: [PASTE COMPUTED MERKLE ROOT]

**Verification:**
| Check | Result |
|-------|--------|
| Computed Merkle Root (4 transactions) | [PASTE COMPUTED ROOT] |
| Block's Merkle Root (4,967 transactions) | [PASTE BLOCK MERKLE ROOT] |
| Match | ❌ (Expected — different transaction sets) |

**Key Insight:**
The computed Merkle root does not match the block's Merkle root because:
- My calculation uses only 4 transactions (TxA, TxB, TxC, TxD)
- The block's Merkle root uses all 4,967 transactions in the block
- This demonstrates that Merkle roots are unique to the exact set of transactions used

---

## Files in This Submission

| File | Description |
|------|-------------|
| `README.md` | This main report |
| `block-inspection.md` | Detailed Task 1 results |
| `merkle-tree-diagram.pdf` | Visual Merkle tree diagram |
| `code/calculate_merkle.py` | Python script for Merkle root calculation |

---

## How to Run the Code

```bash
cd code
python3 calculate_merkle.py
Tools Used
Block Explorer: mempool.space

Programming Language: Python 3

Libraries: hashlib (standard library)

Key Learnings
Merkle trees allow efficient verification of transactions without downloading the entire block.

Changing any transaction changes the Merkle root, ensuring data integrity.

The Merkle root is stored in the block header, securing all transactions in the block.

Merkle roots are unique to the exact set of transactions they are computed from.

References
mempool.space

Bitcoin Developer Guide - Merkle Trees

Bitcoin.org - Block Headers
