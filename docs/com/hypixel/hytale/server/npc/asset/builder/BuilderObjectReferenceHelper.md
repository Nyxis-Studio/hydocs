# BuilderObjectReferenceHelper

## Overview
- Documentation for `BuilderObjectReferenceHelper`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder`.

## Constructors
- `BuilderObjectReferenceHelper(Class<?> classType, BuilderContext owner)`
  - Creates a `BuilderObjectReferenceHelper` instance.

## Methods
- `excludeFromRegularBuild()`
  - Executes `excludeFromRegularBuild` behavior.
- `build(@Nonnull BuilderSupport builderSupport)`
  - Executes `build` behavior.
- `validate(String configName, NPCLoadTimeValidationHelper loadTimeValidationHelper, @Nonnull BuilderManager manager, @Nonnull ExecutionContext context, Scope globalScope, @Nonnull List<String> errors)`
  - Executes `validate` behavior.
- `getBuilder(@Nonnull BuilderManager builderManager, @Nonnull BuilderSupport support, boolean nullable)`
  - Executes `getBuilder` behavior.
- `getBuilder(@Nonnull BuilderManager builderManager, ExecutionContext context, @Nullable Builder<?> parentSpawnable)`
  - Executes `getBuilder` behavior.
- `readConfig(@Nonnull JsonElement data, @Nonnull BuilderManager builderManager, @Nonnull BuilderParameters builderParameters, @Nonnull BuilderValidationHelper builderValidationHelper)`
  - Executes `readConfig` behavior.
- `readConfig(@Nonnull JsonElement data, @Nonnull BuilderFactory<T> factory, @Nonnull BuilderManager builderManager, @Nonnull BuilderParameters builderParameters, @Nonnull BuilderValidationHelper builderValidationHelper)`
  - Executes `readConfig` behavior.
- `setInternalReference(@Nonnull StringHolder holder, InternalReferenceResolver referenceResolver)`
  - Executes `setInternalReference` behavior.
- `setFileReference(@Nonnull StringHolder holder, @Nonnull JsonObject jsonObject, @Nonnull BuilderManager builderManager)`
  - Executes `setFileReference` behavior.
- `validateRequiredFeatures(@Nonnull Builder<T> builder, BuilderManager manager, ExecutionContext context)`
  - Executes `validateRequiredFeatures` behavior.
- `validateInstructionContext(@Nonnull Builder<T> builder, @Nonnull BuilderSupport support)`
  - Executes `validateInstructionContext` behavior.
- `validateComponentInterfaceMatch(String builderInterfaceCode)`
  - Executes `validateComponentInterfaceMatch` behavior.
- `isPresent()`
  - Executes `isPresent` behavior.
- `isFinal()`
  - Executes `isFinal` behavior.
- `getLabel()`
  - Executes `getLabel` behavior.
- `setLabel(String label)`
  - Executes `setLabel` behavior.

## Notes
- No additional notes.
