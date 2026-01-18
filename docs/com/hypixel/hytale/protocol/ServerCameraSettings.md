# ServerCameraSettings

## Overview
- Documentation for `ServerCameraSettings`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ServerCameraSettings()`
  - Creates a `ServerCameraSettings` instance.
- `ServerCameraSettings(float positionLerpSpeed, float rotationLerpSpeed, float distance, float speedModifier, boolean allowPitchControls, boolean displayCursor, boolean displayReticle, @Nonnull MouseInputTargetType mouseInputTargetType, boolean sendMouseMotion, boolean skipCharacterPhysics, boolean isFirstPerson, @Nonnull MovementForceRotationType movementForceRotationType, @Nullable Direction movementForceRotation, @Nonnull AttachedToType attachedToType, int attachedToEntityId, boolean eyeOffset, @Nonnull PositionDistanceOffsetType positionDistanceOffsetType, @Nullable Position positionOffset, @Nullable Direction rotationOffset, @Nonnull PositionType positionType, @Nullable Position position, @Nonnull RotationType rotationType, @Nullable Direction rotation, @Nonnull CanMoveType canMoveType, @Nonnull ApplyMovementType applyMovementType, @Nullable Vector3f movementMultiplier, @Nonnull ApplyLookType applyLookType, @Nullable Vector2f lookMultiplier, @Nonnull MouseInputType mouseInputType, @Nullable Vector3f planeNormal)`
  - Creates a `ServerCameraSettings` instance.
- `ServerCameraSettings(@Nonnull ServerCameraSettings other)`
  - Creates a `ServerCameraSettings` instance.

## Methods
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
