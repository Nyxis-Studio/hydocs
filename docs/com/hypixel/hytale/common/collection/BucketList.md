# BucketList

## Overview
- Documentation for `BucketList`.
- Declared as a class in `com.hypixel.hytale.common.collection`.

## Constructors
- `BucketList(BucketItemPool<E> bucketItemPool)`
  - Creates a `BucketList` instance.

## Methods
- `setBucketItemPool(@Nonnull BucketItemPool<E> bucketItemPool)`
  - Executes `setBucketItemPool` behavior.
- `clear()`
  - Executes `clear` behavior.
- `reset()`
  - Executes `reset` behavior.
- `configure(@Nonnull int[] bucketRanges)`
  - Executes `configure` behavior.
- `configure(@Nonnull int[] bucketRanges, int initialBucketItemArraySize)`
  - Executes `configure` behavior.
- `configureWithPreSortedArray(@Nonnull int[] bucketRanges)`
  - Executes `configureWithPreSortedArray` behavior.
- `configureWithPreSortedArray(@Nonnull int[] bucketRanges, int initialBucketItemArraySize)`
  - Executes `configureWithPreSortedArray` behavior.
- `configureWithPresortedArray(@Nonnull IntArrayList bucketRanges, int initialBucketItemArraySize)`
  - Executes `configureWithPresortedArray` behavior.
- `add(@Nonnull E item, double squaredDistance)`
  - Executes `add` behavior.
- `getBucketCount()`
  - Executes `getBucketCount` behavior.
- `getBucket(int index)`
  - Executes `getBucket` behavior.
- `getFirstBucketIndex(int distanceSquared)`
  - Executes `getFirstBucketIndex` behavior.
- `getLastBucketIndex(int distanceSquared)`
  - Executes `getLastBucketIndex` behavior.
- `getClosestInRange(int minRange, int maxRange, @Nonnull Predicate<E> filter, @Nonnull SortBufferProvider sortBufferProvider)`
  - Executes `getClosestInRange` behavior.
- `addBucketDistance(@Nonnull IntArrayList bucketRanges, int maxBucketCount, int distance)`
  - Executes `addBucketDistance` behavior.
- `addBucketDistance(@Nonnull IntArrayList bucketRanges, int maxBucketCount, int distance, int keepDistance)`
  - Executes `addBucketDistance` behavior.
- `area(int inner, int outer)`
  - Executes `area` behavior.
- `getItems()`
  - Executes `getItems` behavior.
- `size()`
  - Executes `size` behavior.
- `isUnsorted()`
  - Executes `isUnsorted` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `clear(@Nonnull BucketItemPool<E> pool)`
  - Executes `clear` behavior.
- `add(@Nonnull BucketItem<E> item)`
  - Executes `add` behavior.
- `sort(@Nonnull SortBufferProvider sortBufferProvider)`
  - Executes `sort` behavior.
- `apply(int size)`
  - Executes `apply` behavior.

## Notes
- No additional notes.
