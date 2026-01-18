# DeployablesUtils

## Overview
- Documentation for `DeployablesUtils`.
- Declared as a class in `com.hypixel.hytale.builtin.deployables`.

## Constructors
- None.

## Methods
- `spawnDeployable(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Store<EntityStore> store, @Nonnull DeployableConfig config, @Nonnull Ref<EntityStore> deployerRef, @Nonnull Vector3f position, @Nonnull Vector3f rotation, @Nonnull String spawnFace)`
  - Executes `spawnDeployable` behavior.
- `populateStats(@Nonnull DeployableConfig config, @Nonnull EntityStatMap entityStatMapComponent)`
  - Executes `populateStats` behavior.
- `playAnimation(@Nonnull Store<EntityStore> store, int networkId, @Nonnull Ref<EntityStore> ref, @Nonnull DeployableConfig config, @Nonnull AnimationSlot animationSlot, @Nullable String itemAnimationsId, @Nonnull String animationId)`
  - Executes `playAnimation` behavior.
- `stopAnimation(@Nonnull Store<EntityStore> store, int networkId, @Nonnull Ref<EntityStore> ref, @Nonnull AnimationSlot animationSlot)`
  - Executes `stopAnimation` behavior.
- `playSoundEventsAtEntity(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor, int localIndex, int worldIndex, @Nonnull Vector3d pos)`
  - Executes `playSoundEventsAtEntity` behavior.

## Notes
- No additional notes.
