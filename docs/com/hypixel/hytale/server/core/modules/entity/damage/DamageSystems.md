# DamageSystems

## Overview
- Documentation for `DamageSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.damage`.

## Constructors
- None.

## Methods
- `executeDamage(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Damage damage)`
  - Executes `executeDamage` behavior.
- `executeDamage(int index, @Nonnull ArchetypeChunk<EntityStore> chunk, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage damage)`
  - Executes `executeDamage` behavior.
- `executeDamage(@Nonnull Ref<EntityStore> ref, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage damage)`
  - Executes `executeDamage` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `handle(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage damage)`
  - Executes `handle` behavior.
- `getResistanceModifiers(@Nonnull World world, @Nonnull ItemContainer inventory, boolean canApplyItemStackPenalties, @Nullable EffectControllerComponent effectControllerComponent)`
  - Executes `getResistanceModifiers` behavior.
- `calculateResistanceEntryModifications(@Nonnull Map.Entry<DamageCause, StaticModifier[]> entry, @Nonnull World world, @Nonnull Map<DamageCause, ArmorResistanceModifiers> result, boolean canApplyItemStackPenalties, boolean itemStackIsBroken, double flatResistance)`
  - Executes `calculateResistanceEntryModifications` behavior.
- `addResistanceModifiersFromEntityEffects(Map<DamageCause, ArmorResistanceModifiers> resistanceModifiers, EffectControllerComponent effectControllerComponent)`
  - Executes `addResistanceModifiersFromEntityEffects` behavior.
- `handle(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage event)`
  - Executes `handle` behavior.
- `handleInternal(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage damage)`
  - Executes `handleInternal` behavior.
- `handle(int index, @NonNullDecl ArchetypeChunk<EntityStore> archetypeChunk, @NonNullDecl Store<EntityStore> store, @NonNullDecl CommandBuffer<EntityStore> commandBuffer, @NonNullDecl Damage event)`
  - Executes `handle` behavior.
- `queueUpdateFor(@Nonnull Ref<EntityStore> ref, float damageAmount, @Nullable Float hitAngleDeg, @Nonnull EntityTrackerSystems.EntityViewer viewer)`
  - Executes `queueUpdateFor` behavior.
- `tick(float dt, int systemIndex, @NonNullDecl Store<EntityStore> store)`
  - Executes `tick` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.

## Notes
- No additional notes.
