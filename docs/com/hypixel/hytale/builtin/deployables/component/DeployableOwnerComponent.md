# DeployableOwnerComponent

## Overview
- Documentation for `DeployableOwnerComponent`.
- Declared as a class in `com.hypixel.hytale.builtin.deployables.component`.

## Constructors
- None.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `getMaxDeployablesForId(@Nonnull DeployableComponent comp)`
  - Executes `getMaxDeployablesForId` behavior.
- `getMaxDeployablesGlobal(@Nonnull Store<EntityStore> store)`
  - Executes `getMaxDeployablesGlobal` behavior.
- `tick(@Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `registerDeployable(@Nonnull Ref<EntityStore> owner, @Nonnull DeployableComponent deployableComp, @Nonnull String id, @Nonnull Ref<EntityStore> deployable, @Nonnull Store<EntityStore> store)`
  - Executes `registerDeployable` behavior.
- `deRegisterDeployable(@Nonnull String id, @Nonnull Ref<EntityStore> deployable)`
  - Executes `deRegisterDeployable` behavior.
- `incrementId(@Nonnull String id)`
  - Executes `incrementId` behavior.
- `decrementId(@Nonnull String id)`
  - Executes `decrementId` behavior.
- `getCurrentDeployablesById(@Nonnull String id)`
  - Executes `getCurrentDeployablesById` behavior.
- `handlePerDeployableLimit(@Nonnull String id, @Nonnull DeployableComponent deployableComponent)`
  - Executes `handlePerDeployableLimit` behavior.
- `handleGlobalDeployableLimit(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> owner)`
  - Executes `handleGlobalDeployableLimit` behavior.
- `handleOverMaxDeployableDestruction(@Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `handleOverMaxDeployableDestruction` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
