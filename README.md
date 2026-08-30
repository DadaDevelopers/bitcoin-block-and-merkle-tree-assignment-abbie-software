# Assignment 6: Bitcoin Block and Merkle Tree Assignment

## Overview
This assignment explores Bitcoin's block structure and Merkle tree construction through hands-on exploration and visualization.

---

## Task 1: Block Inspection

**Status:**  Complete

**Block Details:**
-| **Block Height** | 964736 |
| **Block Hash** | 000000000000000000013f386abff9abeda1dac7431d6703a4d14d3ac9e4bd76 |
| **Previous Block Hash** | 964735 |
| **Merkle Root** | 47b9e398d4b000dff4a631b5c60f7c5f3df7ca6bafeae9ac37dc286a93ee202b |
| **Number of Transactions** | 4388 |
| **Timestamp** | 2026-08-30 17:06:39 |

**Explorer Used:** mempool.space

**Key Findings:**
- The block contains 4,388 transactions.
- The Merkle root is a cryptographic summary of all transactions.
- The previous block hash links this block to the one before it, forming the blockchain.

---

## Task 2: Merkle Tree Visualization

**Status:** Complete

**Transaction Hashes Used:**
| Transaction | Hash |
|-------------|------|
| **TxA** | 5ecffdb73872911773b0316a6be3b0148f2e57f272f659237c4334b6c97ec2f7 |
| **TxB** | f6dfd5b3b0dc2c5ea42e3b424ee6377c8070d011acc6b24ddc25a6491a3ffbdf |
| **TxC** | 595c018fded6c7fcfc25730b34adb02c306a5a444132ab195e089dee72428207 |
| **TxD** | 5c3795afa3f404ddf268f5528b5f9dbc6c42ad6440d2d24cfbf6214b2f37f961 |
### Merkle Tree Diagram
       Merkle Root
             |
+------------+------------+
|                         |
Hash(AB)              Hash(CD)
|                         |
+---+---+             +---+---+
|       |             |       |
TxA    TxB           TxC     TxD


---

**Calculated Values:**
- Hash(AB): 52f502d53b40c733df45a0220c85acfe9ab59ae03c7799a91806d8bcb490b3c6
- Hash(CD): 6485357dfc861796f3a10b98d7e1a9417b4bf9d1294b7ca3cece125db98254f9

- Merkle Root: 15535c8f5211390a31a86c2cc7e4e8ab624591419077b6bece93b5453e7dffac

### Verification

| Check | Result |
|-------|--------|
| Computed Merkle Root (for 4 transactions) |  15535c8f5211390a31a86c2cc7e4e8ab624591419077b6bece93b5453e7dffac |
| Block's Merkle Root (for all 4,388 transactions) |47b9e398d4b000dff4a631b5c60f7c5f3df7ca6bafeae9ac37dc286a93ee202b |
| Match | NO(Expected — block has 4,388 transactions, not just 4) |

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
