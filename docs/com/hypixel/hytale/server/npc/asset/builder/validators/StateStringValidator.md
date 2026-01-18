# StateStringValidator

## Overview
- Documentation for `StateStringValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `StateStringValidator(boolean allowEmptyMain, boolean mainStateOnly, boolean allowNull)`
  - Creates a `StateStringValidator` instance.
- `StateStringValidator(true, false, false)`
  - Creates a `StateStringValidator` instance.
- `StateStringValidator(false, true, false)`
  - Creates a `StateStringValidator` instance.
- `StateStringValidator(false, false, false)`
  - Creates a `StateStringValidator` instance.
- `StateStringValidator(false, false, true)`
  - Creates a `StateStringValidator` instance.

## Methods
- `test(@Nullable String value)`
  - Executes `test` behavior.
- `errorMessage(String value)`
  - Executes `errorMessage` behavior.
- `errorMessage(String value, String name)`
  - Executes `errorMessage` behavior.
- `hasMainState()`
  - Executes `hasMainState` behavior.
- `hasSubState()`
  - Executes `hasSubState` behavior.
- `getMainState()`
  - Executes `getMainState` behavior.
- `getSubState()`
  - Executes `getSubState` behavior.
- `get()`
  - Executes `get` behavior.
- `mainStateOnly()`
  - Executes `mainStateOnly` behavior.
- `requireMainState()`
  - Executes `requireMainState` behavior.
- `requireMainStateOrNull()`
  - Executes `requireMainStateOrNull` behavior.

## Notes
- No additional notes.
