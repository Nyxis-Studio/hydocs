# EntityFilterNot

## Overview
- Documentation for `EntityFilterNot`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.entity.filters`.

## Constructors
- `EntityFilterNot(IEntityFilter filter)`
  - Creates a `EntityFilterNot` instance.

## Methods
- `matchesEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store)`
  - Executes `matchesEntity` behavior.
- `cost()`
  - Executes `cost` behavior.
- `registerWithSupport(Role role)`
  - Executes `registerWithSupport` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `motionControllerChanged` behavior.
- `loaded(Role role)`
  - Executes `loaded` behavior.
- `spawned(Role role)`
  - Executes `spawned` behavior.
- `unloaded(Role role)`
  - Executes `unloaded` behavior.
- `removed(Role role)`
  - Executes `removed` behavior.
- `teleported(Role role, World from, World to)`
  - Executes `teleported` behavior.
- `componentCount()`
  - Executes `componentCount` behavior.
- `getComponent(int index)`
  - Executes `getComponent` behavior.
- `setContext(IAnnotatedComponent parent, int index)`
  - Executes `setContext` behavior.

## Notes
- No additional notes.
