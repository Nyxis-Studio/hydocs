# Archetype

## Overview
- Documentation for `Archetype`.
- Declared as a class in `com.hypixel.hytale.component`.

## Constructors
- `Archetype(0, 0, ComponentType.EMPTY_ARRAY)`
  - Creates a `Archetype` instance.
- `Archetype(int minIndex, int count, @Nonnull ComponentType<ECS_TYPE, ?>[] componentTypes)`
  - Creates a `Archetype` instance.

## Methods
- `empty()`
  - Executes `empty` behavior.
- `getMinIndex()`
  - Executes `getMinIndex` behavior.
- `count()`
  - Executes `count` behavior.
- `length()`
  - Executes `length` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `contains(@Nonnull ComponentType<ECS_TYPE, ?> componentType)`
  - Executes `contains` behavior.
- `contains(@Nonnull Archetype<ECS_TYPE> archetype)`
  - Executes `contains` behavior.
- `validateComponentType(@Nonnull ComponentType<ECS_TYPE, ?> componentType)`
  - Executes `validateComponentType` behavior.
- `validateComponents(@Nonnull Component<ECS_TYPE>[] components, @Nullable ComponentType<ECS_TYPE, UnknownComponents<ECS_TYPE>> ignore)`
  - Executes `validateComponents` behavior.
- `hasSerializableComponents(@Nonnull ComponentRegistry.Data<ECS_TYPE> data)`
  - Executes `hasSerializableComponents` behavior.
- `getSerializableArchetype(@Nonnull ComponentRegistry.Data<ECS_TYPE> data)`
  - Executes `getSerializableArchetype` behavior.
- `asExactQuery()`
  - Executes `asExactQuery` behavior.
- `of(@Nonnull ComponentType<ECS_TYPE, ?> componentTypes)`
  - Executes `of` behavior.
- `of(ComponentType<ECS_TYPE, ?> ... componentTypes)`
  - Executes `of` behavior.
- `add(@Nonnull Archetype<ECS_TYPE> archetype, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `add` behavior.
- `remove(@Nonnull Archetype<ECS_TYPE> archetype, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `remove` behavior.
- `test(@Nonnull Archetype<ECS_TYPE> archetype)`
  - Executes `test` behavior.
- `requiresComponentType(@Nonnull ComponentType<ECS_TYPE, ?> componentType)`
  - Executes `requiresComponentType` behavior.
- `validateRegistry(ComponentRegistry<ECS_TYPE> registry)`
  - Executes `validateRegistry` behavior.
- `validate()`
  - Executes `validate` behavior.
- `equals(@Nullable Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
