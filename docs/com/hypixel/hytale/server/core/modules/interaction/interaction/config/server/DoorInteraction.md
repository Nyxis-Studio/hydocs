**Source Hash:** `58a36ddb34596ee0e7eb98d68b55420b1e59ab75ab1411ff43faf74169d2b421`

# DoorInteraction

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `interactWithBlock(@Nonnull World world, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull Vector3i targetBlock, @Nonnull CooldownHandler cooldownHandler)`: Add description.
  - Executes `interactWithBlock` behavior.
- `simulateInteractWithBlock(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull World world, @Nonnull Vector3i targetBlock)`: Add description.
  - Executes `simulateInteractWithBlock` behavior.
- `checkForDoubleDoor(@Nonnull World world, @Nonnull Vector3i blockPosition, @Nonnull BlockType blockType, int rotation, @Nonnull DoorState fromState, @Nonnull DoorState doorStateToCheck)`: Add description.
  - Executes `checkForDoubleDoor` behavior.
- `isHorizontalDoor(@Nonnull BlockType blockType)`: Add description.
  - Executes `isHorizontalDoor` behavior.
- `checkDoor(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, @Nonnull Vector3i blockPosition, @Nonnull BlockType blockType, int rotation, @Nonnull DoorState oldDoorState, @Nonnull DoorState newDoorState)`: Add description.
  - Executes `checkDoor` behavior.
- `activateDoor(@Nonnull World world, @Nonnull BlockType blockType, @Nonnull Vector3i blockPosition, @Nonnull DoorState fromState, @Nonnull DoorState doorState)`: Add description.
  - Executes `activateDoor` behavior.
- `getDoubleDoor(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, @Nonnull Vector3i worldPosition, @Nonnull BlockType blockType, int rotation, @Nonnull DoorState doorStateToCheck)`: Add description.
  - Executes `getDoubleDoor` behavior.
- `getDoorAtPosition(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, int x, int y, int z, @Nonnull Rotation rotationToCheck)`: Add description.
  - Executes `getDoorAtPosition` behavior.
- `canOpenDoor(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, @Nonnull Vector3i blockPosition, @Nonnull String state)`: Add description.
  - Executes `canOpenDoor` behavior.
- `isInFrontOfDoor(@Nonnull Vector3i blockPosition, @Nullable Rotation doorRotationYaw, @Nonnull Vector3d playerPosition)`: Add description.
  - Executes `isInFrontOfDoor` behavior.
- `getInteractionState(@Nonnull DoorState fromState, @Nonnull DoorState doorState)`: Add description.
  - Executes `getInteractionState` behavior.
- `getOppositeDoorState(@Nonnull DoorState doorState)`: Add description.
  - Executes `getOppositeDoorState` behavior.
- `fromBlockState(@Nullable String state)`: Add description.
  - Executes `fromBlockState` behavior.
- `getBlockType()`: Add description.
  - Executes `getBlockType` behavior.
- `getBlockPosition()`: Add description.
  - Executes `getBlockPosition` behavior.
- `getDoorState()`: Add description.
  - Executes `getDoorState` behavior.

## Notes
- No additional notes.
