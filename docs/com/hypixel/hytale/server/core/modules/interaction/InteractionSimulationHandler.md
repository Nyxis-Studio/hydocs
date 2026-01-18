# InteractionSimulationHandler

## Overview
- Documentation for `InteractionSimulationHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction`.

## Constructors
- None.

## Methods
- `setState(@Nonnull InteractionType type, boolean state)`
  - Executes `setState` behavior.
- `isCharging(boolean firstRun, float time, @Nonnull InteractionType type, InteractionContext context, Ref<EntityStore> ref, CooldownHandler cooldownHandler)`
  - Executes `isCharging` behavior.
- `shouldCancelCharging(boolean firstRun, float time, InteractionType type, InteractionContext context, Ref<EntityStore> ref, CooldownHandler cooldownHandler)`
  - Executes `shouldCancelCharging` behavior.
- `getChargeValue(boolean firstRun, float time, InteractionType type, InteractionContext context, Ref<EntityStore> ref, CooldownHandler cooldownHandler)`
  - Executes `getChargeValue` behavior.

## Notes
- No additional notes.
