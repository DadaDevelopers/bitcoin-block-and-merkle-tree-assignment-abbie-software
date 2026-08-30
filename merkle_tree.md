# Assignment 6: Merkle Tree Visualization

## Task 2: Merkle Tree Construction

### Transaction Hashes Used

| Transaction | Hash |
|-------------|------|
| **TxA** | 5ecffdb73872911773b0316a6be3b0148f2e57f272f659237c4334b6c97ec2f7 |
| **TxB** | f6dfd5b3b0dc2c5ea42e3b424ee6377c8070d011acc6b24ddc25a6491a3ffbdf |
| **TxC** | 595c018fded6c7fcfc25730b34adb02c306a5a444132ab195e089dee72428207 |
| **TxD** | 5c3795afa3f404ddf268f5528b5f9dbc6c42ad6440d2d24cfbf6214b2f37f961 |

---

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

### Step-by-Step Hashing Process

#### Level 0: Leaf Nodes (Transaction Hashes)
| **TxA** | 5ecffdb73872911773b0316a6be3b0148f2e57f272f659237c4334b6c97ec2f7 |
| **TxB** | f6dfd5b3b0dc2c5ea42e3b424ee6377c8070d011acc6b24ddc25a6491a3ffbdf |
| **TxC** | 595c018fded6c7fcfc25730b34adb02c306a5a444132ab195e089dee72428207 |
| **TxD** | 5c3795afa3f404ddf268f5528b5f9dbc6c42ad6440d2d24cfbf6214b2f37f961 |



#### Level 1: Hash Pairs
Hash(AB) = SHA256(SHA256(TxA + TxB))
Hash(AB): 52f502d53b40c733df45a0220c85acfe9ab59ae03c7799a91806d8bcb490b3c6
Hash(CD) = SHA256(SHA256(TxC + TxD))
Hash(CD): 6485357dfc861796f3a10b98d7e1a9417b4bf9d1294b7ca3cece125db98254f9



#### Level 2: Merkle Root
Merkle Root = SHA256(SHA256(Hash(AB) + Hash(CD)))
Merkle Root: 15535c8f5211390a31a86c2cc7e4e8ab624591419077b6bece93b5453e7dffac



---

### Verification

| Check | Result |
|-------|--------|
| Computed Merkle Root (for 4 transactions) |  15535c8f5211390a31a86c2cc7e4e8ab624591419077b6bece93b5453e7dffac |
| Block's Merkle Root (for all 4,388 transactions) |47b9e398d4b000dff4a631b5c60f7c5f3df7ca6bafeae9ac37dc286a93ee202b |
| Match | NO(Expected — block has 4,388 transactions, not just 4) |
