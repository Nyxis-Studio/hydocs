# FormattedMessage

## Overview
- Documentation for `FormattedMessage`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `FormattedMessage()`
  - Creates a `FormattedMessage` instance.
- `FormattedMessage(@Nullable String rawText, @Nullable String messageId, @Nullable FormattedMessage[] children, @Nullable Map<String, ParamValue> params, @Nullable Map<String, FormattedMessage> messageParams, @Nullable String color, @Nonnull MaybeBool bold, @Nonnull MaybeBool italic, @Nonnull MaybeBool monospace, @Nonnull MaybeBool underlined, @Nullable String link, boolean markupEnabled)`
  - Creates a `FormattedMessage` instance.
- `FormattedMessage(@Nonnull FormattedMessage other)`
  - Creates a `FormattedMessage` instance.

## Methods
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
