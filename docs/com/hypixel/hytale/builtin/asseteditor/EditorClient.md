**Source Hash:** `95a2b0c49a82444547e027d41b1d3c3a11cf462cd36ade71ac1b362f94443483`

# EditorClient

## Overview

## Constructor Descriptions
- `EditorClient(String language, @Nonnull PlayerAuthentication auth, PacketHandler packetHandler)`
  - Creates a `EditorClient` instance.
- `EditorClient(String language, UUID uuid, String username, PacketHandler packetHandler)`
  - Creates a `EditorClient` instance.
- `EditorClient(@Nonnull PlayerRef playerRef)`
  - Creates a `EditorClient` instance.

## Method Descriptions
- `getLanguage()`: Add description.
  - Executes `getLanguage` behavior.
- `setLanguage(String language)`: Add description.
  - Executes `setLanguage` behavior.
- `getUuid()`: Add description.
  - Executes `getUuid` behavior.
- `getUsername()`: Add description.
  - Executes `getUsername` behavior.
- `getAuth()`: Add description.
  - Executes `getAuth` behavior.
- `getPacketHandler()`: Add description.
  - Executes `getPacketHandler` behavior.
- `tryGetPlayer()`: Add description.
  - Executes `tryGetPlayer` behavior.
- `hasPermission(@Nonnull String id)`: Add description.
  - Executes `hasPermission` behavior.
- `hasPermission(@Nonnull String id, boolean def)`: Add description.
  - Executes `hasPermission` behavior.
- `sendPopupNotification(AssetEditorPopupNotificationType type, @Nonnull Message message)`: Add description.
  - Executes `sendPopupNotification` behavior.
- `sendSuccessReply(int token)`: Add description.
  - Executes `sendSuccessReply` behavior.
- `sendSuccessReply(int token, @Nullable Message message)`: Add description.
  - Executes `sendSuccessReply` behavior.
- `sendFailureReply(int token, @Nonnull Message message)`: Add description.
  - Executes `sendFailureReply` behavior.

## Notes
- No additional notes.
