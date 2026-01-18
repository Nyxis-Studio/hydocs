# ItemExistsValidator

## Overview
- Documentation for `ItemExistsValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators.asset`.

## Constructors
- `ItemExistsValidator()`
  - Creates a `ItemExistsValidator` instance.
- `ItemExistsValidator(boolean requireBlock, boolean allowDroplist)`
  - Creates a `ItemExistsValidator` instance.
- `ItemExistsValidator(EnumSet<AssetValidator.Config> config, boolean requireBlock, boolean allowDroplist)`
  - Creates a `ItemExistsValidator` instance.
- `ItemExistsValidator(true, false)`
  - Creates a `ItemExistsValidator` instance.
- `ItemExistsValidator(false, true)`
  - Creates a `ItemExistsValidator` instance.
- `ItemExistsValidator(config, false, false)`
  - Creates a `ItemExistsValidator` instance.
- `ItemExistsValidator(config, false, true)`
  - Creates a `ItemExistsValidator` instance.

## Methods
- `getDomain()`
  - Executes `getDomain` behavior.
- `test(String item)`
  - Executes `test` behavior.
- `errorMessage(String item, String attributeName)`
  - Executes `errorMessage` behavior.
- `getAssetName()`
  - Executes `getAssetName` behavior.
- `required()`
  - Executes `required` behavior.
- `requireBlock()`
  - Executes `requireBlock` behavior.
- `orDroplist()`
  - Executes `orDroplist` behavior.
- `withConfig(EnumSet<AssetValidator.Config> config)`
  - Executes `withConfig` behavior.
- `orDroplistWithConfig(EnumSet<AssetValidator.Config> config)`
  - Executes `orDroplistWithConfig` behavior.

## Notes
- No additional notes.
