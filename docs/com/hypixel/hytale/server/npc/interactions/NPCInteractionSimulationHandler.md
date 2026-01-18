# NPCInteractionSimulationHandler

## Overview
- Documentation for `NPCInteractionSimulationHandler`.
- Declared as a class in `com.hypixel.hytale.server.npc.interactions`.

## Constructors
- None.

## Methods
- `setState(InteractionType type, boolean state)`
  - Executes `setState` behavior.
- `isCharging(boolean firstRun, float time, InteractionType type, InteractionContext context, Ref<EntityStore> ref, CooldownHandler cooldownHandler)`
  - Executes `isCharging` behavior.
- `shouldCancelCharging(boolean firstRun, float time, InteractionType type, InteractionContext context, Ref<EntityStore> ref, CooldownHandler cooldownHandler)`
  - Executes `shouldCancelCharging` behavior.
- `getChargeValue(boolean firstRun, float time, InteractionType type, InteractionContext context, Ref<EntityStore> ref, CooldownHandler cooldownHandler)`
  - Executes `getChargeValue` behavior.
- `requestChargeTime(float chargeTime)`
  - Executes `requestChargeTime` behavior.

## Notes
- No additional notes.
