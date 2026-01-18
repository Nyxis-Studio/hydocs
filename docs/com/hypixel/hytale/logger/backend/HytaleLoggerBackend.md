# HytaleLoggerBackend

## Overview
- Documentation for `HytaleLoggerBackend`.
- Declared as a class in `com.hypixel.hytale.logger.backend`.

## Constructors
- `HytaleLoggerBackend(String name)`
  - Creates a `HytaleLoggerBackend` instance.
- `HytaleLoggerBackend(String name, HytaleLoggerBackend parent)`
  - Creates a `HytaleLoggerBackend` instance.
- `HytaleLoggerBackend(this.name + "][" + name, this)`
  - Creates a `HytaleLoggerBackend` instance.
- `HytaleLoggerBackend("Hytale", null)`
  - Creates a `HytaleLoggerBackend` instance.

## Methods
- `getLoggerName()`
  - Executes `getLoggerName` behavior.
- `getLevel()`
  - Executes `getLevel` behavior.
- `isLoggable(@Nonnull Level lvl)`
  - Executes `isLoggable` behavior.
- `log(@Nonnull LogData data)`
  - Executes `log` behavior.
- `handleError(@Nonnull RuntimeException error, @Nonnull LogData badData)`
  - Executes `handleError` behavior.
- `log(@Nonnull LogRecord logRecord)`
  - Executes `log` behavior.
- `log(@Nonnull LogRecord logRecord, boolean sentryHandled)`
  - Executes `log` behavior.
- `subscribe(CopyOnWriteArrayList<LogRecord> subscriber)`
  - Executes `subscribe` behavior.
- `unsubscribe(CopyOnWriteArrayList<LogRecord> subscriber)`
  - Executes `unsubscribe` behavior.
- `getSubLogger(String name)`
  - Executes `getSubLogger` behavior.
- `setSentryClient(@Nullable IScopes scope)`
  - Executes `setSentryClient` behavior.
- `setPropagatesSentryToParent(boolean propagate)`
  - Executes `setPropagatesSentryToParent` behavior.
- `setOnLevelChange(BiConsumer<Level, Level> onLevelChange)`
  - Executes `setOnLevelChange` behavior.
- `setLevel(@Nonnull Level newLevel)`
  - Executes `setLevel` behavior.
- `loadLogLevel()`
  - Executes `loadLogLevel` behavior.
- `loadLevels(@Nonnull List<Map.Entry<String, Level>> list)`
  - Executes `loadLevels` behavior.
- `reloadLogLevels()`
  - Executes `reloadLogLevels` behavior.
- `getLogger()`
  - Executes `getLogger` behavior.
- `getLogger(@Nonnull String name)`
  - Executes `getLogger` behavior.
- `getLogger(String name, BiConsumer<Level, Level> onLevelChange)`
  - Executes `getLogger` behavior.
- `setIndent(int indent)`
  - Executes `setIndent` behavior.
- `isJunitTest()`
  - Executes `isJunitTest` behavior.
- `rawLog(String message)`
  - Executes `rawLog` behavior.

## Notes
- No additional notes.
