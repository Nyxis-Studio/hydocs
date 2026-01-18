# CaseInsensitiveHashStrategy

**Overview**
Hash strategy that treats string keys in a case-insensitive manner.
Falls back to default `hashCode` and `equals` for non-string keys.

**Constructors**
- Not applicable. Use `getInstance()`.

**Methods**
- `getInstance()`: returns the shared singleton instance.
- `hashCode(K key)`: computes case-insensitive hash for strings.
- `equals(K a, K b)`: compares strings ignoring case, otherwise uses `equals`.

**Notes**
- Implements `Hash.Strategy<K>` from fastutil.
