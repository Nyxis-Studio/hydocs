# EntitySupport

## Overview
- Documentation for `EntitySupport`.
- Declared as a class in `com.hypixel.hytale.server.npc.role.support`.

## Constructors
- `EntitySupport(NPCEntity parent, @Nonnull BuilderRole builder)`
  - Creates a `EntitySupport` instance.

## Methods
- `getSensorScope()`
  - Executes `getSensorScope` behavior.
- `getNextBodyMotionStep()`
  - Executes `getNextBodyMotionStep` behavior.
- `setNextBodyMotionStep(Instruction step)`
  - Executes `setNextBodyMotionStep` behavior.
- `clearNextBodyMotionStep()`
  - Executes `clearNextBodyMotionStep` behavior.
- `getNextHeadMotionStep()`
  - Executes `getNextHeadMotionStep` behavior.
- `setNextHeadMotionStep(Instruction step)`
  - Executes `setNextHeadMotionStep` behavior.
- `clearNextHeadMotionStep()`
  - Executes `clearNextHeadMotionStep` behavior.
- `postRoleBuilt(@Nonnull BuilderSupport builderSupport)`
  - Executes `postRoleBuilt` behavior.
- `tick(float dt)`
  - Executes `tick` behavior.
- `handleNominatedDisplayName(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `handleNominatedDisplayName` behavior.
- `nominateDisplayName(@Nonnull String displayName)`
  - Executes `nominateDisplayName` behavior.
- `pickRandomDisplayName(@Nonnull Holder<EntityStore> holder, boolean override)`
  - Executes `pickRandomDisplayName` behavior.
- `setDisplayName(@Nonnull Holder<EntityStore> holder, @Nonnull String displayName)`
  - Executes `setDisplayName` behavior.
- `setDisplayName(@Nonnull Holder<EntityStore> holder, @Nullable String displayName, boolean override)`
  - Executes `setDisplayName` behavior.
- `pickRandomDisplayName(@Nonnull Ref<EntityStore> ref, boolean override, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `pickRandomDisplayName` behavior.
- `setRandomDisplayName(@Nonnull Ref<EntityStore> ref, @Nullable String[] names, boolean override, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setRandomDisplayName` behavior.
- `setDisplayName(@Nonnull Ref<EntityStore> ref, @Nonnull String displayName, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setDisplayName` behavior.
- `setDisplayName(@Nonnull Ref<EntityStore> ref, @Nullable String displayName, boolean override, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setDisplayName` behavior.
- `addTargetPlayerActiveTask(@Nonnull String task)`
  - Executes `addTargetPlayerActiveTask` behavior.
- `clearTargetPlayerActiveTasks()`
  - Executes `clearTargetPlayerActiveTasks` behavior.
- `getTargetPlayerActiveTasks()`
  - Executes `getTargetPlayerActiveTasks` behavior.
- `registerDelay(@Nonnull IComponentExecutionControl component)`
  - Executes `registerDelay` behavior.
- `createScope(@Nonnull NPCEntity entity)`
  - Executes `createScope` behavior.

## Notes
- No additional notes.
