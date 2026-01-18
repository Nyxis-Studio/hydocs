# InternalReferenceResolver

## Overview
- Documentation for `InternalReferenceResolver`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder`.

## Constructors
- `InternalReferenceResolver()`
  - Creates a `InternalReferenceResolver` instance.

## Methods
- `getOrCreateIndex(String name)`
  - Executes `getOrCreateIndex` behavior.
- `setRecordDependencies()`
  - Executes `setRecordDependencies` behavior.
- `getRecordedDependenices()`
  - Executes `getRecordedDependenices` behavior.
- `stopRecordingDependencies()`
  - Executes `stopRecordingDependencies` behavior.
- `addBuilder(int index, BuilderInstructionReference builder)`
  - Executes `addBuilder` behavior.
- `validateInternalReferences(String configName, @Nonnull List<String> errors)`
  - Executes `validateInternalReferences` behavior.
- `validateNoCycles(@Nonnull BuilderInstructionReference builder, int index, @Nonnull IntArrayList path)`
  - Executes `validateNoCycles` behavior.
- `getBuilder(int index, Class<?> classType)`
  - Executes `getBuilder` behavior.
- `optimise()`
  - Executes `optimise` behavior.

## Notes
- No additional notes.
