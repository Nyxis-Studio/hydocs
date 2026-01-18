# BlockStateRegistry

## Overview
- Documentation for `BlockStateRegistry`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.meta`.

## Constructors
- `BlockStateRegistry(@Nonnull List<BooleanConsumer> registrations, BooleanSupplier precondition, String preconditionMessage)`
  - Creates a `BlockStateRegistry` instance.

## Methods
- `registerBlockState(@Nonnull Class<T> clazz, @Nonnull String key, Codec<T> codec)`
  - Executes `registerBlockState` behavior.
- `registerBlockState(@Nonnull Class<T> clazz, @Nonnull String key, Codec<T> codec, Class<D> dataClass, Codec<D> dataCodec)`
  - Executes `registerBlockState` behavior.

## Notes
- No additional notes.
