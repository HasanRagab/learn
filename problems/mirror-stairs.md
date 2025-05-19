### Problem Name: `mirror-stairs`

#### Problem Statement:

You're designing a fancy staircase for a palace 👑. It's not just any staircase — it's **mirrored**. That means it builds up, then reflects perfectly on the other side. Your job is to print a **mirrored staircase pattern** of numbers from `1` to `n` and back down.

#### Input:

* A single integer `n` (1 ≤ n ≤ 100) — the number of steps to the peak.

#### Output:

* Print `2n - 1` lines.
* Each line `i` (1-based) should contain numbers from `1` to the current step, space-separated.
* The staircase builds up to `n` and then mirrors back down to `1`.

#### Example:

**Input:**

```
4
```

**Output:**

```
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
```

#### Another Example:

**Input:**

```
2
```

**Output:**

```
1
1 2
1
```

#### Notes:

* Total number of lines is `2n - 1`.
* Think of it like walking up the stairs to the throne room, then back down in reverse.

---
