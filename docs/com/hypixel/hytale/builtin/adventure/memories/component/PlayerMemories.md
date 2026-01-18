**Source Hash:** `c347bd0c2b995366a53847a27c828910596408ec21db2a290ea612354e20eb21`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# PlayerMemories

## Overview
Player component that stores collected memories and capacity. Allows recording memories until capacity is reached and supports transferring recorded memories to the global record.

## Field Descriptions
- `CODEC`: Builder codec for capacity and stored memories.
- `memories`: Ordered set of recorded memories.
- `memoriesCapacity`: Maximum number of memories the player can hold.

## Constructor Descriptions
- `PlayerMemories()`: Creates a component with empty memory storage.

## Method Descriptions
- `getComponentType()`: Returns the entity component type for player memories.
- `clone()`: Returns a copy of the component with the same recorded memories and capacity.
- `getMemoriesCapacity()`: Returns the capacity value.
- `setMemoriesCapacity(int memoriesCapacity)`: Updates the maximum number of memories.
- `recordMemory(Memory memory)`: Adds a memory if capacity permits.
- `hasMemories()`: Returns whether the player currently has any memories.
- `takeMemories(Set<Memory> outMemories)`: Transfers stored memories into the provided set and clears local storage.
- `getRecordedMemories()`: Returns an unmodifiable view of recorded memories.

## Usage Notes
- `recordMemory` returns `false` when capacity is full without modifying storage.

## Examples
```java
PlayerMemories memories = store.ensureAndGetComponent(ref, PlayerMemories.getComponentType());
```
