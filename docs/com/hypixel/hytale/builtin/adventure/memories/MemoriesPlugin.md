**Source Hash:** `a4a8c81a84f0b1f9baebef1b6b4200c5713c8e872475fbe4eee0331790aefc35`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesPlugin

## Overview
Plugin that manages the memories feature, including memory providers, player memory storage, and UI interactions. Loads recorded memories from disk, tracks collected memories by category, and registers systems for memory collection and temple respawns.

## Field Descriptions
- `instance`: Singleton plugin instance.
- `config`: Plugin configuration for collection radii.
- `providers`: Registered memory providers.
- `allMemories`: Cached map of all memories by category.
- `playerMemoriesComponentType`: Component type for player memory storage.
- `recordedMemories`: Persisted set of memories recorded globally.
- `hasInitializedMemories`: Tracks whether the plugin has loaded memories from disk.

## Constructor Descriptions
- `MemoriesPlugin(JavaPluginInit init)`: Initializes the plugin and sets the singleton instance.

## Method Descriptions
- `get()`: Returns the singleton instance.
- `setup()`: Registers commands, UI pages, components, memory providers, and systems.
- `start()`: Loads recorded memories from `memories.json` and caches provider data.
- `shutdown()`: Persists recorded memories to disk.
- `getConfig()`: Returns the plugin configuration.
- `getPlayerMemoriesComponentType()`: Returns the component type for player memory storage.
- `registerMemoryProvider(MemoryProvider<T> memoryProvider)`: Registers a memory provider and its codec.
- `getAllMemories()`: Returns the cached map of all memories by category.
- `getMemoriesLevel(GameplayConfig gameplayConfig)`: Computes the current memories level based on recorded memories.
- `getMemoriesForNextLevel(GameplayConfig gameplayConfig)`: Returns how many memories are needed to reach the next level, or `-1` if maxed.
- `hasRecordedMemory(Memory memory)`: Checks whether a memory has been recorded globally.
- `recordPlayerMemories(PlayerMemories playerMemories)`: Transfers player memories into the global record and persists.
- `getRecordedMemories()`: Returns a snapshot of recorded memories.
- `clearRecordedMemories()`: Clears all recorded memories and persists the empty set.
- `recordAllMemories()`: Marks all known memories as recorded and persists.

## Usage Notes
- `memories.json` is stored under the universe path and is read/written on start and shutdown.
- Provider data is rebuilt after asset loading events to keep categories current.

## Examples
```java
MemoriesPlugin memories = MemoriesPlugin.get();
```
