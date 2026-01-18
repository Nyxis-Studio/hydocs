**Source Hash:** `3bf87abfd876785ff2e1589e8f64f3fb3625633b89eadf824e46082917137635`
**Last Updated:** `2026-01-18T17:16:53-03:00`

## Overview
Entry point class for the Hytale server JVM. It sets locale/system properties, loads early plugins, and decides whether to bootstrap via a transforming class loader or run `LateMain` directly.

## Field Descriptions
- `none`: No fields exposed; static entry point only.

## Constructor Descriptions
- `none()`: Static entry point only.

## Method Descriptions
- `main(String[] args)`: Sets JVM defaults (locale, headless mode, UTF-8 encoding), loads early plugins, and chooses the launch path based on whether transformers are present.
- `launchWithTransformingClassLoader(String[] args)`: Builds a transforming class loader, switches the thread context loader, reflectively invokes `LateMain.lateMain`, and normalizes thrown exceptions.
- `getClasspathUrls()`: Derives classpath URLs from the current class loader or `java.class.path`, skipping missing entries and logging parse errors to stderr.

## Usage Notes
- Always launch through this entry point to ensure early plugins and transformers are discovered.
- `launchWithTransformingClassLoader` is only used when early plugins register transformers.

## Examples
```java
public static void main(String[] args) {
    Main.main(args);
}
```
