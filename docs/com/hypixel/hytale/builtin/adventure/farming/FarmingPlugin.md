**Source Hash:** `8f6689733738dd9628add741707b024fcf33e22401083fff3a6d9177c9738fac`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# FarmingPlugin

## Overview
Plugin that registers farming assets, codecs, components, and systems. Sets up growth modifiers, farming stage data, interactions, and coop components.

## Field Descriptions
- `instance`: Singleton instance for access via `get()`.
- `tiledSoilBlockComponentType`: Chunk component type for tilled soil blocks.
- `farmingBlockComponentType`: Chunk component type for farming blocks.
- `farmingBlockStateComponentType`: Legacy farming state component type.
- `coopBlockStateComponentType`: Chunk component type for coop blocks.
- `coopResidentComponentType`: Entity component type for coop residents.

## Constructor Descriptions
- `FarmingPlugin(JavaPluginInit init)`: Initializes the plugin with the provided plugin context.

## Method Descriptions
- `get()`: Returns the singleton plugin instance.
- `setup()`: Registers asset stores, codecs, components, systems, and event hooks for farming.
- `getTiledSoilBlockComponentType()`: Returns the tilled soil component type.
- `getFarmingBlockComponentType()`: Returns the farming block component type.
- `getFarmingBlockStateComponentType()`: Returns the legacy farming state component type.
- `getCoopBlockStateComponentType()`: Returns the coop block component type.
- `getCoopResidentComponentType()`: Returns the coop resident component type.

## Usage Notes
- `preventSpreadOnNew` disables spread rates for newly generated chunks.

## Examples
```java
FarmingPlugin plugin = FarmingPlugin.get();
```
