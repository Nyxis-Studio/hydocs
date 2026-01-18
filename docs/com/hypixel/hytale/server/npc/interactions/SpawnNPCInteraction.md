# SpawnNPCInteraction

## Overview
- Documentation for `SpawnNPCInteraction`.
- Declared as a class in `com.hypixel.hytale.server.npc.interactions`.

## Constructors
- None.

## Methods
- `spawnNPC(@Nonnull Store<EntityStore> store, @Nonnull Vector3i targetBlock)`
  - Executes `spawnNPC` behavior.
- `computeSpawnData(@Nonnull World world, @Nonnull Vector3i targetBlock)`
  - Executes `computeSpawnData` behavior.
- `interactWithBlock(@Nonnull World world, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull Vector3i targetBlock, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `interactWithBlock` behavior.
- `simulateInteractWithBlock(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull World world, @Nonnull Vector3i targetBlock)`
  - Executes `simulateInteractWithBlock` behavior.
- `SpawnData(@Nonnull Vector3d position, @Nonnull Vector3f rotation)`
  - Executes `SpawnData` behavior.

## Notes
- No additional notes.
