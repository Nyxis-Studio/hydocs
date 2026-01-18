**Source Hash:** `a9162add3c6cab43883af10b5f108cb954755c9329388dc211255d7783c14d53`
**Last Updated:** `2026-01-18T17:16:53-03:00`

## Overview
Secondary entry point invoked after the transforming class loader is ready. It parses startup options, initializes logging, and constructs the server with bytecode transformations applied.

## Field Descriptions
- `none`: No fields exposed; static entry point only.

## Constructor Descriptions
- `none()`: Static entry point only.

## Method Descriptions
- `lateMain(String[] args)`: Parses CLI options, initializes the logger and file handler, configures log-level lookups from options or server config, optionally reloads log levels when validating, then instantiates `HytaleServer`. Captures unexpected failures in Sentry and rethrows as a runtime exception.

## Usage Notes
- This entry point is invoked from `Main` when class loader setup is complete.
- Do not call this directly in normal launches; use `Main.main` to ensure early plugins and transformers are loaded.
- When `Options.SHUTDOWN_AFTER_VALIDATE` is set, log levels default to warnings until validation completes.

## Examples
```java
// Standard JVM entry uses Main; LateMain is invoked internally.
public static void main(String[] args) {
    Main.main(args);
}
```
