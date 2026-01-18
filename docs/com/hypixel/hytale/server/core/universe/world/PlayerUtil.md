**Source Hash:** `e8379e89864ad93e27136343cab14b75b2ef0d3f61b767405d89c329698e0c89`

# PlayerUtil

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `forEachPlayerThatCanSeeEntity(@Nonnull Ref<EntityStore> ref, @Nonnull TriConsumer<Ref<EntityStore>, PlayerRef, ComponentAccessor<EntityStore>> consumer, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `forEachPlayerThatCanSeeEntity` behavior.
- `forEachPlayerThatCanSeeEntity(@Nonnull Ref<EntityStore> ref, @Nonnull TriConsumer<Ref<EntityStore>, PlayerRef, ComponentAccessor<EntityStore>> consumer, @Nullable Ref<EntityStore> ignoredPlayerRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `forEachPlayerThatCanSeeEntity` behavior.
- `broadcastMessageToPlayers(@Nullable UUID sourcePlayerUuid, @Nonnull Message message, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `broadcastMessageToPlayers` behavior.
- `broadcastPacketToPlayers(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Packet packet)`: Add description.
  - Executes `broadcastPacketToPlayers` behavior.
- `broadcastPacketToPlayersNoCache(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Packet packet)`: Add description.
  - Executes `broadcastPacketToPlayersNoCache` behavior.
- `broadcastPacketToPlayers(@Nonnull ComponentAccessor<EntityStore> componentAccessor, Packet ... packets)`: Add description.
  - Executes `broadcastPacketToPlayers` behavior.
- `resetPlayerModel(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `resetPlayerModel` behavior.

## Notes
- No additional notes.
