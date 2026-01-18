# EditorClient

## Overview
- Documentation for `EditorClient`.
- Declared as a class in `com.hypixel.hytale.builtin.asseteditor`.

## Constructors
- `EditorClient(String language, @Nonnull PlayerAuthentication auth, PacketHandler packetHandler)`
  - Creates a `EditorClient` instance.
- `EditorClient(String language, UUID uuid, String username, PacketHandler packetHandler)`
  - Creates a `EditorClient` instance.
- `EditorClient(@Nonnull PlayerRef playerRef)`
  - Creates a `EditorClient` instance.

## Methods
- `getLanguage()`
  - Executes `getLanguage` behavior.
- `setLanguage(String language)`
  - Executes `setLanguage` behavior.
- `getUuid()`
  - Executes `getUuid` behavior.
- `getUsername()`
  - Executes `getUsername` behavior.
- `getAuth()`
  - Executes `getAuth` behavior.
- `getPacketHandler()`
  - Executes `getPacketHandler` behavior.
- `tryGetPlayer()`
  - Executes `tryGetPlayer` behavior.
- `hasPermission(@Nonnull String id)`
  - Executes `hasPermission` behavior.
- `hasPermission(@Nonnull String id, boolean def)`
  - Executes `hasPermission` behavior.
- `sendPopupNotification(AssetEditorPopupNotificationType type, @Nonnull Message message)`
  - Executes `sendPopupNotification` behavior.
- `sendSuccessReply(int token)`
  - Executes `sendSuccessReply` behavior.
- `sendSuccessReply(int token, @Nullable Message message)`
  - Executes `sendSuccessReply` behavior.
- `sendFailureReply(int token, @Nonnull Message message)`
  - Executes `sendFailureReply` behavior.

## Notes
- No additional notes.
