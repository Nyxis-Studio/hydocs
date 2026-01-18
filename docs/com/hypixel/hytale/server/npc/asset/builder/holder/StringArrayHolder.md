# StringArrayHolder

## Overview
- Documentation for `StringArrayHolder`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.holder`.

## Constructors
- `StringArrayHolder()`
  - Creates a `StringArrayHolder` instance.

## Methods
- `validate(ExecutionContext context)`
  - Executes `validate` behavior.
- `readJSON(@Nonnull JsonElement requiredJsonElement, int minLength, int maxLength, StringArrayValidator validator, String name, @Nonnull BuilderParameters builderParameters)`
  - Executes `readJSON` behavior.
- `readJSON(JsonElement optionalJsonElement, int minLength, int maxLength, String[] defaultValue, StringArrayValidator validator, String name, @Nonnull BuilderParameters builderParameters)`
  - Executes `readJSON` behavior.
- `get(ExecutionContext executionContext)`
  - Executes `get` behavior.
- `rawGet(ExecutionContext executionContext)`
  - Executes `rawGet` behavior.
- `validate(@Nullable String[] value)`
  - Executes `validate` behavior.
- `addRelationValidator(BiConsumer<ExecutionContext, String[]> validator)`
  - Executes `addRelationValidator` behavior.
- `validateRelations(ExecutionContext executionContext, String[] value)`
  - Executes `validateRelations` behavior.

## Notes
- No additional notes.
