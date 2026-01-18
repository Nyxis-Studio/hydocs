# ClipboardBoundsSnapshot

## Overview
- Documentation for `ClipboardBoundsSnapshot`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.snapshot`.

## Constructors
- `ClipboardBoundsSnapshot(Vector3i.ZERO, Vector3i.ZERO)`
  - Creates a `ClipboardBoundsSnapshot` instance.
- `ClipboardBoundsSnapshot(@Nonnull BlockSelection selection)`
  - Creates a `ClipboardBoundsSnapshot` instance.
- `ClipboardBoundsSnapshot(Vector3i min, Vector3i max)`
  - Creates a `ClipboardBoundsSnapshot` instance.
- `ClipboardBoundsSnapshot(state.getSelection()`
  - Creates a `ClipboardBoundsSnapshot` instance.

## Methods
- `getMin()`
  - Executes `getMin` behavior.
- `getMax()`
  - Executes `getMax` behavior.
- `restoreClipboard(Ref<EntityStore> ref, Player player, World world, @Nonnull BuilderToolsPlugin.BuilderState state, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `restoreClipboard` behavior.

## Notes
- No additional notes.
