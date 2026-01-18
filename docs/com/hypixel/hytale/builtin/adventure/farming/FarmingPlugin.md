# FarmingPlugin

**Overview**
Plugin that registers farming assets, codecs, components, and systems.
Sets up growth modifiers, farming stage data, interactions, and coop components.

**Constructors**
- `FarmingPlugin(JavaPluginInit init)`: initializes the plugin.

**Methods**
- `setup()`: registers asset stores, codecs, components, and systems.
- `getTiledSoilBlockComponentType()`: returns the tilled soil component type.
- `getFarmingBlockComponentType()`: returns the farming block component type.
- `getFarmingBlockStateComponentType()`: returns the legacy farming state component type.
- `getCoopBlockStateComponentType()`: returns the coop block component type.
- `getCoopResidentComponentType()`: returns the coop resident component type.

**Notes**
- Prevents spread on newly generated chunks via `preventSpreadOnNew`.
