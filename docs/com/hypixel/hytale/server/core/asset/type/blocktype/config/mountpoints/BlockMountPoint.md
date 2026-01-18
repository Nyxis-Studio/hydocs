# BlockMountPoint

## Overview
- Documentation for `BlockMountPoint`.
- Declared as a class in `com.hypixel.hytale.server.core.asset.type.blocktype.config.mountpoints`.

## Constructors
- `BlockMountPoint()`
  - Creates a `BlockMountPoint` instance.
- `BlockMountPoint(Vector3f offset, float yawOffSetDegrees)`
  - Creates a `BlockMountPoint` instance.
- `BlockMountPoint(rotatedOffset, this.yawOffSetDegrees)`
  - Creates a `BlockMountPoint` instance.

## Methods
- `getOffset()`
  - Executes `getOffset` behavior.
- `getYawOffSetDegrees()`
  - Executes `getYawOffSetDegrees` behavior.
- `rotate(@Nonnull Rotation yaw, @Nonnull Rotation pitch, @Nonnull Rotation roll)`
  - Executes `rotate` behavior.
- `computeWorldSpacePosition(@Nonnull Vector3i blockLoc)`
  - Executes `computeWorldSpacePosition` behavior.
- `computeRotationEuler(@Nonnull int rotationIndex)`
  - Executes `computeRotationEuler` behavior.

## Notes
- No additional notes.
