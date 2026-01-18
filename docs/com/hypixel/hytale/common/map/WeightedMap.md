**Source Hash:** `7cbd99bf113bbfbed05fceaf8b2b6d5a94f94ce5baefbe5d7d08e88406df8f89`

# WeightedMap

## Overview

## Constructor Descriptions
- `WeightedMap(@Nonnull T[] keys, double[] values, double sum)`
  - Creates a `WeightedMap` instance.

## Method Descriptions
- `builder(T[] emptyKeys)`: Add description.
  - Executes `builder` behavior.
- `get(double value)`: Add description.
  - Executes `get` behavior.
- `get(@Nonnull DoubleSupplier supplier)`: Add description.
  - Executes `get` behavior.
- `get(@Nonnull Random random)`: Add description.
  - Executes `get` behavior.
- `get(int x, int z, @Nonnull BiIntToDoubleFunction supplier)`: Add description.
  - Executes `get` behavior.
- `get(long x, long z, @Nonnull BiLongToDoubleFunction supplier)`: Add description.
  - Executes `get` behavior.
- `get(double x, double z, @Nonnull BiDoubleToDoubleFunction supplier)`: Add description.
  - Executes `get` behavior.
- `get(int seed, int x, int z, @Nonnull IWeightedMap.SeedCoordinateFunction<K> supplier, K k)`: Add description.
  - Executes `get` behavior.
- `size()`: Add description.
  - Executes `size` behavior.
- `contains(T obj)`: Add description.
  - Executes `contains` behavior.
- `forEach(@Nonnull Consumer<T> consumer)`: Add description.
  - Executes `forEach` behavior.
- `forEachEntry(@Nonnull ObjDoubleConsumer<T> consumer)`: Add description.
  - Executes `forEachEntry` behavior.
- `internalKeys()`: Add description.
  - Executes `internalKeys` behavior.
- `toArray()`: Add description.
  - Executes `toArray` behavior.
- `resolveKeys(@Nonnull Function<T, K> mapper, @Nonnull IntFunction<K[]> arraySupplier)`: Add description.
  - Executes `resolveKeys` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `putAll(@Nullable IWeightedMap<T> map)`: Add description.
  - Executes `putAll` behavior.
- `putAll(@Nullable T[] arr, @Nonnull ToDoubleFunction<T> weight)`: Add description.
  - Executes `putAll` behavior.
- `put(T obj, double weight)`: Add description.
  - Executes `put` behavior.
- `ensureCapacity(int toAdd)`: Add description.
  - Executes `ensureCapacity` behavior.
- `resize(int newLength)`: Add description.
  - Executes `resize` behavior.
- `insert(T key, double value)`: Add description.
  - Executes `insert` behavior.
- `allocated()`: Add description.
  - Executes `allocated` behavior.
- `clear()`: Add description.
  - Executes `clear` behavior.
- `build()`: Add description.
  - Executes `build` behavior.
- `get(DoubleSupplier supplier)`: Add description.
  - Executes `get` behavior.
- `get(Random random)`: Add description.
  - Executes `get` behavior.
- `get(int x, int z, BiIntToDoubleFunction supplier)`: Add description.
  - Executes `get` behavior.
- `get(long x, long z, BiLongToDoubleFunction supplier)`: Add description.
  - Executes `get` behavior.
- `get(double x, double z, BiDoubleToDoubleFunction supplier)`: Add description.
  - Executes `get` behavior.
- `get(int seed, int x, int z, IWeightedMap.SeedCoordinateFunction<K> supplier, K k)`: Add description.
  - Executes `get` behavior.
- `contains(@Nullable T obj)`: Add description.
  - Executes `contains` behavior.

## Notes
- No additional notes.
