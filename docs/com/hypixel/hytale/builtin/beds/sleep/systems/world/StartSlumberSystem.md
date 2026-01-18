# StartSlumberSystem

## Overview
- Documentation for `StartSlumberSystem`.
- Declared as a class in `com.hypixel.hytale.builtin.beds.sleep.systems.world`.

## Constructors
- `StartSlumberSystem()`
  - Creates a `StartSlumberSystem` instance.

## Methods
- `delayedTick(float dt, int systemIndex, @NonNullDecl Store<EntityStore> store)`
  - Executes `delayedTick` behavior.
- `checkIfEveryoneIsReadyToSleep(Store<EntityStore> store)`
  - Executes `checkIfEveryoneIsReadyToSleep` behavior.
- `computeWakeupInstant(Instant now, float wakeUpHour)`
  - Executes `computeWakeupInstant` behavior.
- `computeIrlSeconds(Instant startInstant, Instant targetInstant)`
  - Executes `computeIrlSeconds` behavior.
- `isEveryoneReadyToSleep(ComponentAccessor<EntityStore> store)`
  - Executes `isEveryoneReadyToSleep` behavior.
- `isReadyToSleep(ComponentAccessor<EntityStore> store, Ref<EntityStore> ref)`
  - Executes `isReadyToSleep` behavior.

## Notes
- No additional notes.
