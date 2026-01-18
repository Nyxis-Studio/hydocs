# VariantRotation

## Overview
- Documentation for `VariantRotation`.
- Declared as a enum in `com.hypixel.hytale.server.core.asset.type.blocktype.config`.

## Constructors
- `VariantRotation(com.hypixel.hytale.protocol.VariantRotation protocolType, RotationTuple[] rotations, Function<RotationTuple, RotationTuple> verify, BiFunction<RotationTuple, Rotation, RotationTuple> rotateX, BiFunction<RotationTuple, Rotation, RotationTuple> rotateZ)`
  - Creates a `VariantRotation` instance.

## Methods
- `validatePipe(@Nonnull Rotation yaw)`
  - Executes `validatePipe` behavior.
- `getRotations()`
  - Executes `getRotations` behavior.
- `rotateX(RotationTuple pair, Rotation rotation)`
  - Executes `rotateX` behavior.
- `rotateZ(RotationTuple pair, Rotation rotation)`
  - Executes `rotateZ` behavior.
- `verify(RotationTuple pair)`
  - Executes `verify` behavior.

## Notes
- No additional notes.
