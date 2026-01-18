# Holder

## Overview
- Documentation for `Holder`.
- Declared as a class in `com.hypixel.hytale.component`.

## Constructors
- `Holder()`
  - Creates a `Holder` instance.
- `Holder(@Nonnull ComponentRegistry<ECS_TYPE> registry)`
  - Creates a `Holder` instance.
- `Holder(@Nonnull ComponentRegistry<ECS_TYPE> registry, @Nonnull Archetype<ECS_TYPE> archetype, @Nonnull Component<ECS_TYPE>[] components)`
  - Creates a `Holder` instance.

## Methods
- `emptyArray()`
  - Executes `emptyArray` behavior.
- `ensureComponentsSize(int size)`
  - Executes `ensureComponentsSize` behavior.
- `init(@Nonnull Archetype<ECS_TYPE> archetype, @Nonnull Component<ECS_TYPE>[] components)`
  - Executes `init` behavior.
- `_internal_init(@Nonnull Archetype<ECS_TYPE> archetype, @Nonnull Component<ECS_TYPE>[] components, @Nonnull ComponentType<ECS_TYPE, UnknownComponents<ECS_TYPE>> unknownComponentType)`
  - Executes `_internal_init` behavior.
- `getArchetype()`
  - Executes `getArchetype` behavior.
- `ensureComponent(@Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `ensureComponent` behavior.
- `ensureAndGetComponent(@Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `ensureAndGetComponent` behavior.
- `addComponent(@Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`
  - Executes `addComponent` behavior.
- `addComponent0(@Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`
  - Executes `addComponent0` behavior.
- `replaceComponent(@Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`
  - Executes `replaceComponent` behavior.
- `putComponent(@Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`
  - Executes `putComponent` behavior.
- `getComponent(@Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `getComponent` behavior.
- `removeComponent(@Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `removeComponent` behavior.
- `tryRemoveComponent(@Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `tryRemoveComponent` behavior.
- `hasSerializableComponents(@Nonnull ComponentRegistry.Data<ECS_TYPE> data)`
  - Executes `hasSerializableComponents` behavior.
- `updateData(@Nonnull ComponentRegistry.Data<ECS_TYPE> oldData, @Nonnull ComponentRegistry.Data<ECS_TYPE> newData)`
  - Executes `updateData` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(@Nullable Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
