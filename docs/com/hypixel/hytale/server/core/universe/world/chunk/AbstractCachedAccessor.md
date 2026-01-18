# AbstractCachedAccessor

## Overview
- Documentation for `AbstractCachedAccessor`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk`.

## Constructors
- `AbstractCachedAccessor(int numComponents)`
  - Creates a `AbstractCachedAccessor` instance.

## Methods
- `init(ComponentAccessor<ChunkStore> commandBuffer, int cx, int cy, int cz, int radius)`
  - Executes `init` behavior.
- `insertSection(Ref<ChunkStore> section, int cx, int cy, int cz)`
  - Executes `insertSection` behavior.
- `insertSectionComponent(int index, Component<ChunkStore> component, int cx, int cy, int cz)`
  - Executes `insertSectionComponent` behavior.
- `getChunk(int cx, int cz)`
  - Executes `getChunk` behavior.
- `getSection(int cx, int cy, int cz)`
  - Executes `getSection` behavior.
- `getComponentSection(int cx, int cy, int cz, int typeIndex, @Nonnull ComponentType<ChunkStore, T> componentType)`
  - Executes `getComponentSection` behavior.

## Notes
- No additional notes.
