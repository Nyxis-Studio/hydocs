# EventBus

## Overview
- Documentation for `EventBus`.
- Declared as a class in `com.hypixel.hytale.event`.

## Constructors
- `EventBus(boolean timeEvents)`
  - Creates a `EventBus` instance.

## Methods
- `shutdown()`
  - Executes `shutdown` behavior.
- `getRegisteredEventClassNames()`
  - Executes `getRegisteredEventClassNames` behavior.
- `getAsyncRegistry(@Nonnull Class<? super EventType> eventClass)`
  - Executes `getAsyncRegistry` behavior.
- `register(@Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `register` behavior.
- `register(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `register` behavior.
- `register(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `register` behavior.
- `register(@Nonnull Class<? super EventType> eventClass, @Nonnull KeyType key, @Nonnull Consumer<EventType> consumer)`
  - Executes `register` behavior.
- `register(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull KeyType key, @Nonnull Consumer<EventType> consumer)`
  - Executes `register` behavior.
- `register(short priority, @Nonnull Class<? super EventType> eventClass, @Nullable KeyType key, @Nonnull Consumer<EventType> consumer)`
  - Executes `register` behavior.
- `registerAsync(@Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsync` behavior.
- `registerAsync(short priority, Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull Class<? super EventType> eventClass, @Nonnull KeyType key, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull EventPriority priority, Class<? super EventType> eventClass, @Nonnull KeyType key, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsync` behavior.
- `registerAsync(short priority, @Nonnull Class<? super EventType> eventClass, @Nullable KeyType key, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsync` behavior.
- `registerGlobal(@Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `registerGlobal` behavior.
- `registerGlobal(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `registerGlobal` behavior.
- `registerGlobal(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `registerGlobal` behavior.
- `registerAsyncGlobal(@Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsyncGlobal` behavior.
- `registerAsyncGlobal(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsyncGlobal` behavior.
- `registerAsyncGlobal(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsyncGlobal` behavior.
- `registerUnhandled(@Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `registerUnhandled` behavior.
- `registerUnhandled(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `registerUnhandled` behavior.
- `registerUnhandled(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`
  - Executes `registerUnhandled` behavior.
- `registerAsyncUnhandled(@Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsyncUnhandled` behavior.
- `registerAsyncUnhandled(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsyncUnhandled` behavior.
- `registerAsyncUnhandled(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`
  - Executes `registerAsyncUnhandled` behavior.
- `dispatchFor(@Nonnull Class<? super EventType> eventClass, KeyType key)`
  - Executes `dispatchFor` behavior.
- `dispatchForAsync(@Nonnull Class<? super EventType> eventClass, KeyType key)`
  - Executes `dispatchForAsync` behavior.

## Notes
- No additional notes.
