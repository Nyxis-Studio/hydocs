# DoubleHolderBase

## Overview
- Documentation for `DoubleHolderBase`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.holder`.

## Constructors
- `DoubleHolderBase()`
  - Creates a `DoubleHolderBase` instance.

## Methods
- `readJSON(@Nonnull JsonElement requiredJsonElement, DoubleValidator validator, String name, @Nonnull BuilderParameters builderParameters)`
  - Executes `readJSON` behavior.
- `readJSON(JsonElement optionalJsonElement, double defaultValue, DoubleValidator validator, String name, @Nonnull BuilderParameters builderParameters)`
  - Executes `readJSON` behavior.
- `addRelationValidator(ObjDoubleConsumer<ExecutionContext> validator)`
  - Executes `addRelationValidator` behavior.
- `validateRelations(ExecutionContext executionContext, double value)`
  - Executes `validateRelations` behavior.
- `rawGet(ExecutionContext executionContext)`
  - Executes `rawGet` behavior.
- `validate(double value)`
  - Executes `validate` behavior.

## Notes
- No additional notes.
