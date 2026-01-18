**Source Hash:** `d79425b7109e1ca6cf7aa83413f8c9d64e7876e060b3bb531d894c725f9e8708`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesPageSupplier

## Overview
Custom page supplier that constructs a `MemoriesPage` from an interaction context.

## Constructor Descriptions
- `MemoriesPageSupplier()`: Creates the page supplier instance.

## Method Descriptions
- `tryCreate(Ref<EntityStore> ref, ComponentAccessor<EntityStore> componentAccessor, PlayerRef playerRef, InteractionContext context)`: Returns a new `MemoriesPage` using the target block position.

## Examples
```java
MemoriesPageSupplier supplier = new MemoriesPageSupplier();
```
