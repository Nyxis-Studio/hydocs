# TransformingClassLoader

## Overview
- Documentation for `TransformingClassLoader`.
- Declared as a class in `com.hypixel.hytale.plugin.early`.

## Constructors
- `TransformingClassLoader(@Nonnull URL[] urls, @Nonnull List<ClassTransformer> transformers, ClassLoader parent, ClassLoader appClassLoader)`
  - Creates a `TransformingClassLoader` instance.

## Methods
- `getCodeSourceUrl(URL resource, String internalName)`
  - Executes `getCodeSourceUrl` behavior.
- `isPreloadedClass(@Nonnull String name)`
  - Executes `isPreloadedClass` behavior.
- `isSecureClass(@Nonnull String name)`
  - Executes `isSecureClass` behavior.

## Notes
- No additional notes.
