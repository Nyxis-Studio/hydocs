**Source Hash:** `edcd52f411b149fe85c9bccae18d67ffb3db6db3e90d6e332193017b96308ee1`
**Last Updated:** 2026-01-18T18:54:44-03:00

# NPCShopPlugin

## Overview

Plugin that provides NPC shop functionality for adventure mode. Registers NPC component types for opening regular shops and barter shops, enabling NPCs to act as merchants with different trading interfaces.

## Constructor Descriptions
- `NPCShopPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `NPCShopPlugin` instance with the provided initialization context.

## Method Descriptions
- `setup()`: Initializes the NPC shop system.
  - Registers "OpenShop" component type with `BuilderActionOpenShop` for standard shop interfaces.
  - Registers "OpenBarterShop" component type with `BuilderActionOpenBarterShop` for barter trading interfaces.

## Notes
- Depends on NPCPlugin for component registration.
- Supports both traditional shops and barter-based trading systems.
