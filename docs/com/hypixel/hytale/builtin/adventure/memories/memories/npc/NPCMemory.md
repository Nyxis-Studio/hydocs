**Source Hash:** `51b74fff4a454d5e4ce67ca6c648325929a7d5075885900e9b4a2020b4f59298`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# NPCMemory

## Overview
Memory entry representing a discovered NPC. Stores NPC role identifiers, capture time, and location keys, and provides tooltip and icon metadata for the memories UI.

## Field Descriptions
- `ID`: Memory provider identifier for NPC memories.
- `CODEC`: Builder codec for NPC memory serialization.
- `npcRole`: Role or memory ID for the NPC.
- `isMemoriesNameOverridden`: Whether the NPC name should be overridden in the memories UI.
- `capturedTimestamp`: Timestamp when the memory was captured.
- `foundLocationZoneNameKey`: Zone translation key where the NPC was found.
- `foundLocationGeneralNameKey`: General location translation key, if provided.
- `memoryTitleKey`: Translation key for the memory title.

## Constructor Descriptions
- `NPCMemory()`: Creates an empty memory instance for codec use.
- `NPCMemory(String npcRole, String nameTranslationKey, boolean isMemoriesNameOverridden)`: Creates a memory entry and applies name override processing.

## Method Descriptions
- `getId()`: Returns the NPC role identifier.
- `getTitle()`: Returns the translation key for the memory title.
- `getTooltipText()`: Returns the tooltip for discovered memories.
- `getIconPath()`: Returns the NPC memory icon path.
- `processConfig()`: Updates the memory title key based on override rules and localization fallback.
- `getUndiscoveredTooltipText()`: Returns the tooltip for undiscovered memories.
- `getNpcRole()`: Returns the NPC role identifier.
- `getCapturedTimestamp()`: Returns the capture timestamp in milliseconds.
- `getFoundLocationZoneNameKey()`: Returns the zone translation key.
- `getLocationMessage()`: Returns a translated location message or "???" when unknown.
- `equals(Object o)`: Compares memories by role and override state.
- `hashCode()`: Hashes the role and override state.
- `toString()`: Returns a debug string.

## Usage Notes
- `processConfig` should run after setting role and override flags to keep title keys consistent.

## Examples
```java
NPCMemory memory = new NPCMemory("npc_role", "server.npcRoles.npc_role.name", false);
```
