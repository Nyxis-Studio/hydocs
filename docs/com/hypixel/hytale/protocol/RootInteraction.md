# RootInteraction

## Overview
- Documentation for `RootInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `RootInteraction()`
  - Creates a `RootInteraction` instance.
- `RootInteraction(@Nullable String id, @Nullable int[] interactions, @Nullable InteractionCooldown cooldown, @Nullable Map<GameMode, RootInteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, float clickQueuingTimeout, boolean requireNewClick)`
  - Creates a `RootInteraction` instance.
- `RootInteraction(@Nonnull RootInteraction other)`
  - Creates a `RootInteraction` instance.

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
