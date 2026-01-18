# Notification

## Overview
- Documentation for `Notification`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.interface_`.

## Constructors
- `Notification()`
  - Creates a `Notification` instance.
- `Notification(@Nullable FormattedMessage message, @Nullable FormattedMessage secondaryMessage, @Nullable String icon, @Nullable ItemWithAllMetadata item, @Nonnull NotificationStyle style)`
  - Creates a `Notification` instance.
- `Notification(@Nonnull Notification other)`
  - Creates a `Notification` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
