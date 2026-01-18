**Source Hash:** `4d9dd79020c3740f322c693494c39b7267fb785e33277e2f7e50ba718650abc7`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# Memory

## Overview
Abstract base class for a collectible memory entry. Defines the ID, title, tooltip text, icon, and undiscovered tooltip used in memories UI and comparisons.

## Field Descriptions
- `CODEC`: Codec registry used to serialize and resolve memory subtypes.

## Constructor Descriptions
- `Memory()`: Base constructor for memory implementations.

## Method Descriptions
- `getId()`: Returns the unique memory identifier.
- `getTitle()`: Returns the translation key for the memory title.
- `getTooltipText()`: Returns the tooltip message shown for discovered memories.
- `getIconPath()`: Returns the icon asset path, or null if none is defined.
- `getUndiscoveredTooltipText()`: Returns the tooltip message shown for undiscovered memories.
- `equals(Object o)`: Compares memories by class identity.
- `hashCode()`: Returns a hash based on the memory class.
- `toString()`: Returns a basic debug string.

## Usage Notes
- Concrete subclasses should implement title and tooltip text to drive UI display.

## Examples
```java
Memory memory = new NPCMemory();
```
