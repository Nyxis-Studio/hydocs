# BlockFace

## Overview
- Documentation for `BlockFace`.
- Declared as a enum in `com.hypixel.hytale.server.core.asset.type.blocktype.config`.

## Constructors
- `BlockFace(FaceConnectionType faceConnectionType, BlockNeighbor blockNeighbor, Vector3i direction)`
  - Creates a `BlockFace` instance.
- `BlockFace(@Nonnull FaceConnectionType faceConnectionType, BlockNeighbor blockNeighbor, BlockFace ... components)`
  - Creates a `BlockFace` instance.

## Methods
- `getFaceConnectionType()`
  - Executes `getFaceConnectionType` behavior.
- `getComponents()`
  - Executes `getComponents` behavior.
- `getDirection()`
  - Executes `getDirection` behavior.
- `getConnectingFaces()`
  - Executes `getConnectingFaces` behavior.
- `getConnectingFaceOffsets()`
  - Executes `getConnectingFaceOffsets` behavior.
- `getConnectingFaces0()`
  - Executes `getConnectingFaces0` behavior.
- `directionTo(@Nonnull BlockFace connectingFace)`
  - Executes `directionTo` behavior.
- `lookup(Vector3i direction)`
  - Executes `lookup` behavior.
- `rotate(@Nonnull BlockFace blockFace, @Nonnull Rotation rotationYaw, @Nonnull Rotation rotationPitch)`
  - Executes `rotate` behavior.
- `rotate(@Nonnull BlockFace blockFace, @Nonnull Rotation rotationX, @Nonnull Rotation rotationY, @Nonnull Rotation rotationZ)`
  - Executes `rotate` behavior.
- `flip(@Nonnull BlockFace blockFace)`
  - Executes `flip` behavior.
- `toProtocolBlockNeighbor()`
  - Executes `toProtocolBlockNeighbor` behavior.
- `fromProtocolFace(@Nonnull com.hypixel.hytale.protocol.BlockFace face)`
  - Executes `fromProtocolFace` behavior.

## Notes
- No additional notes.
