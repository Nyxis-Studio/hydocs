**Source Hash:** `690ab5dfaa445361b1a562723208cbfa9cfc6289af0bb44ab2a893b0210c927b`

# IntRangeBoundValidator

## Overview

## Constructor Descriptions
- `IntRangeBoundValidator(min, max, inclusive, true)`
  - Creates a `IntRangeBoundValidator` instance.
- `IntRangeBoundValidator(min, max, inclusive, false)`
  - Creates a `IntRangeBoundValidator` instance.
- `IntRangeBoundValidator(Integer min, Integer max, boolean inclusive, boolean lowerBound)`
  - Creates a `IntRangeBoundValidator` instance.

## Method Descriptions
- `lowerBound(Integer min, Integer max, boolean inclusive)`: Add description.
  - Executes `lowerBound` behavior.
- `upperBound(Integer min, Integer max, boolean inclusive)`: Add description.
  - Executes `upperBound` behavior.
- `accept(@Nullable IntRange intRange, @Nonnull ValidationResults results)`: Add description.
  - Executes `accept` behavior.
- `validateBound(int value, String boundName, @Nonnull ValidationResults results)`: Add description.
  - Executes `validateBound` behavior.
- `updateSchema(SchemaContext context, Schema target)`: Add description.
  - Executes `updateSchema` behavior.
- `updateSchemaBound(@Nonnull IntegerSchema integerSchema)`: Add description.
  - Executes `updateSchemaBound` behavior.

## Notes
- No additional notes.
