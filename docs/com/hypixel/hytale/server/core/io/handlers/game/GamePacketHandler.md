# GamePacketHandler

## Overview
- Documentation for `GamePacketHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.io.handlers.game`.

## Constructors
- `GamePacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, @Nonnull PlayerAuthentication auth)`
  - Creates a `GamePacketHandler` instance.

## Methods
- `getInteractionPacketQueue()`
  - Executes `getInteractionPacketQueue` behavior.
- `getPlayerRef()`
  - Executes `getPlayerRef` behavior.
- `setPlayerRef(@Nonnull PlayerRef playerRef, @Nonnull Player playerComponent)`
  - Executes `setPlayerRef` behavior.
- `getIdentifier()`
  - Executes `getIdentifier` behavior.
- `registerHandlers()`
  - Executes `registerHandlers` behavior.
- `closed(ChannelHandlerContext ctx)`
  - Executes `closed` behavior.
- `disconnect(@Nonnull String message)`
  - Executes `disconnect` behavior.
- `handle(@Nonnull Disconnect packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull MouseInteraction packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull ClientMovement packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull ChatMessage packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull RequestAssets packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull CustomPageEvent packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull ViewRadius packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull UpdateLanguage packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull ClientOpenWindow packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull SendWindowAction packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull SyncPlayerPreferences packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull ClientPlaceBlock packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull RemoveMapMarker packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull CloseWindow packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull UpdateServerAccess packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull SetServerAccess packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull RequestMachinimaActorModel packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull UpdateMachinimaScene packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull ClientReady packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull UpdateWorldMapVisible packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull TeleportToWorldMapMarker packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull TeleportToWorldMapPosition packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull SyncInteractionChains packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull MountMovement packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull SetPaused packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull RequestFlyCameraMode packet)`
  - Executes `handle` behavior.

## Notes
- No additional notes.
