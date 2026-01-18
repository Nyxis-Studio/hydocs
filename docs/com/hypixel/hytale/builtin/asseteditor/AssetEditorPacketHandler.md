**Source Hash:** `2a28efcbbac391c9c8004ad54126ceb6166efa40cdb12c4a402f2610fe8f82c1`

# AssetEditorPacketHandler

## Overview

## Constructor Descriptions
- `AssetEditorPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, @Nonnull PlayerAuthentication auth)`
  - Creates a `AssetEditorPacketHandler` instance.
- `AssetEditorPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, UUID uuid, String username)`
  - Creates a `AssetEditorPacketHandler` instance.
- `AssetEditorPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, UUID uuid, String username, byte[] referralData, HostAddress referralSource)`
  - Creates a `AssetEditorPacketHandler` instance.

## Method Descriptions
- `init()`: Add description.
  - Executes `init` behavior.
- `getEditorClient()`: Add description.
  - Executes `getEditorClient` behavior.
- `getIdentifier()`: Add description.
  - Executes `getIdentifier` behavior.
- `closed(ChannelHandlerContext ctx)`: Add description.
  - Executes `closed` behavior.
- `registerHandlers()`: Add description.
  - Executes `registerHandlers` behavior.
- `handle(@Nonnull AssetEditorSubscribeModifiedAssetsChanges packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUndoChanges packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRedoChanges packet)`: Add description.
  - Executes `handle` behavior.
- `handle(AssetEditorFetchLastModifiedAssets packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorExportAssets packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorCreateAsset packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorFetchAsset packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorFetchJsonAssetWithParents packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRequestChildrenList packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUpdateAsset packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUpdateJsonAsset packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorFetchAutoCompleteData packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRenameAsset packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorDeleteAsset packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorActivateButton packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRequestDataset packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorSelectAsset packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorCreateDirectory packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorDeleteDirectory packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRenameDirectory packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull UpdateLanguage packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorSetGameTime packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUpdateWeatherPreviewLock packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUpdateAssetPack packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorDeleteAssetPack packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorCreateAssetPack packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull Disconnect packet)`: Add description.
  - Executes `handle` behavior.
- `lacksPermission(int token)`: Add description.
  - Executes `lacksPermission` behavior.
- `lacksPermission()`: Add description.
  - Executes `lacksPermission` behavior.
- `lacksPermission(String permissionId)`: Add description.
  - Executes `lacksPermission` behavior.
- `lacksPermission(int token, String permissionId)`: Add description.
  - Executes `lacksPermission` behavior.

## Notes
- No additional notes.
