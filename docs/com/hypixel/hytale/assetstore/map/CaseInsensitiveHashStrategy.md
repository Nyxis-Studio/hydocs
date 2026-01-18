**Source Hash:** `a06a70c6ab0961574478d8faf960c557e4c3043ef29b662a61bdb87ef4fa2e7d`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# CaseInsensitiveHashStrategy

## Overview
Hash strategy that treats string keys in a case-insensitive manner. Falls back to default `hashCode` and `equals` for non-string keys.

## Field Descriptions
- `INSTANCE`: Singleton instance used by `getInstance()`.

## Constructor Descriptions
- None. Use `getInstance()`.

## Method Descriptions
- `getInstance()`: Returns the shared singleton instance.
- `hashCode(K key)`: Returns a case-insensitive hash for string keys, or 0 for null.
- `equals(K a, K b)`: Returns true for identical references or case-insensitive string matches; otherwise falls back to `equals`.

## Usage Notes
- Implements `Hash.Strategy<K>` from fastutil for custom map/set hashing.

## Examples
```java
Hash.Strategy<String> strategy = CaseInsensitiveHashStrategy.getInstance();
```
