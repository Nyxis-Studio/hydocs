# AssetEditorPacketHandler

## Overview
- Documentation for `AssetEditorPacketHandler`.
- Declared as a class in `com.hypixel.hytale.builtin.asseteditor`.

## Constructors
- `AssetEditorPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, @Nonnull PlayerAuthentication auth)`
  - Creates a `AssetEditorPacketHandler` instance.
- `AssetEditorPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, UUID uuid, String username)`
  - Creates a `AssetEditorPacketHandler` instance.
- `AssetEditorPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, UUID uuid, String username, byte[] referralData, HostAddress referralSource)`
  - Creates a `AssetEditorPacketHandler` instance.

## Methods
- `init()`
  - Executes `init` behavior.
- `getEditorClient()`
  - Executes `getEditorClient` behavior.
- `getIdentifier()`
  - Executes `getIdentifier` behavior.
- `closed(ChannelHandlerContext ctx)`
  - Executes `closed` behavior.
- `registerHandlers()`
  - Executes `registerHandlers` behavior.
- `handle(@Nonnull AssetEditorSubscribeModifiedAssetsChanges packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUndoChanges packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRedoChanges packet)`
  - Executes `handle` behavior.
- `handle(AssetEditorFetchLastModifiedAssets packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorExportAssets packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorCreateAsset packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorFetchAsset packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorFetchJsonAssetWithParents packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRequestChildrenList packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUpdateAsset packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUpdateJsonAsset packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorFetchAutoCompleteData packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRenameAsset packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorDeleteAsset packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorActivateButton packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRequestDataset packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorSelectAsset packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorCreateDirectory packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorDeleteDirectory packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorRenameDirectory packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull UpdateLanguage packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorSetGameTime packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUpdateWeatherPreviewLock packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorUpdateAssetPack packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorDeleteAssetPack packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AssetEditorCreateAssetPack packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull Disconnect packet)`
  - Executes `handle` behavior.
- `lacksPermission(int token)`
  - Executes `lacksPermission` behavior.
- `lacksPermission()`
  - Executes `lacksPermission` behavior.
- `lacksPermission(String permissionId)`
  - Executes `lacksPermission` behavior.
- `lacksPermission(int token, String permissionId)`
  - Executes `lacksPermission` behavior.

## Notes
- No additional notes.
