# TaskRegistry

## Overview
- Documentation for `TaskRegistry`.
- Declared as a class in `com.hypixel.hytale.server.core.task`.

## Constructors
- `TaskRegistry(@Nonnull List<BooleanConsumer> registrations, BooleanSupplier precondition, String preconditionMessage)`
  - Creates a `TaskRegistry` instance.

## Methods
- `registerTask(@Nonnull CompletableFuture<Void> task)`
  - Executes `registerTask` behavior.
- `registerTask(@Nonnull ScheduledFuture<Void> task)`
  - Executes `registerTask` behavior.

## Notes
- No additional notes.
