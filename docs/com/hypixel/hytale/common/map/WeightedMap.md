# WeightedMap

## Overview
- Documentation for `WeightedMap`.
- Declared as a class in `com.hypixel.hytale.common.map`.

## Constructors
- `WeightedMap(@Nonnull T[] keys, double[] values, double sum)`
  - Creates a `WeightedMap` instance.

## Methods
- `builder(T[] emptyKeys)`
  - Executes `builder` behavior.
- `get(double value)`
  - Executes `get` behavior.
- `get(@Nonnull DoubleSupplier supplier)`
  - Executes `get` behavior.
- `get(@Nonnull Random random)`
  - Executes `get` behavior.
- `get(int x, int z, @Nonnull BiIntToDoubleFunction supplier)`
  - Executes `get` behavior.
- `get(long x, long z, @Nonnull BiLongToDoubleFunction supplier)`
  - Executes `get` behavior.
- `get(double x, double z, @Nonnull BiDoubleToDoubleFunction supplier)`
  - Executes `get` behavior.
- `get(int seed, int x, int z, @Nonnull IWeightedMap.SeedCoordinateFunction<K> supplier, K k)`
  - Executes `get` behavior.
- `size()`
  - Executes `size` behavior.
- `contains(T obj)`
  - Executes `contains` behavior.
- `forEach(@Nonnull Consumer<T> consumer)`
  - Executes `forEach` behavior.
- `forEachEntry(@Nonnull ObjDoubleConsumer<T> consumer)`
  - Executes `forEachEntry` behavior.
- `internalKeys()`
  - Executes `internalKeys` behavior.
- `toArray()`
  - Executes `toArray` behavior.
- `resolveKeys(@Nonnull Function<T, K> mapper, @Nonnull IntFunction<K[]> arraySupplier)`
  - Executes `resolveKeys` behavior.
- `toString()`
  - Executes `toString` behavior.
- `putAll(@Nullable IWeightedMap<T> map)`
  - Executes `putAll` behavior.
- `putAll(@Nullable T[] arr, @Nonnull ToDoubleFunction<T> weight)`
  - Executes `putAll` behavior.
- `put(T obj, double weight)`
  - Executes `put` behavior.
- `ensureCapacity(int toAdd)`
  - Executes `ensureCapacity` behavior.
- `resize(int newLength)`
  - Executes `resize` behavior.
- `insert(T key, double value)`
  - Executes `insert` behavior.
- `allocated()`
  - Executes `allocated` behavior.
- `clear()`
  - Executes `clear` behavior.
- `build()`
  - Executes `build` behavior.
- `get(DoubleSupplier supplier)`
  - Executes `get` behavior.
- `get(Random random)`
  - Executes `get` behavior.
- `get(int x, int z, BiIntToDoubleFunction supplier)`
  - Executes `get` behavior.
- `get(long x, long z, BiLongToDoubleFunction supplier)`
  - Executes `get` behavior.
- `get(double x, double z, BiDoubleToDoubleFunction supplier)`
  - Executes `get` behavior.
- `get(int seed, int x, int z, IWeightedMap.SeedCoordinateFunction<K> supplier, K k)`
  - Executes `get` behavior.
- `contains(@Nullable T obj)`
  - Executes `contains` behavior.

## Notes
- No additional notes.
