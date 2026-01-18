# BuilderParameters

## Overview
- Documentation for `BuilderParameters`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder`.

## Constructors
- `BuilderParameters(StdScope scope, String fileName, String interfaceCode)`
  - Creates a `BuilderParameters` instance.
- `BuilderParameters(StdScope scope, String fileName, String interfaceCode, IntSet dependencies)`
  - Creates a `BuilderParameters` instance.
- `BuilderParameters(@Nonnull BuilderParameters other)`
  - Creates a `BuilderParameters` instance.

## Methods
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `addParametersToScope()`
  - Executes `addParametersToScope` behavior.
- `getParameterType(String name)`
  - Executes `getParameterType` behavior.
- `readJSON(@Nonnull JsonObject jsonObject, @Nonnull StateMappingHelper stateHelper)`
  - Executes `readJSON` behavior.
- `createCompileContext()`
  - Executes `createCompileContext` behavior.
- `disposeCompileContext()`
  - Executes `disposeCompileContext` behavior.
- `getCompileContext()`
  - Executes `getCompileContext` behavior.
- `compile(@Nonnull String expression)`
  - Executes `compile` behavior.
- `getScope()`
  - Executes `getScope` behavior.
- `createScope()`
  - Executes `createScope` behavior.
- `validateNoDuplicateParameters(@Nonnull BuilderParameters other)`
  - Executes `validateNoDuplicateParameters` behavior.
- `getFileName()`
  - Executes `getFileName` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `getInterfaceCode()`
  - Executes `getInterfaceCode` behavior.
- `addDependency(int d)`
  - Executes `addDependency` behavior.
- `toSchema(@Nonnull SchemaContext context)`
  - Executes `toSchema` behavior.
- `getExpression()`
  - Executes `getExpression` behavior.
- `getDescription()`
  - Executes `getDescription` behavior.
- `isValidation()`
  - Executes `isValidation` behavior.
- `isPrivate()`
  - Executes `isPrivate` behavior.
- `fromJSON(@Nonnull JsonElement element, @Nonnull BuilderParameters builderParameters, String parameterName)`
  - Executes `fromJSON` behavior.

## Notes
- No additional notes.
