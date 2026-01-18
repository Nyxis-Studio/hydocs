# BooleanImplicationValidator

## Overview
- Documentation for `BooleanImplicationValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `BooleanImplicationValidator(String[] antecedentSet, boolean antecedentState, String[] consequentSet, boolean consequentState, boolean anyAntecedent)`
  - Creates a `BooleanImplicationValidator` instance.
- `BooleanImplicationValidator(antecedentSet, antecedentState, consequentSet, consequentState, anyAntecedent)`
  - Creates a `BooleanImplicationValidator` instance.

## Methods
- `test(@Nonnull boolean[] antecedents, @Nonnull boolean[] consequents)`
  - Executes `test` behavior.
- `allMatch(@Nonnull boolean[] values, boolean expected)`
  - Executes `allMatch` behavior.
- `anyMatch(@Nonnull boolean[] values, boolean expected)`
  - Executes `anyMatch` behavior.
- `errorMessage()`
  - Executes `errorMessage` behavior.
- `withAttributes(String[] antecedentSet, boolean antecedentState, String[] consequentSet, boolean consequentState, boolean anyAntecedent)`
  - Executes `withAttributes` behavior.

## Notes
- No additional notes.
