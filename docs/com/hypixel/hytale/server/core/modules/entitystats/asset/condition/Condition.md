# Condition

## Overview
- Documentation for `Condition`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entitystats.asset.condition`.

## Constructors
- `Condition()`
  - Creates a `Condition` instance.
- `Condition(boolean inverse)`
  - Creates a `Condition` instance.

## Methods
- `eval(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> ref, @Nonnull Instant currentTime)`
  - Executes `eval` behavior.
- `eval0(@Nonnull ComponentAccessor<EntityStore> var1, @Nonnull Ref<EntityStore> var2, @Nonnull Instant var3)`
  - Executes `eval0` behavior.
- `allConditionsMet(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> ref, @Nonnull Instant currentTime, @Nonnull EntityStatType.Regenerating regenerating)`
  - Executes `allConditionsMet` behavior.
- `allConditionsMet(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> ref, @Nonnull Instant currentTime, @Nonnull Condition[] conditions)`
  - Executes `allConditionsMet` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
