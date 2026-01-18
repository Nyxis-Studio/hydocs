# IntRangeBoundValidator

## Overview
- Documentation for `IntRangeBoundValidator`.
- Declared as a class in `com.hypixel.hytale.math.range`.

## Constructors
- `IntRangeBoundValidator(min, max, inclusive, true)`
  - Creates a `IntRangeBoundValidator` instance.
- `IntRangeBoundValidator(min, max, inclusive, false)`
  - Creates a `IntRangeBoundValidator` instance.
- `IntRangeBoundValidator(Integer min, Integer max, boolean inclusive, boolean lowerBound)`
  - Creates a `IntRangeBoundValidator` instance.

## Methods
- `lowerBound(Integer min, Integer max, boolean inclusive)`
  - Executes `lowerBound` behavior.
- `upperBound(Integer min, Integer max, boolean inclusive)`
  - Executes `upperBound` behavior.
- `accept(@Nullable IntRange intRange, @Nonnull ValidationResults results)`
  - Executes `accept` behavior.
- `validateBound(int value, String boundName, @Nonnull ValidationResults results)`
  - Executes `validateBound` behavior.
- `updateSchema(SchemaContext context, Schema target)`
  - Executes `updateSchema` behavior.
- `updateSchemaBound(@Nonnull IntegerSchema integerSchema)`
  - Executes `updateSchemaBound` behavior.

## Notes
- No additional notes.
