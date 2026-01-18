**Source Hash:** `031030f341f7772a23f8524325ad86c7bf85078b3cbd789d1b1521eb8e71a769`

# ArchetypeChunk

## Overview

## Constructor Descriptions
- `ArchetypeChunk(@Nonnull Store<ECS_TYPE> store, @Nonnull Archetype<ECS_TYPE> archetype)`
  - Creates a `ArchetypeChunk` instance.

## Method Descriptions
- `emptyArray()`: Add description.
  - Executes `emptyArray` behavior.
- `getArchetype()`: Add description.
  - Executes `getArchetype` behavior.
- `size()`: Add description.
  - Executes `size` behavior.
- `getReferenceTo(int index)`: Add description.
  - Executes `getReferenceTo` behavior.
- `setComponent(int index, @Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`: Add description.
  - Executes `setComponent` behavior.
- `getComponent(int index, @Nonnull ComponentType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `getComponent` behavior.
- `addEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull Holder<ECS_TYPE> holder)`: Add description.
  - Executes `addEntity` behavior.
- `copyEntity(int entityIndex, @Nonnull Holder<ECS_TYPE> target)`: Add description.
  - Executes `copyEntity` behavior.
- `copySerializableEntity(@Nonnull ComponentRegistry.Data<ECS_TYPE> data, int entityIndex, @Nonnull Holder<ECS_TYPE> target)`: Add description.
  - Executes `copySerializableEntity` behavior.
- `removeEntity(int entityIndex, @Nonnull Holder<ECS_TYPE> target)`: Add description.
  - Executes `removeEntity` behavior.
- `transferTo(@Nonnull Holder<ECS_TYPE> tempInternalEntityHolder, @Nonnull ArchetypeChunk<ECS_TYPE> chunk, @Nonnull Consumer<Holder<ECS_TYPE>> modification, @Nonnull IntObjectConsumer<Ref<ECS_TYPE>> referenceConsumer)`: Add description.
  - Executes `transferTo` behavior.
- `transferSomeTo(@Nonnull Holder<ECS_TYPE> tempInternalEntityHolder, @Nonnull ArchetypeChunk<ECS_TYPE> chunk, @Nonnull IntPredicate shouldTransfer, @Nonnull Consumer<Holder<ECS_TYPE>> modification, @Nonnull IntObjectConsumer<Ref<ECS_TYPE>> referenceConsumer)`: Add description.
  - Executes `transferSomeTo` behavior.
- `fillEmptyIndex(int entityIndex, int lastIndex)`: Add description.
  - Executes `fillEmptyIndex` behavior.
- `appendDump(@Nonnull String prefix, @Nonnull StringBuilder sb)`: Add description.
  - Executes `appendDump` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
