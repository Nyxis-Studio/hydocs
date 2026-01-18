# Query

## Overview
- Documentation for `Query`.
- Declared as a interface in `com.hypixel.hytale.component.query`.

## Constructors
- None.

## Methods
- `any()`
  - Executes `any` behavior.
- `not(Query<ECS_TYPE> query)`
  - Executes `not` behavior.
- `and(Query<ECS_TYPE> ... queries)`
  - Executes `and` behavior.
- `or(Query<ECS_TYPE> ... queries)`
  - Executes `or` behavior.
- `test(Archetype<ECS_TYPE> var1)`
  - Executes `test` behavior.
- `requiresComponentType(ComponentType<ECS_TYPE, ?> var1)`
  - Executes `requiresComponentType` behavior.
- `validateRegistry(ComponentRegistry<ECS_TYPE> var1)`
  - Executes `validateRegistry` behavior.
- `validate()`
  - Executes `validate` behavior.

## Notes
- No additional notes.
