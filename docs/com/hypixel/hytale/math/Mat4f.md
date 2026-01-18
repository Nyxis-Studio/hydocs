# Mat4f

## Overview
- Documentation for `Mat4f`.
- Declared as a class in `com.hypixel.hytale.math`.

## Constructors
- `Mat4f(float m11, float m12, float m13, float m14, float m21, float m22, float m23, float m24, float m31, float m32, float m33, float m34, float m41, float m42, float m43, float m44)`
  - Creates a `Mat4f` instance.
- `Mat4f(1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f)`
  - Creates a `Mat4f` instance.
- `Mat4f(Float.intBitsToFloat(buf.getIntLE(offset)`
  - Creates a `Mat4f` instance.

## Methods
- `identity()`
  - Executes `identity` behavior.
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.

## Notes
- No additional notes.
