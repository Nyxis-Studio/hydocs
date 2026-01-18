# RequiresFeatureIfValidator

## Overview
- Documentation for `RequiresFeatureIfValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `RequiresFeatureIfValidator(String attribute, boolean value, @Nonnull EnumSet<Feature> feature)`
  - Creates a `RequiresFeatureIfValidator` instance.
- `RequiresFeatureIfValidator(attribute, value, feature)`
  - Creates a `RequiresFeatureIfValidator` instance.

## Methods
- `validate(FeatureEvaluatorHelper evaluatorHelper)`
  - Executes `validate` behavior.
- `getErrorMessage(String context)`
  - Executes `getErrorMessage` behavior.
- `staticValidate(@Nonnull FeatureEvaluatorHelper evaluatorHelper, EnumSet<Feature> requiredFeature, boolean requiredValue, boolean value)`
  - Executes `staticValidate` behavior.
- `withAttributes(String attribute, boolean value, @Nonnull EnumSet<Feature> feature)`
  - Executes `withAttributes` behavior.

## Notes
- No additional notes.
