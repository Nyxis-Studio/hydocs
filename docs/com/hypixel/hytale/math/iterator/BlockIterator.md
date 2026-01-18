# BlockIterator

## Overview
- Documentation for `BlockIterator`.
- Declared as a class in `com.hypixel.hytale.math.iterator`.

## Constructors
- `BlockIterator()`
  - Creates a `BlockIterator` instance.

## Methods
- `iterateFromTo(@Nonnull Vector3d origin, @Nonnull Vector3d target, @Nonnull BlockIteratorProcedure procedure)`
  - Executes `iterateFromTo` behavior.
- `iterateFromTo(@Nonnull Vector3i origin, @Nonnull Vector3i target, @Nonnull BlockIteratorProcedure procedure)`
  - Executes `iterateFromTo` behavior.
- `iterateFromTo(double sx, double sy, double sz, double tx, double ty, double tz, @Nonnull BlockIteratorProcedure procedure)`
  - Executes `iterateFromTo` behavior.
- `iterateFromTo(double sx, double sy, double sz, double tx, double ty, double tz, @Nonnull BlockIteratorProcedurePlus1<T> procedure, T t)`
  - Executes `iterateFromTo` behavior.
- `iterate(@Nonnull Vector3d origin, @Nonnull Vector3d direction, double maxDistance, @Nonnull BlockIteratorProcedure procedure)`
  - Executes `iterate` behavior.
- `iterate(double sx, double sy, double sz, double dx, double dy, double dz, double maxDistance, @Nonnull BlockIteratorProcedure procedure)`
  - Executes `iterate` behavior.
- `iterate0(double sx, double sy, double sz, double dx, double dy, double dz, double maxDistance, @Nonnull BlockIteratorProcedure procedure)`
  - Executes `iterate0` behavior.
- `iterate(double sx, double sy, double sz, double dx, double dy, double dz, double maxDistance, @Nonnull BlockIteratorProcedurePlus1<T> procedure, T obj1)`
  - Executes `iterate` behavior.
- `iterate0(double sx, double sy, double sz, double dx, double dy, double dz, double maxDistance, @Nonnull BlockIteratorProcedurePlus1<T> procedure, T obj1)`
  - Executes `iterate0` behavior.
- `checkParameters(double sx, double sy, double sz, double dx, double dy, double dz)`
  - Executes `checkParameters` behavior.
- `isNonValidNumber(double d)`
  - Executes `isNonValidNumber` behavior.
- `isZeroDirection(double dx, double dy, double dz)`
  - Executes `isZeroDirection` behavior.
- `intersection(double px, double py, double pz, double dx, double dy, double dz)`
  - Executes `intersection` behavior.
- `accept(int var1, int var2, int var3, double var4, double var6, double var8, double var10, double var12, double var14)`
  - Executes `accept` behavior.
- `accept(int var1, int var2, int var3, double var4, double var6, double var8, double var10, double var12, double var14, T var16)`
  - Executes `accept` behavior.
- `eq(double a, double b)`
  - Executes `eq` behavior.
- `sEq(double a, double b)`
  - Executes `sEq` behavior.
- `gEq(double a, double b)`
  - Executes `gEq` behavior.
- `abs(double x)`
  - Executes `abs` behavior.
- `fastFloor(double x)`
  - Executes `fastFloor` behavior.

## Notes
- No additional notes.
