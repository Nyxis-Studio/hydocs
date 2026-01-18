# SetServerCamera

## Overview
- Documentation for `SetServerCamera`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.camera`.

## Constructors
- `SetServerCamera()`
  - Creates a `SetServerCamera` instance.
- `SetServerCamera(@Nonnull ClientCameraView clientCameraView, boolean isLocked, @Nullable ServerCameraSettings cameraSettings)`
  - Creates a `SetServerCamera` instance.
- `SetServerCamera(@Nonnull SetServerCamera other)`
  - Creates a `SetServerCamera` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
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
