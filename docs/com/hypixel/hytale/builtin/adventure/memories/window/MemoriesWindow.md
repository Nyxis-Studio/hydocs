**Source Hash:** `0f37e7e1215b460b6179a12a752f8df0d76176449b5270b89e03b1c50250327a`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesWindow

## Overview
Server-side window that packages player memory data into JSON for the memories UI. Populates memory entries with title, tooltip, icon, and category icon where available.

## Field Descriptions
- `windowData`: JSON payload sent to the client when the window opens.

## Constructor Descriptions
- `MemoriesWindow()`: Creates the memories window for the `Memories` window type.

## Method Descriptions
- `getData()`: Returns the window JSON payload.
- `onOpen0()`: Populates the window data with capacity and memory entries, then invalidates the window.
- `GetCategoryIconPathForMemory(Memory memory)`: Finds the category icon path for a given memory.
- `onClose0()`: No-op close handler.

## Usage Notes
- The window sets capacity to zero when the player lacks the `PlayerMemories` component.

## Examples
```java
MemoriesWindow window = new MemoriesWindow();
```
