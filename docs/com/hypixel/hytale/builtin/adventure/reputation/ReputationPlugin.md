# ReputationPlugin

## Overview
- Documentation for `ReputationPlugin`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.reputation`.

## Constructors
- `ReputationPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `ReputationPlugin` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `getReputationGroupComponentType()`
  - Executes `getReputationGroupComponentType` behavior.
- `setup()`
  - Executes `setup` behavior.
- `start()`
  - Executes `start` behavior.
- `changeReputation(@Nonnull Player player, @Nonnull Ref<EntityStore> npcRef, int value, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `changeReputation` behavior.
- `changeReputation(@Nonnull Player player, @Nonnull String reputationGroupId, int value, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `changeReputation` behavior.
- `changeReputation(@Nonnull World world, @Nonnull String reputationGroupId, int value)`
  - Executes `changeReputation` behavior.
- `computeReputation(@Nonnull Object2IntMap<String> reputationData, @Nonnull ReputationGroup reputationGroup, int value)`
  - Executes `computeReputation` behavior.
- `getReputationValue(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> playerEntityRef, @Nonnull Ref<EntityStore> npcEntityRef)`
  - Executes `getReputationValue` behavior.
- `getReputationValue(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> playerEntityRef, @Nonnull String reputationGroupId)`
  - Executes `getReputationValue` behavior.
- `getReputationValue(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> npcRef)`
  - Executes `getReputationValue` behavior.
- `getReputationValue(@Nonnull Store<EntityStore> store, String reputationGroupId)`
  - Executes `getReputationValue` behavior.
- `getReputationValueForGroup(@Nonnull Object2IntMap<String> reputationData, @Nonnull ReputationGroup reputationGroup)`
  - Executes `getReputationValueForGroup` behavior.
- `getReputationRank(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> npcRef)`
  - Executes `getReputationRank` behavior.
- `getReputationRank(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull String reputationGroupId)`
  - Executes `getReputationRank` behavior.
- `getReputationRankFromValue(int value)`
  - Executes `getReputationRankFromValue` behavior.
- `getReputationRank(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> npcRef)`
  - Executes `getReputationRank` behavior.
- `getAttitude(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> npc)`
  - Executes `getAttitude` behavior.
- `getAttitude(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> npcRef)`
  - Executes `getAttitude` behavior.

## Notes
- No additional notes.
