# OperationsBuilder

## Overview
- Documentation for `OperationsBuilder`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.operation`.

## Constructors
- None.

## Methods
- `createLabel()`
  - Executes `createLabel` behavior.
- `createUnresolvedLabel()`
  - Executes `createUnresolvedLabel` behavior.
- `resolveLabel(@Nonnull Label label)`
  - Executes `resolveLabel` behavior.
- `jump(@Nonnull Label target)`
  - Executes `jump` behavior.
- `addOperation(@Nonnull Operation operation)`
  - Executes `addOperation` behavior.
- `addOperation(@Nonnull Operation operation, Label ... labels)`
  - Executes `addOperation` behavior.
- `build()`
  - Executes `build` behavior.
- `LabelOperation(Operation inner, Label[] labels)`
  - Executes `LabelOperation` behavior.
- `tick(@Nonnull Ref<EntityStore> ref, @Nonnull LivingEntity entity, boolean firstRun, float time, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `tick` behavior.
- `simulateTick(@Nonnull Ref<EntityStore> ref, @Nonnull LivingEntity entity, boolean firstRun, float time, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `simulateTick` behavior.
- `handle(@Nonnull Ref<EntityStore> ref, boolean firstRun, float time, @Nonnull InteractionType type, @Nonnull InteractionContext context)`
  - Executes `handle` behavior.
- `getWaitForDataFrom()`
  - Executes `getWaitForDataFrom` behavior.
- `getRules()`
  - Executes `getRules` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
