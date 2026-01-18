**Source Hash:** `097ea61c42dbc42b84684b90a35a81a79de41201bd58bc7ab35aa4847bd1cf8a`

# ToolOperation

## Overview

## Constructor Descriptions
- `ToolOperation(@Nonnull Ref<EntityStore> ref, @Nonnull BuilderToolOnUseInteraction packet, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Creates a `ToolOperation` instance.

## Method Descriptions
- `getOrCreatePrototypeSettings(UUID playerUuid)`: Add description.
  - Executes `getOrCreatePrototypeSettings` behavior.
- `calculateInterpolatedPositions(@Nullable Vector3i lastPosition, @Nonnull Vector3i currentPosition, int brushWidth, int brushHeight, int brushSpacing)`: Add description.
  - Executes `calculateInterpolatedPositions` behavior.
- `getPosition()`: Add description.
  - Executes `getPosition` behavior.
- `getBrushWidth()`: Add description.
  - Executes `getBrushWidth` behavior.
- `getBrushHeight()`: Add description.
  - Executes `getBrushHeight` behavior.
- `getBrushSpacing()`: Add description.
  - Executes `getBrushSpacing` behavior.
- `getBrushDensity()`: Add description.
  - Executes `getBrushDensity` behavior.
- `executeAsBrushConfig(@Nonnull PrototypePlayerBuilderToolSettings prototypePlayerBuilderToolSettings, @Nonnull BuilderToolOnUseInteraction packet, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `executeAsBrushConfig` behavior.
- `getPattern(@Nonnull BuilderToolOnUseInteraction packet, @Nonnull BrushData.Values brush)`: Add description.
  - Executes `getPattern` behavior.
- `getTargetBlockAvoidingPaint(@Nonnull Ref<EntityStore> ref, double maxDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor, float raycastOriginX, float raycastOriginY, float raycastOriginZ, float raycastDirectionX, float raycastDirectionY, float raycastDirectionZ)`: Add description.
  - Executes `getTargetBlockAvoidingPaint` behavior.
- `getEditOperation()`: Add description.
  - Executes `getEditOperation` behavior.
- `test(int x, int y, int z, Void aVoid)`: Add description.
  - Executes `test` behavior.
- `execute0(int var1, int var2, int var3)`: Add description.
  - Executes `execute0` behavior.
- `execute(ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `execute` behavior.
- `executeAt(int posX, int posY, int posZ, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `executeAt` behavior.
- `executeShapeOperation(int x, int y, int z, @Nonnull TriIntObjPredicate<Void> operation, @Nonnull BrushShape shape, int shapeRange, int shapeHeight, int shapeThickness, boolean capped)`: Add description.
  - Executes `executeShapeOperation` behavior.
- `getOffsets(int width, int height, boolean originRotation, BrushOrigin origin, @Nonnull Transform transform, @Nonnull Vector3i vector, boolean applyBottomOriginFix)`: Add description.
  - Executes `getOffsets` behavior.
- `getTransform(@Nonnull Ref<EntityStore> ref, @Nonnull BrushData.Values brushData, @Nonnull Vector3i vector, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getTransform` behavior.
- `getRotation(@Nonnull Ref<EntityStore> ref, @Nonnull BrushData.Values brushData, @Nonnull Vector3i vector, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getRotation` behavior.
- `getMirror(@Nonnull Ref<EntityStore> ref, @Nonnull BrushData.Values brushData, @Nonnull Vector3i vector, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getMirror` behavior.
- `fromPacket(@Nonnull Ref<EntityStore> ref, @Nonnull Player player, @Nonnull BuilderToolOnUseInteraction packet, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `fromPacket` behavior.
- `combineMasks(@Nullable BrushData.Values brush, @Nullable BlockMask globalMask)`: Add description.
  - Executes `combineMasks` behavior.

## Notes
- No additional notes.
