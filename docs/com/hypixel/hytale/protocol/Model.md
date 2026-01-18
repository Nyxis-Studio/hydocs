# Model

## Overview
- Documentation for `Model`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Model()`
  - Creates a `Model` instance.
- `Model(@Nullable String assetId, @Nullable String path, @Nullable String texture, @Nullable String gradientSet, @Nullable String gradientId, @Nullable CameraSettings camera, float scale, float eyeHeight, float crouchOffset, @Nullable Map<String, AnimationSet> animationSets, @Nullable ModelAttachment[] attachments, @Nullable Hitbox hitbox, @Nullable ModelParticle[] particles, @Nullable ModelTrail[] trails, @Nullable ColorLight light, @Nullable Map<String, DetailBox[]> detailBoxes, @Nonnull Phobia phobia, @Nullable Model phobiaModel)`
  - Creates a `Model` instance.
- `Model(@Nonnull Model other)`
  - Creates a `Model` instance.

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
