# I18nModule

## Overview
- Documentation for `I18nModule`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.i18n`.

## Constructors
- `I18nModule(@Nonnull JavaPluginInit parent)`
  - Creates a `I18nModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `start()`
  - Executes `start` behavior.
- `loadMessagesFromPack(AssetPack pack)`
  - Executes `loadMessagesFromPack` behavior.
- `getUpdatePacketsForChanges(String languageKey, @Nonnull Map<String, Map<String, String>> changed, @Nonnull Map<String, Map<String, String>> removed)`
  - Executes `getUpdatePacketsForChanges` behavior.
- `addDefaultMessages(@Nonnull Map<String, String> messages, boolean isInitial)`
  - Executes `addDefaultMessages` behavior.
- `loadMessages(String languageKey, @Nonnull Path languagePath)`
  - Executes `loadMessages` behavior.
- `loadMessagesFrom(@Nonnull Map<String, String> messages, String prefix, @Nonnull Path path)`
  - Executes `loadMessagesFrom` behavior.
- `getPrefix(@Nonnull Path languagePath, @Nonnull Path path)`
  - Executes `getPrefix` behavior.
- `getMessages(String language)`
  - Executes `getMessages` behavior.
- `getMessages(@Nonnull Map<String, Map<String, String>> languageMap, @Nullable String language)`
  - Executes `getMessages` behavior.
- `sendTranslations(@Nonnull PacketHandler packetHandler, String language)`
  - Executes `sendTranslations` behavior.
- `getMessage(String language, @Nonnull String key)`
  - Executes `getMessage` behavior.
- `getKey()`
  - Executes `getKey` behavior.
- `test(Path path, EventKind eventKind)`
  - Executes `test` behavior.
- `accept(Map<Path, EventKind> map)`
  - Executes `accept` behavior.

## Notes
- No additional notes.
