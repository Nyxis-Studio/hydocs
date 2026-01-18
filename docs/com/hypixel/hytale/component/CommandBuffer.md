# CommandBuffer

## Overview
- Documentation for `CommandBuffer`.
- Declared as a class in `com.hypixel.hytale.component`.

## Constructors
- `CommandBuffer(@Nonnull Store<ECS_TYPE> store)`
  - Creates a `CommandBuffer` instance.

## Methods
- `getStore()`
  - Executes `getStore` behavior.
- `run(@Nonnull Consumer<Store<ECS_TYPE>> consumer)`
  - Executes `run` behavior.
- `getComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `getComponent` behavior.
- `getArchetype(@Nonnull Ref<ECS_TYPE> ref)`
  - Executes `getArchetype` behavior.
- `getResource(@Nonnull ResourceType<ECS_TYPE, T> resourceType)`
  - Executes `getResource` behavior.
- `getExternalData()`
  - Executes `getExternalData` behavior.
- `addEntities(@Nonnull Holder<ECS_TYPE>[] holders, @Nonnull AddReason reason)`
  - Executes `addEntities` behavior.
- `addEntity(@Nonnull Holder<ECS_TYPE> holder, @Nonnull AddReason reason)`
  - Executes `addEntity` behavior.
- `addEntities(@Nonnull Holder<ECS_TYPE>[] holders, int holderStart, @Nonnull Ref<ECS_TYPE>[] refs, int refStart, int length, @Nonnull AddReason reason)`
  - Executes `addEntities` behavior.
- `addEntity(@Nonnull Holder<ECS_TYPE> holder, @Nonnull Ref<ECS_TYPE> ref, @Nonnull AddReason reason)`
  - Executes `addEntity` behavior.
- `copyEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull Holder<ECS_TYPE> target)`
  - Executes `copyEntity` behavior.
- `tryRemoveEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull RemoveReason reason)`
  - Executes `tryRemoveEntity` behavior.
- `removeEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull RemoveReason reason)`
  - Executes `removeEntity` behavior.
- `removeEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull Holder<ECS_TYPE> target, @Nonnull RemoveReason reason)`
  - Executes `removeEntity` behavior.
- `ensureComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `ensureComponent` behavior.
- `ensureAndGetComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `ensureAndGetComponent` behavior.
- `addComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `addComponent` behavior.
- `addComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`
  - Executes `addComponent` behavior.
- `replaceComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`
  - Executes `replaceComponent` behavior.
- `removeComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `removeComponent` behavior.
- `tryRemoveComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `tryRemoveComponent` behavior.
- `putComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`
  - Executes `putComponent` behavior.
- `invoke(@Nonnull Ref<ECS_TYPE> ref, @Nonnull Event param)`
  - Executes `invoke` behavior.
- `invoke(@Nonnull EntityEventType<ECS_TYPE, Event> systemType, @Nonnull Ref<ECS_TYPE> ref, @Nonnull Event param)`
  - Executes `invoke` behavior.
- `invoke(@Nonnull Event param)`
  - Executes `invoke` behavior.
- `invoke(@Nonnull WorldEventType<ECS_TYPE, Event> systemType, @Nonnull Event param)`
  - Executes `invoke` behavior.
- `testRemovedTracked(@Nonnull Ref<ECS_TYPE> ref)`
  - Executes `testRemovedTracked` behavior.
- `fork()`
  - Executes `fork` behavior.
- `mergeParallel(@Nonnull CommandBuffer<ECS_TYPE> commandBuffer)`
  - Executes `mergeParallel` behavior.
- `setThread()`
  - Executes `setThread` behavior.
- `validateEmpty()`
  - Executes `validateEmpty` behavior.

## Notes
- No additional notes.
