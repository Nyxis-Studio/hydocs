# ChainFlagInteraction

## Overview
- Documentation for `ChainFlagInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ChainFlagInteraction()`
  - Creates a `ChainFlagInteraction` instance.
- `ChainFlagInteraction(@Nonnull WaitForDataFrom waitForDataFrom, @Nullable InteractionEffects effects, float horizontalSpeedMultiplier, float runTime, boolean cancelOnItemChange, @Nullable Map<GameMode, InteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, @Nullable InteractionCameraSettings camera, int next, int failed, @Nullable String chainId, @Nullable String flag)`
  - Creates a `ChainFlagInteraction` instance.
- `ChainFlagInteraction(@Nonnull ChainFlagInteraction other)`
  - Creates a `ChainFlagInteraction` instance.

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
