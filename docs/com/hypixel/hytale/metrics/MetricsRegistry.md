**Source Hash:** `3fd9a951ef68ec1571a6318a2b36c58b0b0698ce3378e39d7ab55e21ba6d3f65`

# MetricsRegistry

## Overview

## Constructor Descriptions
- `MetricsRegistry()`
  - Creates a `MetricsRegistry` instance.
- `MetricsRegistry(Function<T, MetricProvider> appendFunc)`
  - Creates a `MetricsRegistry` instance.

## Method Descriptions
- `register(String id, MetricsRegistry<Void> metricsRegistry)`: Add description.
  - Executes `register` behavior.
- `register(String id, Function<T, R> func, Codec<R> codec)`: Add description.
  - Executes `register` behavior.
- `register(String id, @Nonnull Function<T, R> func)`: Add description.
  - Executes `register` behavior.
- `register(String id, Function<T, R> func, Function<R, MetricsRegistry<R>> codecFunc)`: Add description.
  - Executes `register` behavior.
- `decode(BsonValue bsonValue, ExtraInfo extraInfo)`: Add description.
  - Executes `decode` behavior.
- `encode(T t, ExtraInfo extraInfo)`: Add description.
  - Executes `encode` behavior.
- `toSchema(@Nonnull SchemaContext context)`: Add description.
  - Executes `toSchema` behavior.
- `toMetricResults(T t)`: Add description.
  - Executes `toMetricResults` behavior.
- `dumpToBson(T t)`: Add description.
  - Executes `dumpToBson` behavior.
- `dumpToJson(T t)`: Add description.
  - Executes `dumpToJson` behavior.
- `dumpToJson(@Nonnull Path path, T t)`: Add description.
  - Executes `dumpToJson` behavior.
- `createDumpPath(@Nullable String ext)`: Add description.
  - Executes `createDumpPath` behavior.
- `createDumpPath(@Nonnull Path dir, @Nullable String ext)`: Add description.
  - Executes `createDumpPath` behavior.
- `createDumpPath(@Nullable String prefix, @Nullable String ext)`: Add description.
  - Executes `createDumpPath` behavior.
- `createDatePath(@Nonnull Path dir, @Nullable String prefix, @Nullable String suffix)`: Add description.
  - Executes `createDatePath` behavior.
- `getCodec(R value)`: Add description.
  - Executes `getCodec` behavior.

## Notes
- No additional notes.
