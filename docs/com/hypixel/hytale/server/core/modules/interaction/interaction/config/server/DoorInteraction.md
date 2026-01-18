# DoorInteraction

## Overview
- Documentation for `DoorInteraction`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.server`.

## Constructors
- None.

## Methods
- `interactWithBlock(@Nonnull World world, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull Vector3i targetBlock, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `interactWithBlock` behavior.
- `simulateInteractWithBlock(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull World world, @Nonnull Vector3i targetBlock)`
  - Executes `simulateInteractWithBlock` behavior.
- `checkForDoubleDoor(@Nonnull World world, @Nonnull Vector3i blockPosition, @Nonnull BlockType blockType, int rotation, @Nonnull DoorState fromState, @Nonnull DoorState doorStateToCheck)`
  - Executes `checkForDoubleDoor` behavior.
- `isHorizontalDoor(@Nonnull BlockType blockType)`
  - Executes `isHorizontalDoor` behavior.
- `checkDoor(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, @Nonnull Vector3i blockPosition, @Nonnull BlockType blockType, int rotation, @Nonnull DoorState oldDoorState, @Nonnull DoorState newDoorState)`
  - Executes `checkDoor` behavior.
- `activateDoor(@Nonnull World world, @Nonnull BlockType blockType, @Nonnull Vector3i blockPosition, @Nonnull DoorState fromState, @Nonnull DoorState doorState)`
  - Executes `activateDoor` behavior.
- `getDoubleDoor(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, @Nonnull Vector3i worldPosition, @Nonnull BlockType blockType, int rotation, @Nonnull DoorState doorStateToCheck)`
  - Executes `getDoubleDoor` behavior.
- `getDoorAtPosition(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, int x, int y, int z, @Nonnull Rotation rotationToCheck)`
  - Executes `getDoorAtPosition` behavior.
- `canOpenDoor(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, @Nonnull Vector3i blockPosition, @Nonnull String state)`
  - Executes `canOpenDoor` behavior.
- `isInFrontOfDoor(@Nonnull Vector3i blockPosition, @Nullable Rotation doorRotationYaw, @Nonnull Vector3d playerPosition)`
  - Executes `isInFrontOfDoor` behavior.
- `getInteractionState(@Nonnull DoorState fromState, @Nonnull DoorState doorState)`
  - Executes `getInteractionState` behavior.
- `getOppositeDoorState(@Nonnull DoorState doorState)`
  - Executes `getOppositeDoorState` behavior.
- `fromBlockState(@Nullable String state)`
  - Executes `fromBlockState` behavior.
- `getBlockType()`
  - Executes `getBlockType` behavior.
- `getBlockPosition()`
  - Executes `getBlockPosition` behavior.
- `getDoorState()`
  - Executes `getDoorState` behavior.

## Notes
- No additional notes.
