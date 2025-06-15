
**Lazy Prim's MST Cheat Sheet**
1. Core Idea (Remember This!)
"Grow a tree by always picking the smallest edge touching it."

2. 3 Key Components to Memorize
Min-Heap → Stores edges ((weight, u, v))

Visited Set → Tracks nodes already in MST

MST Edges → Stores the result

Mnemonic Shortcuts
"HVM" → Heap + Visited + MST

"Pick, Skip, Grow" →

Pick smallest edge from heap.

Skip if node is visited.

Grow MST by adding edges.

#Common Pitfalls
Forget to skip visited nodes → Infinite loop.

Heap stores duplicates → Safe but inefficient.

When to Use Lazy Prim?
Sparse graphs (few edges).

Coding interviews (easier to implement than eager).