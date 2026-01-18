**Source Hash:** `7616179e495d72fce06c3bd3e989122d7b559133b421feaa3272abfdea6a654b`

# Model

## Overview

## Constructor Descriptions
- `Model(String modelAssetId, float scale, Map<String, String> randomAttachmentIds, ModelAttachment[] attachments, @Nullable Box boundingBox, String model, String texture, String gradientSet, String gradientId, float eyeHeight, float crouchOffset, Map<String, ModelAsset.AnimationSet> animationSetMap, CameraSettings camera, ColorLight light, ModelParticle[] particles, ModelTrail[] trails, PhysicsValues physicsValues, Map<String, DetailBox[]> detailBoxes, Phobia phobia, String phobiaModelAssetId)`
  - Creates a `Model` instance.
- `Model(@Nonnull Model other)`
  - Creates a `Model` instance.
- `Model()`
  - Creates a `Model` instance.
- `Model(modelAsset.getId()`
  - Creates a `Model` instance.

## Method Descriptions
- `getModelAssetId()`: Add description.
  - Executes `getModelAssetId` behavior.
- `getScale()`: Add description.
  - Executes `getScale` behavior.
- `getRandomAttachmentIds()`: Add description.
  - Executes `getRandomAttachmentIds` behavior.
- `getAttachments()`: Add description.
  - Executes `getAttachments` behavior.
- `getBoundingBox(@Nullable MovementStates movementStates)`: Add description.
  - Executes `getBoundingBox` behavior.
- `getBoundingBox()`: Add description.
  - Executes `getBoundingBox` behavior.
- `getCrouchBoundingBox()`: Add description.
  - Executes `getCrouchBoundingBox` behavior.
- `getModel()`: Add description.
  - Executes `getModel` behavior.
- `getTexture()`: Add description.
  - Executes `getTexture` behavior.
- `getGradientSet()`: Add description.
  - Executes `getGradientSet` behavior.
- `getGradientId()`: Add description.
  - Executes `getGradientId` behavior.
- `getEyeHeight()`: Add description.
  - Executes `getEyeHeight` behavior.
- `getCrouchOffset()`: Add description.
  - Executes `getCrouchOffset` behavior.
- `getFirstBoundAnimationId(@Nullable String id, @Nullable String fallbackId)`: Add description.
  - Executes `getFirstBoundAnimationId` behavior.
- `getFirstBoundAnimationId(String ... preferenceOrder)`: Add description.
  - Executes `getFirstBoundAnimationId` behavior.
- `getCamera()`: Add description.
  - Executes `getCamera` behavior.
- `getLight()`: Add description.
  - Executes `getLight` behavior.
- `getParticles()`: Add description.
  - Executes `getParticles` behavior.
- `getTrails()`: Add description.
  - Executes `getTrails` behavior.
- `getPhysicsValues()`: Add description.
  - Executes `getPhysicsValues` behavior.
- `getDetailBoxes()`: Add description.
  - Executes `getDetailBoxes` behavior.
- `getPhobia()`: Add description.
  - Executes `getPhobia` behavior.
- `getPhobiaModelAssetId()`: Add description.
  - Executes `getPhobiaModelAssetId` behavior.
- `toReference()`: Add description.
  - Executes `toReference` behavior.
- `getEyeHeight(@Nullable Ref<EntityStore> ref, @Nullable ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getEyeHeight` behavior.
- `equals(@Nullable Object o)`: Add description.
  - Executes `equals` behavior.
- `hashCode()`: Add description.
  - Executes `hashCode` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `createRandomScaleModel(@Nonnull ModelAsset modelAsset)`: Add description.
  - Executes `createRandomScaleModel` behavior.
- `createStaticScaledModel(@Nonnull ModelAsset modelAsset, float scale)`: Add description.
  - Executes `createStaticScaledModel` behavior.
- `createUnitScaleModel(@Nonnull ModelAsset modelAsset)`: Add description.
  - Executes `createUnitScaleModel` behavior.
- `createUnitScaleModel(@Nonnull ModelAsset modelAsset, @Nullable Box boundingBox)`: Add description.
  - Executes `createUnitScaleModel` behavior.
- `createScaledModel(@Nonnull ModelAsset modelAsset, float scale)`: Add description.
  - Executes `createScaledModel` behavior.
- `createScaledModel(@Nonnull ModelAsset modelAsset, float scale, @Nullable Map<String, String> randomAttachmentIds)`: Add description.
  - Executes `createScaledModel` behavior.
- `createScaledModel(@Nonnull ModelAsset modelAsset, float scale, @Nullable Map<String, String> randomAttachmentIds, @Nullable Box overrideBoundingBox)`: Add description.
  - Executes `createScaledModel` behavior.
- `createScaledModel(@Nonnull ModelAsset modelAsset, float scale, @Nullable Map<String, String> randomAttachmentIds, @Nullable Box overrideBoundingBox, boolean staticModel)`: Add description.
  - Executes `createScaledModel` behavior.
- `isStaticModel()`: Add description.
  - Executes `isStaticModel` behavior.
- `toModel()`: Add description.
  - Executes `toModel` behavior.

## Notes
- No additional notes.
