# MetricsRegistry

## Overview
- Documentation for `MetricsRegistry`.
- Declared as a class in `com.hypixel.hytale.metrics`.

## Constructors
- `MetricsRegistry()`
  - Creates a `MetricsRegistry` instance.
- `MetricsRegistry(Function<T, MetricProvider> appendFunc)`
  - Creates a `MetricsRegistry` instance.

## Methods
- `register(String id, MetricsRegistry<Void> metricsRegistry)`
  - Executes `register` behavior.
- `register(String id, Function<T, R> func, Codec<R> codec)`
  - Executes `register` behavior.
- `register(String id, @Nonnull Function<T, R> func)`
  - Executes `register` behavior.
- `register(String id, Function<T, R> func, Function<R, MetricsRegistry<R>> codecFunc)`
  - Executes `register` behavior.
- `decode(BsonValue bsonValue, ExtraInfo extraInfo)`
  - Executes `decode` behavior.
- `encode(T t, ExtraInfo extraInfo)`
  - Executes `encode` behavior.
- `toSchema(@Nonnull SchemaContext context)`
  - Executes `toSchema` behavior.
- `toMetricResults(T t)`
  - Executes `toMetricResults` behavior.
- `dumpToBson(T t)`
  - Executes `dumpToBson` behavior.
- `dumpToJson(T t)`
  - Executes `dumpToJson` behavior.
- `dumpToJson(@Nonnull Path path, T t)`
  - Executes `dumpToJson` behavior.
- `createDumpPath(@Nullable String ext)`
  - Executes `createDumpPath` behavior.
- `createDumpPath(@Nonnull Path dir, @Nullable String ext)`
  - Executes `createDumpPath` behavior.
- `createDumpPath(@Nullable String prefix, @Nullable String ext)`
  - Executes `createDumpPath` behavior.
- `createDatePath(@Nonnull Path dir, @Nullable String prefix, @Nullable String suffix)`
  - Executes `createDatePath` behavior.
- `getCodec(R value)`
  - Executes `getCodec` behavior.

## Notes
- No additional notes.
