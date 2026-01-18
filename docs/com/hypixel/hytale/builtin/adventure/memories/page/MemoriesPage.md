**Source Hash:** `42964b2859ca26c385fdea8dd6a468ffa72c9452785f077654daa4b6f5b4a483`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesPage

## Overview
Interactive custom UI page that displays memories by category and shows details for selected memories. Supports recording player memories into the global collection and updates UI elements based on discovery progress.

## Field Descriptions
- `currentCategory`: Currently selected memory category, or null for the category overview.
- `selectedMemory`: Memory selected within the current category.
- `recordMemoriesParticlesPosition`: Position used to spawn particles when recording memories.

## Constructor Descriptions
- `MemoriesPage(PlayerRef playerRef, BlockPosition blockPosition)`: Creates the page and stores the particle spawn position from the block interaction.

## Method Descriptions
- `build(Ref<EntityStore> ref, UICommandBuilder commandBuilder, UIEventBuilder eventBuilder, Store<EntityStore> store)`: Builds either the category view or the memory list view and wires UI events.
- `buildChestMarkers(UICommandBuilder commandBuilder, GameplayConfig gameplayConfig, int totalMemories)`: Adds chest markers along the progress bar for memory levels.
- `handleDataEvent(Ref<EntityStore> ref, Store<EntityStore> store, PageEventData data)`: Handles record, category navigation, and memory selection actions.
- `updateMemoryButtonSelection(UICommandBuilder commandBuilder, int index, Memory memory, boolean isSelected)`: Toggles button visibility and tooltip for memory selection.
- `updateMemoryDetailsPanel(UICommandBuilder commandBuilder, Memory memory)`: Updates detail text, location/time, and icon for the selected memory.

## Usage Notes
- Recording memories triggers particles for nearby players and closes the page once recorded.
- Selection updates are sent as incremental UI command updates to avoid rebuilding the page.

## Examples
```java
MemoriesPage page = new MemoriesPage(playerRef, blockPosition);
```

---

# MemoriesPage.PageEventData

## Overview
Data payload used for page events, including the action, category, and memory ID.

## Field Descriptions
- `KEY_ACTION`: UI key for the action field.
- `KEY_CATEGORY`: UI key for the category field.
- `KEY_MEMORY_ID`: UI key for the memory ID field.
- `CODEC`: Builder codec for event data serialization.
- `action`: Action type for the event.
- `category`: Category name to view.
- `memoryId`: Memory ID to select.

## Constructor Descriptions
- `PageEventData()`: Creates an empty event payload for the codec.

## Method Descriptions
- `PageEventData()`: Holds event data used by the page.

## Examples
```java
MemoriesPage.PageEventData data = new MemoriesPage.PageEventData();
```

---

# MemoriesPage.PageAction

## Overview
Enum of supported page actions for the memories UI.

## Field Descriptions
- `Record`: Record player memories into the global collection.
- `ViewCategory`: Switch to a specific category view.
- `Back`: Return to the category overview.
- `SelectMemory`: Select a memory for detail display.
- `CODEC`: Codec for serializing the enum value.

## Usage Notes
- The enum is serialized via `EnumCodec` for UI event handling.

## Examples
```java
MemoriesPage.PageAction action = MemoriesPage.PageAction.Record;
```
