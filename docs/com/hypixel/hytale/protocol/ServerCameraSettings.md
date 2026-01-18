**Source Hash:** `6fa83bbc9d30bc7ccfff4a36d72e5aa323a02615795414db7daa48ecdd6f4ace`

# ServerCameraSettings

## Overview

## Constructor Descriptions
- `ServerCameraSettings()`
  - Creates a `ServerCameraSettings` instance.
- `ServerCameraSettings(float positionLerpSpeed, float rotationLerpSpeed, float distance, float speedModifier, boolean allowPitchControls, boolean displayCursor, boolean displayReticle, @Nonnull MouseInputTargetType mouseInputTargetType, boolean sendMouseMotion, boolean skipCharacterPhysics, boolean isFirstPerson, @Nonnull MovementForceRotationType movementForceRotationType, @Nullable Direction movementForceRotation, @Nonnull AttachedToType attachedToType, int attachedToEntityId, boolean eyeOffset, @Nonnull PositionDistanceOffsetType positionDistanceOffsetType, @Nullable Position positionOffset, @Nullable Direction rotationOffset, @Nonnull PositionType positionType, @Nullable Position position, @Nonnull RotationType rotationType, @Nullable Direction rotation, @Nonnull CanMoveType canMoveType, @Nonnull ApplyMovementType applyMovementType, @Nullable Vector3f movementMultiplier, @Nonnull ApplyLookType applyLookType, @Nullable Vector2f lookMultiplier, @Nonnull MouseInputType mouseInputType, @Nullable Vector3f planeNormal)`
  - Creates a `ServerCameraSettings` instance.
- `ServerCameraSettings(@Nonnull ServerCameraSettings other)`
  - Creates a `ServerCameraSettings` instance.

## Method Descriptions
- `deserialize(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`: Add description.
  - Executes `serialize` behavior.
- `computeSize()`: Add description.
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`: Add description.
  - Executes `validateStructure` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `equals(Object obj)`: Add description.
  - Executes `equals` behavior.
- `hashCode()`: Add description.
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
