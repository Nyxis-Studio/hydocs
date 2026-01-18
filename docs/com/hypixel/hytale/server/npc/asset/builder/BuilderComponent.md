# BuilderComponent

## Overview
- Documentation for `BuilderComponent`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder`.

## Constructors
- `BuilderComponent(Class<T> classType)`
  - Creates a `BuilderComponent` instance.

## Methods
- `getShortDescription()`
  - Executes `getShortDescription` behavior.
- `getLongDescription()`
  - Executes `getLongDescription` behavior.
- `build(@Nonnull BuilderSupport builderSupport)`
  - Executes `build` behavior.
- `category()`
  - Executes `category` behavior.
- `getBuilderDescriptorState()`
  - Executes `getBuilderDescriptorState` behavior.
- `isEnabled(ExecutionContext context)`
  - Executes `isEnabled` behavior.
- `readConfig(@Nonnull JsonElement data)`
  - Executes `readConfig` behavior.
- `validate(String configName, @Nonnull NPCLoadTimeValidationHelper validationHelper, @Nonnull ExecutionContext context, Scope globalScope, @Nonnull List<String> errors)`
  - Executes `validate` behavior.
- `canRequireFeature()`
  - Executes `canRequireFeature` behavior.
- `toSchema(@Nonnull SchemaContext context)`
  - Executes `toSchema` behavior.

## Notes
- No additional notes.
