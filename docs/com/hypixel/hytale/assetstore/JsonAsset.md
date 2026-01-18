**Source Hash:** `a6222fa0761fc7986d20b78c7528d0ac4782489b4c7d04741329e1ee3efcf2a5`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# JsonAsset

## Overview
Minimal interface for JSON-backed assets identified by a key. Used as the base contract for asset store entries.

## Field Descriptions
- `none`: Interface-only contract; no fields.

## Constructor Descriptions
- None. Interface type.

## Method Descriptions
- `getId()`: Returns the asset identifier.

## Usage Notes
- Use `K` to define the asset key type.

## Examples
```java
public final class MyAsset implements JsonAsset<String> {
    @Override
    public String getId() {
        return "my_asset";
    }
}
```
