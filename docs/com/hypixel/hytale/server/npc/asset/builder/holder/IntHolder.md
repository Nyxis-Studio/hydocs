# IntHolder

## Overview
- Documentation for `IntHolder`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.holder`.

## Constructors
- `IntHolder()`
  - Creates a `IntHolder` instance.

## Methods
- `validate(ExecutionContext context)`
  - Executes `validate` behavior.
- `readJSON(@Nonnull JsonElement requiredJsonElement, IntValidator validator, String name, @Nonnull BuilderParameters builderParameters)`
  - Executes `readJSON` behavior.
- `readJSON(JsonElement optionalJsonElement, int defaultValue, IntValidator validator, String name, @Nonnull BuilderParameters builderParameters)`
  - Executes `readJSON` behavior.
- `get(ExecutionContext executionContext)`
  - Executes `get` behavior.
- `rawGet(ExecutionContext executionContext)`
  - Executes `rawGet` behavior.
- `validate(int value)`
  - Executes `validate` behavior.
- `addRelationValidator(ObjIntConsumer<ExecutionContext> validator)`
  - Executes `addRelationValidator` behavior.
- `validateRelations(ExecutionContext executionContext, int value)`
  - Executes `validateRelations` behavior.

## Notes
- No additional notes.
