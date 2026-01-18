# MovementConditionInteraction

## Overview
- Documentation for `MovementConditionInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `MovementConditionInteraction()`
  - Creates a `MovementConditionInteraction` instance.
- `MovementConditionInteraction(@Nonnull WaitForDataFrom waitForDataFrom, @Nullable InteractionEffects effects, float horizontalSpeedMultiplier, float runTime, boolean cancelOnItemChange, @Nullable Map<GameMode, InteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, @Nullable InteractionCameraSettings camera, int next, int failed, int forward, int back, int left, int right, int forwardLeft, int forwardRight, int backLeft, int backRight)`
  - Creates a `MovementConditionInteraction` instance.
- `MovementConditionInteraction(@Nonnull MovementConditionInteraction other)`
  - Creates a `MovementConditionInteraction` instance.

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
