# IEventBus

## Overview
- Documentation for `IEventBus`.
- Declared as a interface in `com.hypixel.hytale.event`.

## Constructors
- None.

## Methods
- `dispatch(@Nonnull Class<EventType> eventClass)`
  - Executes `dispatch` behavior.
- `dispatchAsync(@Nonnull Class<EventType> eventClass)`
  - Executes `dispatchAsync` behavior.
- `dispatchFor(@Nonnull Class<? super EventType> eventClass)`
  - Executes `dispatchFor` behavior.
- `dispatchFor(@Nonnull Class<? super EventType> var1, @Nullable KeyType var2)`
  - Executes `dispatchFor` behavior.
- `dispatchForAsync(@Nonnull Class<? super EventType> eventClass)`
  - Executes `dispatchForAsync` behavior.
- `dispatchForAsync(@Nonnull Class<? super EventType> var1, @Nullable KeyType var2)`
  - Executes `dispatchForAsync` behavior.

## Notes
- No additional notes.
