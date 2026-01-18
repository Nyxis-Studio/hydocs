# CombatSupport

## Overview
- Documentation for `CombatSupport`.
- Declared as a class in `com.hypixel.hytale.server.npc.role.support`.

## Constructors
- `CombatSupport(NPCEntity parent, @Nonnull BuilderRole builder, @Nonnull BuilderSupport support)`
  - Creates a `CombatSupport` instance.

## Methods
- `isDealingFriendlyDamage()`
  - Executes `isDealingFriendlyDamage` behavior.
- `getDisableDamageGroups()`
  - Executes `getDisableDamageGroups` behavior.
- `isExecutingAttack()`
  - Executes `isExecutingAttack` behavior.
- `tick(double dt)`
  - Executes `tick` behavior.
- `getCanCauseDamage(@Nonnull Ref<EntityStore> attackerRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getCanCauseDamage` behavior.
- `setExecutingAttack(InteractionChain chain, boolean damageFriendlies, double attackPause)`
  - Executes `setExecutingAttack` behavior.
- `addAttackOverride(String attackSequence)`
  - Executes `addAttackOverride` behavior.
- `clearAttackOverrides()`
  - Executes `clearAttackOverrides` behavior.
- `getNextAttackOverride()`
  - Executes `getNextAttackOverride` behavior.

## Notes
- No additional notes.
