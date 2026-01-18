**Source Hash:** `1a3dabdb2473f5f98158eeeceee6cff2ab9d26f2f5ba8d0387cb6ec8a2ac67ed`

# ExecutorMetricsRegistry

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `encode(@Nonnull T t, ExtraInfo extraInfo)`: Add description.
  - Executes `encode` behavior.
- `register(String id, @Nonnull Function<T, R> func)`: Add description.
  - Executes `register` behavior.
- `register(String id, Function<T, R> func, Codec<R> codec)`: Add description.
  - Executes `register` behavior.
- `register(String id, MetricsRegistry<Void> metricsRegistry)`: Add description.
  - Executes `register` behavior.
- `register(String id, Function<T, R> func, Function<R, MetricsRegistry<R>> codecFunc)`: Add description.
  - Executes `register` behavior.
- `isInThread()`: Add description.
  - Executes `isInThread` behavior.

## Notes
- No additional notes.
