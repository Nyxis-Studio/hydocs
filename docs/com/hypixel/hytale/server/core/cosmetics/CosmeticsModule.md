# CosmeticsModule

## Overview
- Documentation for `CosmeticsModule`.
- Declared as a class in `com.hypixel.hytale.server.core.cosmetics`.

## Constructors
- `CosmeticsModule(@Nonnull JavaPluginInit init)`
  - Creates a `CosmeticsModule` instance.

## Methods
- `setup()`
  - Executes `setup` behavior.
- `getRegistry()`
  - Executes `getRegistry` behavior.
- `validateGeneratedSkin(@Nonnull LoadAssetEvent eventType)`
  - Executes `validateGeneratedSkin` behavior.
- `createRandomModel(@Nonnull Random random)`
  - Executes `createRandomModel` behavior.
- `createModel(@Nonnull PlayerSkin skin)`
  - Executes `createModel` behavior.
- `createModel(@Nonnull PlayerSkin skin, float scale)`
  - Executes `createModel` behavior.
- `validateSkin(@Nonnull PlayerSkin skin)`
  - Executes `validateSkin` behavior.
- `isValidAttachment(@Nonnull Map<String, PlayerSkinPart> map, String id)`
  - Executes `isValidAttachment` behavior.
- `isValidTexture(@Nonnull PlayerSkinPart part, String variantId, String textureId)`
  - Executes `isValidTexture` behavior.
- `isValidAttachment(@Nonnull Map<String, PlayerSkinPart> map, @Nullable String id, boolean required)`
  - Executes `isValidAttachment` behavior.
- `isValidHaircutAttachment(@Nullable String haircutId, @Nullable String headAccessoryId)`
  - Executes `isValidHaircutAttachment` behavior.
- `get()`
  - Executes `get` behavior.
- `generateRandomSkin(@Nonnull Random random)`
  - Executes `generateRandomSkin` behavior.
- `randomSkinPart(@Nonnull Map<String, PlayerSkinPart> map, @Nonnull Random random)`
  - Executes `randomSkinPart` behavior.
- `randomSkinPart(@Nonnull Map<String, PlayerSkinPart> map, boolean required, @Nonnull Random random)`
  - Executes `randomSkinPart` behavior.
- `randomSkinPart(@Nonnull Map<String, PlayerSkinPart> map, boolean required, boolean color, @Nonnull Random random)`
  - Executes `randomSkinPart` behavior.

## Notes
- No additional notes.
