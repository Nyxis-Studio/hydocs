# ComponentAccessor

## Overview
- Documentation for `ComponentAccessor`.
- Declared as a interface in `com.hypixel.hytale.component`.

## Constructors
- None.

## Methods
- `getComponent(@Nonnull Ref<ECS_TYPE> var1, @Nonnull ComponentType<ECS_TYPE, T> var2)`
  - Executes `getComponent` behavior.
- `ensureAndGetComponent(@Nonnull Ref<ECS_TYPE> var1, @Nonnull ComponentType<ECS_TYPE, T> var2)`
  - Executes `ensureAndGetComponent` behavior.
- `getArchetype(@Nonnull Ref<ECS_TYPE> var1)`
  - Executes `getArchetype` behavior.
- `getResource(@Nonnull ResourceType<ECS_TYPE, T> var1)`
  - Executes `getResource` behavior.
- `getExternalData()`
  - Executes `getExternalData` behavior.
- `putComponent(@Nonnull Ref<ECS_TYPE> var1, @Nonnull ComponentType<ECS_TYPE, T> var2, @Nonnull T var3)`
  - Executes `putComponent` behavior.
- `addComponent(@Nonnull Ref<ECS_TYPE> var1, @Nonnull ComponentType<ECS_TYPE, T> var2, @Nonnull T var3)`
  - Executes `addComponent` behavior.
- `addComponent(@Nonnull Ref<ECS_TYPE> var1, @Nonnull ComponentType<ECS_TYPE, T> var2)`
  - Executes `addComponent` behavior.
- `addEntities(@Nonnull Holder<ECS_TYPE>[] var1, @Nonnull AddReason var2)`
  - Executes `addEntities` behavior.
- `addEntity(@Nonnull Holder<ECS_TYPE> var1, @Nonnull AddReason var2)`
  - Executes `addEntity` behavior.
- `removeEntity(@Nonnull Ref<ECS_TYPE> var1, @Nonnull Holder<ECS_TYPE> var2, @Nonnull RemoveReason var3)`
  - Executes `removeEntity` behavior.
- `removeComponent(@Nonnull Ref<ECS_TYPE> var1, @Nonnull ComponentType<ECS_TYPE, T> var2)`
  - Executes `removeComponent` behavior.
- `tryRemoveComponent(@Nonnull Ref<ECS_TYPE> var1, @Nonnull ComponentType<ECS_TYPE, T> var2)`
  - Executes `tryRemoveComponent` behavior.
- `invoke(@Nonnull Ref<ECS_TYPE> var1, @Nonnull Event var2)`
  - Executes `invoke` behavior.
- `invoke(@Nonnull EntityEventType<ECS_TYPE, Event> var1, @Nonnull Ref<ECS_TYPE> var2, @Nonnull Event var3)`
  - Executes `invoke` behavior.
- `invoke(@Nonnull Event var1)`
  - Executes `invoke` behavior.
- `invoke(@Nonnull WorldEventType<ECS_TYPE, Event> var1, @Nonnull Event var2)`
  - Executes `invoke` behavior.

## Notes
- No additional notes.
