# OneOrNonePresentValidator

## Overview
- Documentation for `OneOrNonePresentValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `OneOrNonePresentValidator(String ... attributes)`
  - Creates a `OneOrNonePresentValidator` instance.
- `OneOrNonePresentValidator(attributes)`
  - Creates a `OneOrNonePresentValidator` instance.

## Methods
- `test(@Nonnull BuilderObjectHelper<?>[] objects)`
  - Executes `test` behavior.
- `test(@Nonnull boolean[] readStatus)`
  - Executes `test` behavior.
- `test(@Nonnull BuilderObjectHelper<?> objectHelper1, @Nonnull BuilderObjectHelper<?> objectHelper2)`
  - Executes `test` behavior.
- `test(@Nonnull BuilderObjectHelper<?> objectHelper1, @Nonnull BuilderObjectHelper<?> objectHelper2, @Nonnull BuilderObjectHelper<?> objectHelper3)`
  - Executes `test` behavior.
- `errorMessage(@Nonnull String[] attributes, BuilderObjectHelper<?>[] objectHelpers)`
  - Executes `errorMessage` behavior.
- `errorMessage(@Nonnull String[] attributes, boolean[] readStatus)`
  - Executes `errorMessage` behavior.
- `errorMessage(@Nonnull String[] attributes, @Nonnull IntPredicate presentPredicate)`
  - Executes `errorMessage` behavior.
- `withAttributes(String ... attributes)`
  - Executes `withAttributes` behavior.

## Notes
- No additional notes.
