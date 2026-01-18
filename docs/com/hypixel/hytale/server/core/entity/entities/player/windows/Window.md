# Window

## Overview
- Documentation for `Window`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities.player.windows`.

## Constructors
- `Window(@Nonnull WindowType windowType)`
  - Creates a `Window` instance.

## Methods
- `init(@Nonnull PlayerRef playerRef, @Nonnull WindowManager manager)`
  - Executes `init` behavior.
- `getData()`
  - Executes `getData` behavior.
- `onOpen0()`
  - Executes `onOpen0` behavior.
- `onClose0()`
  - Executes `onClose0` behavior.
- `onOpen()`
  - Executes `onOpen` behavior.
- `onClose()`
  - Executes `onClose` behavior.
- `handleAction(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull WindowAction action)`
  - Executes `handleAction` behavior.
- `getType()`
  - Executes `getType` behavior.
- `setId(int id)`
  - Executes `setId` behavior.
- `getId()`
  - Executes `getId` behavior.
- `getPlayerRef()`
  - Executes `getPlayerRef` behavior.
- `close()`
  - Executes `close` behavior.
- `invalidate()`
  - Executes `invalidate` behavior.
- `setNeedRebuild()`
  - Executes `setNeedRebuild` behavior.
- `consumeIsDirty()`
  - Executes `consumeIsDirty` behavior.
- `consumeNeedRebuild()`
  - Executes `consumeNeedRebuild` behavior.
- `registerCloseEvent(@Nonnull Consumer<WindowCloseEvent> consumer)`
  - Executes `registerCloseEvent` behavior.
- `registerCloseEvent(short priority, @Nonnull Consumer<WindowCloseEvent> consumer)`
  - Executes `registerCloseEvent` behavior.
- `registerCloseEvent(@Nonnull EventPriority priority, @Nonnull Consumer<WindowCloseEvent> consumer)`
  - Executes `registerCloseEvent` behavior.
- `equals(@Nullable Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
