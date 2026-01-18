**Source Hash:** `bf159744f573590575bcc2af39b06787fd59a6cb113143283ab321c93d83866c`

# HytaleLoggerBackend

## Overview

## Constructor Descriptions
- `HytaleLoggerBackend(String name)`
  - Creates a `HytaleLoggerBackend` instance.
- `HytaleLoggerBackend(String name, HytaleLoggerBackend parent)`
  - Creates a `HytaleLoggerBackend` instance.
- `HytaleLoggerBackend(this.name + "][" + name, this)`
  - Creates a `HytaleLoggerBackend` instance.
- `HytaleLoggerBackend("Hytale", null)`
  - Creates a `HytaleLoggerBackend` instance.

## Method Descriptions
- `getLoggerName()`: Add description.
  - Executes `getLoggerName` behavior.
- `getLevel()`: Add description.
  - Executes `getLevel` behavior.
- `isLoggable(@Nonnull Level lvl)`: Add description.
  - Executes `isLoggable` behavior.
- `log(@Nonnull LogData data)`: Add description.
  - Executes `log` behavior.
- `handleError(@Nonnull RuntimeException error, @Nonnull LogData badData)`: Add description.
  - Executes `handleError` behavior.
- `log(@Nonnull LogRecord logRecord)`: Add description.
  - Executes `log` behavior.
- `log(@Nonnull LogRecord logRecord, boolean sentryHandled)`: Add description.
  - Executes `log` behavior.
- `subscribe(CopyOnWriteArrayList<LogRecord> subscriber)`: Add description.
  - Executes `subscribe` behavior.
- `unsubscribe(CopyOnWriteArrayList<LogRecord> subscriber)`: Add description.
  - Executes `unsubscribe` behavior.
- `getSubLogger(String name)`: Add description.
  - Executes `getSubLogger` behavior.
- `setSentryClient(@Nullable IScopes scope)`: Add description.
  - Executes `setSentryClient` behavior.
- `setPropagatesSentryToParent(boolean propagate)`: Add description.
  - Executes `setPropagatesSentryToParent` behavior.
- `setOnLevelChange(BiConsumer<Level, Level> onLevelChange)`: Add description.
  - Executes `setOnLevelChange` behavior.
- `setLevel(@Nonnull Level newLevel)`: Add description.
  - Executes `setLevel` behavior.
- `loadLogLevel()`: Add description.
  - Executes `loadLogLevel` behavior.
- `loadLevels(@Nonnull List<Map.Entry<String, Level>> list)`: Add description.
  - Executes `loadLevels` behavior.
- `reloadLogLevels()`: Add description.
  - Executes `reloadLogLevels` behavior.
- `getLogger()`: Add description.
  - Executes `getLogger` behavior.
- `getLogger(@Nonnull String name)`: Add description.
  - Executes `getLogger` behavior.
- `getLogger(String name, BiConsumer<Level, Level> onLevelChange)`: Add description.
  - Executes `getLogger` behavior.
- `setIndent(int indent)`: Add description.
  - Executes `setIndent` behavior.
- `isJunitTest()`: Add description.
  - Executes `isJunitTest` behavior.
- `rawLog(String message)`: Add description.
  - Executes `rawLog` behavior.

## Notes
- No additional notes.
