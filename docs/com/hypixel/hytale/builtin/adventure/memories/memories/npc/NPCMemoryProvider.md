**Source Hash:** `319840a6ffb528ebccf36bec5269fc958328fb2aee0c817e4a07c69b2562de95`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# NPCMemoryProvider

## Overview
Memory provider that derives NPC memories from registered NPC builders. Filters valid, spawnable, non-deprecated NPCs and groups them by configured memories category.

## Field Descriptions
- `DEFAULT_RADIUS`: Default collection radius for NPC memories.

## Constructor Descriptions
- `NPCMemoryProvider()`: Registers the NPC memory provider with default radius and codec.

## Method Descriptions
- `getAllMemories()`: Builds the category map of NPC memories, logging failures per builder.
- `getCategory(Builder<?> builder)`: Returns the memories category for a spawnable NPC or "Other".
- `isMemory(Builder<?> builder)`: Returns whether the NPC should appear in memories.
- `getMemoriesNameOverride(Builder<?> builder)`: Returns a name override for the memory entry, if any.
- `getNPCNameTranslationKey(Builder<?> builder)`: Returns the translation key for the NPC display name.

## Usage Notes
- Builders marked as deprecated or invalid are skipped when generating memories.

## Examples
```java
NPCMemoryProvider provider = new NPCMemoryProvider();
```
