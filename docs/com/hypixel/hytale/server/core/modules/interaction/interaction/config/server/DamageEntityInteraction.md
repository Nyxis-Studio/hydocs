# DamageEntityInteraction

## Overview
- Documentation for `DamageEntityInteraction`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.server`.

## Constructors
- `DamageEntityInteraction()`
  - Creates a `DamageEntityInteraction` instance.

## Methods
- `tick0(boolean firstRun, float time, @NonNullDecl InteractionType type, @Nonnull InteractionContext context, @NonNullDecl CooldownHandler cooldownHandler)`
  - Executes `tick0` behavior.
- `simulateTick0(boolean firstRun, float time, @NonNullDecl InteractionType type, @Nonnull InteractionContext context, @NonNullDecl CooldownHandler cooldownHandler)`
  - Executes `simulateTick0` behavior.
- `processDamage(@Nonnull InteractionContext context, @Nullable Damage[] queuedDamage)`
  - Executes `processDamage` behavior.
- `compile(@Nonnull OperationsBuilder builder)`
  - Executes `compile` behavior.
- `walk(@Nonnull Collector collector, @Nonnull InteractionContext context)`
  - Executes `walk` behavior.
- `configurePacket(com.hypixel.hytale.protocol.Interaction packet)`
  - Executes `configurePacket` behavior.
- `needsRemoteSync()`
  - Executes `needsRemoteSync` behavior.
- `getWaitForDataFrom()`
  - Executes `getWaitForDataFrom` behavior.
- `attemptEntityDamage0(@Nonnull Damage.Source source, @Nonnull InteractionContext context, @Nonnull Ref<EntityStore> attackerRef, @Nonnull Ref<EntityStore> targetRef, @Nullable Vector4d hit)`
  - Executes `attemptEntityDamage0` behavior.
- `calculateKnockbackAndArmorModifiers(@Nonnull DamageClass damageClass, @Nonnull Object2FloatMap<DamageCause> damage, @Nonnull Ref<EntityStore> targetRef, @Nonnull Ref<EntityStore> attackerRef, float[] armorDamageModifiers, double[] knockbackMultiplier, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `calculateKnockbackAndArmorModifiers` behavior.
- `toString()`
  - Executes `toString` behavior.
- `processEntityStatsOnHit(int hits, @Nonnull EntityStatMap statMap)`
  - Executes `processEntityStatsOnHit` behavior.

## Notes
- No additional notes.
