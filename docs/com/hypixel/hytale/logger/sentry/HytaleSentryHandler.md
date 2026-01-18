# HytaleSentryHandler

## Overview
- Documentation for `HytaleSentryHandler`.
- Declared as a class in `com.hypixel.hytale.logger.sentry`.

## Constructors
- `HytaleSentryHandler(@Nonnull IScopes scope)`
  - Creates a `HytaleSentryHandler` instance.
- `HytaleSentryHandler(@Nonnull IScopes scope, boolean configureFromLogManager)`
  - Creates a `HytaleSentryHandler` instance.

## Methods
- `publish(@Nonnull LogRecord record)`
  - Executes `publish` behavior.
- `captureLog(@Nonnull LogRecord loggingEvent)`
  - Executes `captureLog` behavior.
- `maybeFormatted(@Nonnull Object[] arguments, @Nonnull String message)`
  - Executes `maybeFormatted` behavior.
- `retrieveProperties()`
  - Executes `retrieveProperties` behavior.
- `formatLevel(@Nonnull Level level)`
  - Executes `formatLevel` behavior.
- `toSentryLogLevel(@Nonnull Level level)`
  - Executes `toSentryLogLevel` behavior.
- `parseLevelOrDefault(@Nonnull String levelName)`
  - Executes `parseLevelOrDefault` behavior.
- `createBreadcrumb(@Nonnull LogRecord record)`
  - Executes `createBreadcrumb` behavior.
- `toParams(@Nullable Object[] arguments)`
  - Executes `toParams` behavior.
- `formatMessage(@Nonnull String message, @Nullable Object[] parameters)`
  - Executes `formatMessage` behavior.
- `flush()`
  - Executes `flush` behavior.
- `close()`
  - Executes `close` behavior.
- `setPrintfStyle(boolean printfStyle)`
  - Executes `setPrintfStyle` behavior.
- `setMinimumBreadcrumbLevel(@Nullable Level minimumBreadcrumbLevel)`
  - Executes `setMinimumBreadcrumbLevel` behavior.
- `getMinimumBreadcrumbLevel()`
  - Executes `getMinimumBreadcrumbLevel` behavior.
- `setMinimumEventLevel(@Nullable Level minimumEventLevel)`
  - Executes `setMinimumEventLevel` behavior.
- `getMinimumEventLevel()`
  - Executes `getMinimumEventLevel` behavior.
- `setMinimumLevel(@Nullable Level minimumLevel)`
  - Executes `setMinimumLevel` behavior.
- `getMinimumLevel()`
  - Executes `getMinimumLevel` behavior.
- `isPrintfStyle()`
  - Executes `isPrintfStyle` behavior.
- `isLoggable(@Nonnull LogRecord record)`
  - Executes `isLoggable` behavior.

## Notes
- No additional notes.
