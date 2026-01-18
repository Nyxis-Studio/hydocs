# ChainingInteraction

## Overview
- Documentation for `ChainingInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ChainingInteraction()`
  - Creates a `ChainingInteraction` instance.
- `ChainingInteraction(@Nonnull WaitForDataFrom waitForDataFrom, @Nullable InteractionEffects effects, float horizontalSpeedMultiplier, float runTime, boolean cancelOnItemChange, @Nullable Map<GameMode, InteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, @Nullable InteractionCameraSettings camera, @Nullable String chainId, float chainingAllowance, @Nullable int[] chainingNext, @Nullable Map<String, Integer> flags)`
  - Creates a `ChainingInteraction` instance.
- `ChainingInteraction(@Nonnull ChainingInteraction other)`
  - Creates a `ChainingInteraction` instance.

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
