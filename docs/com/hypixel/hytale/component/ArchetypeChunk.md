# ArchetypeChunk

## Overview
- Documentation for `ArchetypeChunk`.
- Declared as a class in `com.hypixel.hytale.component`.

## Constructors
- `ArchetypeChunk(@Nonnull Store<ECS_TYPE> store, @Nonnull Archetype<ECS_TYPE> archetype)`
  - Creates a `ArchetypeChunk` instance.

## Methods
- `emptyArray()`
  - Executes `emptyArray` behavior.
- `getArchetype()`
  - Executes `getArchetype` behavior.
- `size()`
  - Executes `size` behavior.
- `getReferenceTo(int index)`
  - Executes `getReferenceTo` behavior.
- `setComponent(int index, @Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`
  - Executes `setComponent` behavior.
- `getComponent(int index, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `getComponent` behavior.
- `addEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull Holder<ECS_TYPE> holder)`
  - Executes `addEntity` behavior.
- `copyEntity(int entityIndex, @Nonnull Holder<ECS_TYPE> target)`
  - Executes `copyEntity` behavior.
- `copySerializableEntity(@Nonnull ComponentRegistry.Data<ECS_TYPE> data, int entityIndex, @Nonnull Holder<ECS_TYPE> target)`
  - Executes `copySerializableEntity` behavior.
- `removeEntity(int entityIndex, @Nonnull Holder<ECS_TYPE> target)`
  - Executes `removeEntity` behavior.
- `transferTo(@Nonnull Holder<ECS_TYPE> tempInternalEntityHolder, @Nonnull ArchetypeChunk<ECS_TYPE> chunk, @Nonnull Consumer<Holder<ECS_TYPE>> modification, @Nonnull IntObjectConsumer<Ref<ECS_TYPE>> referenceConsumer)`
  - Executes `transferTo` behavior.
- `transferSomeTo(@Nonnull Holder<ECS_TYPE> tempInternalEntityHolder, @Nonnull ArchetypeChunk<ECS_TYPE> chunk, @Nonnull IntPredicate shouldTransfer, @Nonnull Consumer<Holder<ECS_TYPE>> modification, @Nonnull IntObjectConsumer<Ref<ECS_TYPE>> referenceConsumer)`
  - Executes `transferSomeTo` behavior.
- `fillEmptyIndex(int entityIndex, int lastIndex)`
  - Executes `fillEmptyIndex` behavior.
- `appendDump(@Nonnull String prefix, @Nonnull StringBuilder sb)`
  - Executes `appendDump` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
