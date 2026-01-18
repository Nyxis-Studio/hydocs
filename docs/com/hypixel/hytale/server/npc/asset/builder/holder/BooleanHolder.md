# BooleanHolder

## Overview
- Documentation for `BooleanHolder`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.holder`.

## Constructors
- `BooleanHolder()`
  - Creates a `BooleanHolder` instance.

## Methods
- `readJSON(@Nonnull JsonElement requiredJsonElement, String name, @Nonnull BuilderParameters builderParameters)`
  - Executes `readJSON` behavior.
- `validate(ExecutionContext context)`
  - Executes `validate` behavior.
- `readJSON(JsonElement optionalJsonElement, boolean defaultValue, String name, @Nonnull BuilderParameters builderParameters)`
  - Executes `readJSON` behavior.
- `get(ExecutionContext executionContext)`
  - Executes `get` behavior.
- `rawGet(ExecutionContext executionContext)`
  - Executes `rawGet` behavior.
- `addRelationValidator(BiConsumer<ExecutionContext, Boolean> validator)`
  - Executes `addRelationValidator` behavior.
- `validateRelations(ExecutionContext executionContext, boolean value)`
  - Executes `validateRelations` behavior.

## Notes
- No additional notes.
