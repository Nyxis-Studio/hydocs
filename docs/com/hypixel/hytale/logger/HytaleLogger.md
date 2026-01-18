# HytaleLogger

## Overview
- Documentation for `HytaleLogger`.
- Declared as a class in `com.hypixel.hytale.logger`.

## Constructors
- `HytaleLogger(HytaleLoggerBackend.getLogger(key)`
  - Creates a `HytaleLogger` instance.
- `HytaleLogger(@Nonnull HytaleLoggerBackend backend)`
  - Creates a `HytaleLogger` instance.
- `HytaleLogger(this.backend.getSubLogger(name)`
  - Creates a `HytaleLogger` instance.
- `HytaleLogger(HytaleLoggerBackend.getLogger()`
  - Creates a `HytaleLogger` instance.

## Methods
- `init()`
  - Executes `init` behavior.
- `replaceStd()`
  - Executes `replaceStd` behavior.
- `getLogger()`
  - Executes `getLogger` behavior.
- `forEnclosingClass()`
  - Executes `forEnclosingClass` behavior.
- `forEnclosingClassFull()`
  - Executes `forEnclosingClassFull` behavior.
- `get(String loggerName)`
  - Executes `get` behavior.
- `at(@Nonnull Level level)`
  - Executes `at` behavior.
- `getName()`
  - Executes `getName` behavior.
- `getLevel()`
  - Executes `getLevel` behavior.
- `setLevel(@Nonnull Level level)`
  - Executes `setLevel` behavior.
- `getSubLogger(String name)`
  - Executes `getSubLogger` behavior.
- `setSentryClient(@Nonnull IScopes scope)`
  - Executes `setSentryClient` behavior.
- `setPropagatesSentryToParent(boolean propagate)`
  - Executes `setPropagatesSentryToParent` behavior.
- `classToLoggerName(@Nonnull String className)`
  - Executes `classToLoggerName` behavior.
- `api()`
  - Executes `api` behavior.
- `noOp()`
  - Executes `noOp` behavior.
- `getMessageParser()`
  - Executes `getMessageParser` behavior.

## Notes
- No additional notes.
