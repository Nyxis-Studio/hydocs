# StatsConditionInteraction

## Overview
- Documentation for `StatsConditionInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `StatsConditionInteraction()`
  - Creates a `StatsConditionInteraction` instance.
- `StatsConditionInteraction(@Nonnull WaitForDataFrom waitForDataFrom, @Nullable InteractionEffects effects, float horizontalSpeedMultiplier, float runTime, boolean cancelOnItemChange, @Nullable Map<GameMode, InteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, @Nullable InteractionCameraSettings camera, int next, int failed, @Nullable Map<Integer, Float> costs, boolean lessThan, boolean lenient, @Nonnull ValueType valueType)`
  - Creates a `StatsConditionInteraction` instance.
- `StatsConditionInteraction(@Nonnull StatsConditionInteraction other)`
  - Creates a `StatsConditionInteraction` instance.

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
