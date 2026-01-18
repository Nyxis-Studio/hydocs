# ExtendedCoordinateCache

## Overview
- Documentation for `ExtendedCoordinateCache`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cache`.

## Constructors
- `ExtendedCoordinateCache(@Nonnull ExtendedCoordinateObjectFunction<K, T> loader, @Nullable ExtendedCoordinateRemovalListener<T> removalListener, int maxSize, long expireAfterSeconds)`
  - Creates a `ExtendedCoordinateCache` instance.

## Methods
- `get(@Nonnull K k, int seed, int x, int y)`
  - Executes `get` behavior.
- `localKey()`
  - Executes `localKey` behavior.
- `compute(K var1, int var2, int var3, int var4)`
  - Executes `compute` behavior.
- `onRemoval(T var1)`
  - Executes `onRemoval` behavior.
- `setLocation(@Nonnull K k, int seed, int x, int y)`
  - Executes `setLocation` behavior.
- `apply(@Nonnull ExtendedCoordinateKey<K> cachedKey)`
  - Executes `apply` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `equals(Object o)`
  - Executes `equals` behavior.

## Notes
- No additional notes.
