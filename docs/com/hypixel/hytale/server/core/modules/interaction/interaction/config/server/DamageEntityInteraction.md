**Source Hash:** `3c86ad4b51fbf0e6f8bdcb29e64a19208005fa940fbb3a3fc194c78b5beaa26e`

# DamageEntityInteraction

## Overview

## Constructor Descriptions
- `DamageEntityInteraction()`
  - Creates a `DamageEntityInteraction` instance.

## Method Descriptions
- `tick0(boolean firstRun, float time, @NonNullDecl InteractionType type, @Nonnull InteractionContext context, @NonNullDecl CooldownHandler cooldownHandler)`: Add description.
  - Executes `tick0` behavior.
- `simulateTick0(boolean firstRun, float time, @NonNullDecl InteractionType type, @Nonnull InteractionContext context, @NonNullDecl CooldownHandler cooldownHandler)`: Add description.
  - Executes `simulateTick0` behavior.
- `processDamage(@Nonnull InteractionContext context, @Nullable Damage[] queuedDamage)`: Add description.
  - Executes `processDamage` behavior.
- `compile(@Nonnull OperationsBuilder builder)`: Add description.
  - Executes `compile` behavior.
- `walk(@Nonnull Collector collector, @Nonnull InteractionContext context)`: Add description.
  - Executes `walk` behavior.
- `configurePacket(com.hypixel.hytale.protocol.Interaction packet)`: Add description.
  - Executes `configurePacket` behavior.
- `needsRemoteSync()`: Add description.
  - Executes `needsRemoteSync` behavior.
- `getWaitForDataFrom()`: Add description.
  - Executes `getWaitForDataFrom` behavior.
- `attemptEntityDamage0(@Nonnull Damage.Source source, @Nonnull InteractionContext context, @Nonnull Ref<EntityStore> attackerRef, @Nonnull Ref<EntityStore> targetRef, @Nullable Vector4d hit)`: Add description.
  - Executes `attemptEntityDamage0` behavior.
- `calculateKnockbackAndArmorModifiers(@Nonnull DamageClass damageClass, @Nonnull Object2FloatMap<DamageCause> damage, @Nonnull Ref<EntityStore> targetRef, @Nonnull Ref<EntityStore> attackerRef, float[] armorDamageModifiers, double[] knockbackMultiplier, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `calculateKnockbackAndArmorModifiers` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `processEntityStatsOnHit(int hits, @Nonnull EntityStatMap statMap)`: Add description.
  - Executes `processEntityStatsOnHit` behavior.

## Notes
- No additional notes.
