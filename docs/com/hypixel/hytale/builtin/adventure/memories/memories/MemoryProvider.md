**Source Hash:** `8d58cb0cc1308081302c0d33a9017486e2b745ecde0fe0f68895ddbcafb4edf4`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoryProvider

## Overview
Abstract provider that supplies memories of a specific type and category. Stores codec metadata, provider ID, and collection radius defaults.

## Field Descriptions
- `id`: Provider identifier used for configuration lookup.
- `codec`: Codec for the memory subtype.
- `defaultRadius`: Default collection radius when no config override exists.

## Constructor Descriptions
- `MemoryProvider(String id, BuilderCodec<T> codec, double defaultRadius)`: Creates a provider with an ID, codec, and default collection radius.

## Method Descriptions
- `getId()`: Returns the provider identifier.
- `getCodec()`: Returns the codec for the memory subtype.
- `getCollectionRadius()`: Returns the collection radius from config, falling back to the default.
- `getAllMemories()`: Returns all memories grouped by category.

## Usage Notes
- `getCollectionRadius` reads from `MemoriesPlugin` configuration using the provider ID.

## Examples
```java
MemoryProvider<NPCMemory> provider = new NPCMemoryProvider();
```
