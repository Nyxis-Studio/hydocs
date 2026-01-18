# BuilderRoleVariant

## Overview
- Documentation for `BuilderRoleVariant`.
- Declared as a class in `com.hypixel.hytale.server.npc.role.builders`.

## Constructors
- None.

## Methods
- `build(@Nonnull BuilderSupport builderSupport)`
  - Executes `build` behavior.
- `getStateMappingHelper()`
  - Executes `getStateMappingHelper` behavior.
- `validate(String configName, @Nonnull NPCLoadTimeValidationHelper validationHelper, @Nonnull ExecutionContext context, Scope globalScope, List<String> errors)`
  - Executes `validate` behavior.
- `readConfig(@Nonnull JsonElement data)`
  - Executes `readConfig` behavior.
- `category()`
  - Executes `category` behavior.
- `getIdentifier()`
  - Executes `getIdentifier` behavior.
- `canSpawn(@Nonnull SpawningContext spawningContext)`
  - Executes `canSpawn` behavior.
- `getSpawnModelName(@Nonnull ExecutionContext context, Scope modifierScope)`
  - Executes `getSpawnModelName` behavior.
- `createModifierScope(@Nonnull ExecutionContext executionContext)`
  - Executes `createModifierScope` behavior.
- `createExecutionScope()`
  - Executes `createExecutionScope` behavior.
- `markNeedsReload()`
  - Executes `markNeedsReload` behavior.
- `getShortDescription()`
  - Executes `getShortDescription` behavior.
- `getLongDescription()`
  - Executes `getLongDescription` behavior.
- `getBuilderDescriptorState()`
  - Executes `getBuilderDescriptorState` behavior.
- `isEnabled(ExecutionContext context)`
  - Executes `isEnabled` behavior.
- `getReferenceIndex()`
  - Executes `getReferenceIndex` behavior.
- `isMemory(@Nonnull ExecutionContext context, Scope modifierScope)`
  - Executes `isMemory` behavior.
- `getMemoriesCategory(@Nonnull ExecutionContext context, Scope modifierScope)`
  - Executes `getMemoriesCategory` behavior.
- `getMemoriesNameOverride(@Nonnull ExecutionContext context, Scope modifierScope)`
  - Executes `getMemoriesNameOverride` behavior.
- `getNameTranslationKey(ExecutionContext context, Scope modifierScope)`
  - Executes `getNameTranslationKey` behavior.
- `executeOnSuperRole(@Nonnull BuilderSupport builderSupport, @Nonnull BiFunction<Builder<Role>, BuilderSupport, V> func, @Nonnull Supplier<V> failed)`
  - Executes `executeOnSuperRole` behavior.
- `executeOnSuperRole(@Nonnull SpawningContext spawningContext, @Nonnull BiFunction<Builder<Role>, SpawningContext, V> func, @Nonnull Supplier<V> failed)`
  - Executes `executeOnSuperRole` behavior.
- `executeOnSuperRole(@Nonnull ExecutionContext context, Scope modifierScope, @Nonnull TriFunction<Builder<Role>, ExecutionContext, Scope, V> func, @Nonnull Supplier<V> failed)`
  - Executes `executeOnSuperRole` behavior.
- `executeOnSuperRole(@Nonnull ExecutionContext context, Scope modifierScope, @Nonnull TriToIntFunction<Builder<Role>, ExecutionContext, Scope> func, int failed)`
  - Executes `executeOnSuperRole` behavior.

## Notes
- No additional notes.
