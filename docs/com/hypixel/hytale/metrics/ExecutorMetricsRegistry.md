# ExecutorMetricsRegistry

## Overview
- Documentation for `ExecutorMetricsRegistry`.
- Declared as a class in `com.hypixel.hytale.metrics`.

## Constructors
- None.

## Methods
- `encode(@Nonnull T t, ExtraInfo extraInfo)`
  - Executes `encode` behavior.
- `register(String id, @Nonnull Function<T, R> func)`
  - Executes `register` behavior.
- `register(String id, Function<T, R> func, Codec<R> codec)`
  - Executes `register` behavior.
- `register(String id, MetricsRegistry<Void> metricsRegistry)`
  - Executes `register` behavior.
- `register(String id, Function<T, R> func, Function<R, MetricsRegistry<R>> codecFunc)`
  - Executes `register` behavior.
- `isInThread()`
  - Executes `isInThread` behavior.

## Notes
- No additional notes.
