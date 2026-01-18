# Blackboard

## Overview
- Documentation for `Blackboard`.
- Declared as a class in `com.hypixel.hytale.server.npc.blackboard`.

## Constructors
- `Blackboard()`
  - Creates a `Blackboard` instance.

## Methods
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `init(@Nonnull World world)`
  - Executes `init` behavior.
- `onEntityDamageBlock(@Nonnull Ref<EntityStore> ref, @Nonnull DamageBlockEvent event)`
  - Executes `onEntityDamageBlock` behavior.
- `onEntityBreakBlock(@Nonnull Ref<EntityStore> ref, @Nonnull BreakBlockEvent event)`
  - Executes `onEntityBreakBlock` behavior.
- `registerViewType(@Nonnull Class<View> clazz, @Nonnull IBlackboardViewManager<View> holder)`
  - Executes `registerViewType` behavior.
- `cleanupViews()`
  - Executes `cleanupViews` behavior.
- `clear()`
  - Executes `clear` behavior.
- `onWorldRemoved()`
  - Executes `onWorldRemoved` behavior.
- `forEachView(Class<View> viewTypeClass, Consumer<View> consumer)`
  - Executes `forEachView` behavior.
- `getView(Class<View> viewTypeClass, Ref<EntityStore> ref, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getView` behavior.
- `getView(Class<View> viewTypeClass, int chunkX, int chunkZ)`
  - Executes `getView` behavior.
- `getView(Class<View> viewTypeClass, long index)`
  - Executes `getView` behavior.
- `getIfExists(Class<View> viewTypeClass, long index)`
  - Executes `getIfExists` behavior.
- `getViewManager(Class<View> viewTypeClass)`
  - Executes `getViewManager` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
