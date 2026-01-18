# EnvironmentColumn

## Overview
- Documentation for `EnvironmentColumn`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk.environment`.

## Constructors
- `EnvironmentColumn(@Nonnull int[] maxYs, @Nonnull int[] values)`
  - Creates a `EnvironmentColumn` instance.
- `EnvironmentColumn(@Nonnull IntArrayList maxYs, @Nonnull IntArrayList values)`
  - Creates a `EnvironmentColumn` instance.
- `EnvironmentColumn(int initialId)`
  - Creates a `EnvironmentColumn` instance.

## Methods
- `size()`
  - Executes `size` behavior.
- `getValue(int index)`
  - Executes `getValue` behavior.
- `getValueMin(int index)`
  - Executes `getValueMin` behavior.
- `getValueMax(int index)`
  - Executes `getValueMax` behavior.
- `indexOf(int y)`
  - Executes `indexOf` behavior.
- `set(int value)`
  - Executes `set` behavior.
- `get(int y)`
  - Executes `get` behavior.
- `set(int y, int value)`
  - Executes `set` behavior.
- `getMin(int y)`
  - Executes `getMin` behavior.
- `getMax(int y)`
  - Executes `getMax` behavior.
- `set(int fromY, int toY, int value)`
  - Executes `set` behavior.
- `serialize(@Nonnull ByteBuf buf, @Nonnull IntObjectConsumer<ByteBuf> valueSerializer)`
  - Executes `serialize` behavior.
- `serializeProtocol(@Nonnull ByteBuf buf)`
  - Executes `serializeProtocol` behavior.
- `deserialize(@Nonnull ByteBuf buf, @Nonnull ToIntFunction<ByteBuf> valueDeserializer)`
  - Executes `deserialize` behavior.
- `copyFrom(@Nonnull EnvironmentColumn other)`
  - Executes `copyFrom` behavior.
- `trim()`
  - Executes `trim` behavior.
- `equals(@Nullable Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
