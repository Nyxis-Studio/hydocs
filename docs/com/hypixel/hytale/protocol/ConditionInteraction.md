# ConditionInteraction

## Overview
- Documentation for `ConditionInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ConditionInteraction()`
  - Creates a `ConditionInteraction` instance.
- `ConditionInteraction(@Nonnull WaitForDataFrom waitForDataFrom, @Nullable InteractionEffects effects, float horizontalSpeedMultiplier, float runTime, boolean cancelOnItemChange, @Nullable Map<GameMode, InteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, @Nullable InteractionCameraSettings camera, int next, int failed, @Nullable GameMode requiredGameMode, @Nullable Boolean jumping, @Nullable Boolean swimming, @Nullable Boolean crouching, @Nullable Boolean running, @Nullable Boolean flying)`
  - Creates a `ConditionInteraction` instance.
- `ConditionInteraction(@Nonnull ConditionInteraction other)`
  - Creates a `ConditionInteraction` instance.

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
