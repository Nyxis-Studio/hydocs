# ToolOperation

## Overview
- Documentation for `ToolOperation`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.tooloperations`.

## Constructors
- `ToolOperation(@Nonnull Ref<EntityStore> ref, @Nonnull BuilderToolOnUseInteraction packet, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Creates a `ToolOperation` instance.

## Methods
- `getOrCreatePrototypeSettings(UUID playerUuid)`
  - Executes `getOrCreatePrototypeSettings` behavior.
- `calculateInterpolatedPositions(@Nullable Vector3i lastPosition, @Nonnull Vector3i currentPosition, int brushWidth, int brushHeight, int brushSpacing)`
  - Executes `calculateInterpolatedPositions` behavior.
- `getPosition()`
  - Executes `getPosition` behavior.
- `getBrushWidth()`
  - Executes `getBrushWidth` behavior.
- `getBrushHeight()`
  - Executes `getBrushHeight` behavior.
- `getBrushSpacing()`
  - Executes `getBrushSpacing` behavior.
- `getBrushDensity()`
  - Executes `getBrushDensity` behavior.
- `executeAsBrushConfig(@Nonnull PrototypePlayerBuilderToolSettings prototypePlayerBuilderToolSettings, @Nonnull BuilderToolOnUseInteraction packet, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `executeAsBrushConfig` behavior.
- `getPattern(@Nonnull BuilderToolOnUseInteraction packet, @Nonnull BrushData.Values brush)`
  - Executes `getPattern` behavior.
- `getTargetBlockAvoidingPaint(@Nonnull Ref<EntityStore> ref, double maxDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor, float raycastOriginX, float raycastOriginY, float raycastOriginZ, float raycastDirectionX, float raycastDirectionY, float raycastDirectionZ)`
  - Executes `getTargetBlockAvoidingPaint` behavior.
- `getEditOperation()`
  - Executes `getEditOperation` behavior.
- `test(int x, int y, int z, Void aVoid)`
  - Executes `test` behavior.
- `execute0(int var1, int var2, int var3)`
  - Executes `execute0` behavior.
- `execute(ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `execute` behavior.
- `executeAt(int posX, int posY, int posZ, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `executeAt` behavior.
- `executeShapeOperation(int x, int y, int z, @Nonnull TriIntObjPredicate<Void> operation, @Nonnull BrushShape shape, int shapeRange, int shapeHeight, int shapeThickness, boolean capped)`
  - Executes `executeShapeOperation` behavior.
- `getOffsets(int width, int height, boolean originRotation, BrushOrigin origin, @Nonnull Transform transform, @Nonnull Vector3i vector, boolean applyBottomOriginFix)`
  - Executes `getOffsets` behavior.
- `getTransform(@Nonnull Ref<EntityStore> ref, @Nonnull BrushData.Values brushData, @Nonnull Vector3i vector, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getTransform` behavior.
- `getRotation(@Nonnull Ref<EntityStore> ref, @Nonnull BrushData.Values brushData, @Nonnull Vector3i vector, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getRotation` behavior.
- `getMirror(@Nonnull Ref<EntityStore> ref, @Nonnull BrushData.Values brushData, @Nonnull Vector3i vector, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getMirror` behavior.
- `fromPacket(@Nonnull Ref<EntityStore> ref, @Nonnull Player player, @Nonnull BuilderToolOnUseInteraction packet, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `fromPacket` behavior.
- `combineMasks(@Nullable BrushData.Values brush, @Nullable BlockMask globalMask)`
  - Executes `combineMasks` behavior.

## Notes
- No additional notes.
