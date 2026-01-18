**Source Hash:** `431687e73e956963d0db62de7647f7dfd6630e97956206799c0d39329b0c382d`

# CommandBuffer

## Overview

## Constructor Descriptions
- `CommandBuffer(@Nonnull Store<ECS_TYPE> store)`
  - Creates a `CommandBuffer` instance.

## Method Descriptions
- `getStore()`: Add description.
  - Executes `getStore` behavior.
- `run(@Nonnull Consumer<Store<ECS_TYPE>> consumer)`: Add description.
  - Executes `run` behavior.
- `getComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `getComponent` behavior.
- `getArchetype(@Nonnull Ref<ECS_TYPE> ref)`: Add description.
  - Executes `getArchetype` behavior.
- `getResource(@Nonnull ResourceType<ECS_TYPE, T> resourceType)`: Add description.
  - Executes `getResource` behavior.
- `getExternalData()`: Add description.
  - Executes `getExternalData` behavior.
- `addEntities(@Nonnull Holder<ECS_TYPE>[] holders, @Nonnull AddReason reason)`: Add description.
  - Executes `addEntities` behavior.
- `addEntity(@Nonnull Holder<ECS_TYPE> holder, @Nonnull AddReason reason)`: Add description.
  - Executes `addEntity` behavior.
- `addEntities(@Nonnull Holder<ECS_TYPE>[] holders, int holderStart, @Nonnull Ref<ECS_TYPE>[] refs, int refStart, int length, @Nonnull AddReason reason)`: Add description.
  - Executes `addEntities` behavior.
- `addEntity(@Nonnull Holder<ECS_TYPE> holder, @Nonnull Ref<ECS_TYPE> ref, @Nonnull AddReason reason)`: Add description.
  - Executes `addEntity` behavior.
- `copyEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull Holder<ECS_TYPE> target)`: Add description.
  - Executes `copyEntity` behavior.
- `tryRemoveEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull RemoveReason reason)`: Add description.
  - Executes `tryRemoveEntity` behavior.
- `removeEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull RemoveReason reason)`: Add description.
  - Executes `removeEntity` behavior.
- `removeEntity(@Nonnull Ref<ECS_TYPE> ref, @Nonnull Holder<ECS_TYPE> target, @Nonnull RemoveReason reason)`: Add description.
  - Executes `removeEntity` behavior.
- `ensureComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `ensureComponent` behavior.
- `ensureAndGetComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `ensureAndGetComponent` behavior.
- `addComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `addComponent` behavior.
- `addComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`: Add description.
  - Executes `addComponent` behavior.
- `replaceComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`: Add description.
  - Executes `replaceComponent` behavior.
- `removeComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `removeComponent` behavior.
- `tryRemoveComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `tryRemoveComponent` behavior.
- `putComponent(@Nonnull Ref<ECS_TYPE> ref, @Nonnull ComponentType<ECS_TYPE, T> componentType, @Nonnull T component)`: Add description.
  - Executes `putComponent` behavior.
- `invoke(@Nonnull Ref<ECS_TYPE> ref, @Nonnull Event param)`: Add description.
  - Executes `invoke` behavior.
- `invoke(@Nonnull EntityEventType<ECS_TYPE, Event> systemType, @Nonnull Ref<ECS_TYPE> ref, @Nonnull Event param)`: Add description.
  - Executes `invoke` behavior.
- `invoke(@Nonnull Event param)`: Add description.
  - Executes `invoke` behavior.
- `invoke(@Nonnull WorldEventType<ECS_TYPE, Event> systemType, @Nonnull Event param)`: Add description.
  - Executes `invoke` behavior.
- `testRemovedTracked(@Nonnull Ref<ECS_TYPE> ref)`: Add description.
  - Executes `testRemovedTracked` behavior.
- `fork()`: Add description.
  - Executes `fork` behavior.
- `mergeParallel(@Nonnull CommandBuffer<ECS_TYPE> commandBuffer)`: Add description.
  - Executes `mergeParallel` behavior.
- `setThread()`: Add description.
  - Executes `setThread` behavior.
- `validateEmpty()`: Add description.
  - Executes `validateEmpty` behavior.

## Notes
- No additional notes.
