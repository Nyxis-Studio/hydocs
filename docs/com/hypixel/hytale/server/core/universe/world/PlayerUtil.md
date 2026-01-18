# PlayerUtil

## Overview
- Documentation for `PlayerUtil`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world`.

## Constructors
- None.

## Methods
- `forEachPlayerThatCanSeeEntity(@Nonnull Ref<EntityStore> ref, @Nonnull TriConsumer<Ref<EntityStore>, PlayerRef, ComponentAccessor<EntityStore>> consumer, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `forEachPlayerThatCanSeeEntity` behavior.
- `forEachPlayerThatCanSeeEntity(@Nonnull Ref<EntityStore> ref, @Nonnull TriConsumer<Ref<EntityStore>, PlayerRef, ComponentAccessor<EntityStore>> consumer, @Nullable Ref<EntityStore> ignoredPlayerRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `forEachPlayerThatCanSeeEntity` behavior.
- `broadcastMessageToPlayers(@Nullable UUID sourcePlayerUuid, @Nonnull Message message, @Nonnull Store<EntityStore> store)`
  - Executes `broadcastMessageToPlayers` behavior.
- `broadcastPacketToPlayers(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Packet packet)`
  - Executes `broadcastPacketToPlayers` behavior.
- `broadcastPacketToPlayersNoCache(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Packet packet)`
  - Executes `broadcastPacketToPlayersNoCache` behavior.
- `broadcastPacketToPlayers(@Nonnull ComponentAccessor<EntityStore> componentAccessor, Packet ... packets)`
  - Executes `broadcastPacketToPlayers` behavior.
- `resetPlayerModel(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `resetPlayerModel` behavior.

## Notes
- No additional notes.
