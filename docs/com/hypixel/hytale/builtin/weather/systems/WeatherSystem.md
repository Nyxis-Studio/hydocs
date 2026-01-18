# WeatherSystem

## Overview
- Documentation for `WeatherSystem`.
- Declared as a class in `com.hypixel.hytale.builtin.weather.systems`.

## Constructors
- None.

## Methods
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@NonNullDecl Ref<EntityStore> ref, @NonNullDecl Teleport component, @NonNullDecl Store<EntityStore> store, @NonNullDecl CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@NonNullDecl Ref<EntityStore> ref, @NullableDecl Teleport oldComponent, @NonNullDecl Teleport newComponent, @NonNullDecl Store<EntityStore> store, @NonNullDecl CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@NonNullDecl Ref<EntityStore> ref, @NonNullDecl Teleport component, @NonNullDecl Store<EntityStore> store, @NonNullDecl CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.
- `onSystemAddedToStore(@Nonnull Store<EntityStore> store)`
  - Executes `onSystemAddedToStore` behavior.
- `onSystemRemovedFromStore(@Nonnull Store<EntityStore> store)`
  - Executes `onSystemRemovedFromStore` behavior.

## Notes
- No additional notes.
