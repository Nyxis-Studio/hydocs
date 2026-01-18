# CameraInteraction

## Overview
- Documentation for `CameraInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `CameraInteraction()`
  - Creates a `CameraInteraction` instance.
- `CameraInteraction(@Nonnull WaitForDataFrom waitForDataFrom, @Nullable InteractionEffects effects, float horizontalSpeedMultiplier, float runTime, boolean cancelOnItemChange, @Nullable Map<GameMode, InteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, @Nullable InteractionCameraSettings camera, int next, int failed, @Nonnull CameraActionType cameraAction, @Nonnull CameraPerspectiveType cameraPerspective, boolean cameraPersist, float cameraInteractionTime)`
  - Creates a `CameraInteraction` instance.
- `CameraInteraction(@Nonnull CameraInteraction other)`
  - Creates a `CameraInteraction` instance.

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
