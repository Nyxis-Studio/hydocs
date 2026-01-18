# MaskShader

## Overview
- Documentation for `MaskShader`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.framework.shaders`.

## Constructors
- `MaskShader(Predicate<T> mask, Shader<T> childShader, long seed)`
  - Creates a `MaskShader` instance.

## Methods
- `builder(@Nonnull Class<T> dataType)`
  - Executes `builder` behavior.
- `shade(T current, long seed)`
  - Executes `shade` behavior.
- `shade(T current, long seedA, long seedB)`
  - Executes `shade` behavior.
- `shade(T current, long seedA, long seedB, long seedC)`
  - Executes `shade` behavior.
- `toString()`
  - Executes `toString` behavior.
- `build()`
  - Executes `build` behavior.
- `withSeed(long seed)`
  - Executes `withSeed` behavior.
- `withMask(@Nonnull Predicate<T> mask)`
  - Executes `withMask` behavior.
- `withChildShader(@Nonnull Shader<T> shader)`
  - Executes `withChildShader` behavior.

## Notes
- No additional notes.
