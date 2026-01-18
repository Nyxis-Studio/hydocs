**Source Hash:** `136861a85f4804927b249abc3220567c52d958d94df9aaac2a66726b66acc678`

# EventBus

## Overview

## Constructor Descriptions
- `EventBus(boolean timeEvents)`
  - Creates a `EventBus` instance.

## Method Descriptions
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.
- `getRegisteredEventClassNames()`: Add description.
  - Executes `getRegisteredEventClassNames` behavior.
- `getAsyncRegistry(@Nonnull Class<? super EventType> eventClass)`: Add description.
  - Executes `getAsyncRegistry` behavior.
- `register(@Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `register` behavior.
- `register(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `register` behavior.
- `register(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `register` behavior.
- `register(@Nonnull Class<? super EventType> eventClass, @Nonnull KeyType key, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `register` behavior.
- `register(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull KeyType key, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `register` behavior.
- `register(short priority, @Nonnull Class<? super EventType> eventClass, @Nullable KeyType key, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `register` behavior.
- `registerAsync(@Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsync` behavior.
- `registerAsync(short priority, Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull Class<? super EventType> eventClass, @Nonnull KeyType key, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull EventPriority priority, Class<? super EventType> eventClass, @Nonnull KeyType key, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsync` behavior.
- `registerAsync(short priority, @Nonnull Class<? super EventType> eventClass, @Nullable KeyType key, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsync` behavior.
- `registerGlobal(@Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `registerGlobal` behavior.
- `registerGlobal(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `registerGlobal` behavior.
- `registerGlobal(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `registerGlobal` behavior.
- `registerAsyncGlobal(@Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsyncGlobal` behavior.
- `registerAsyncGlobal(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsyncGlobal` behavior.
- `registerAsyncGlobal(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsyncGlobal` behavior.
- `registerUnhandled(@Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `registerUnhandled` behavior.
- `registerUnhandled(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `registerUnhandled` behavior.
- `registerUnhandled(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Consumer<EventType> consumer)`: Add description.
  - Executes `registerUnhandled` behavior.
- `registerAsyncUnhandled(@Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsyncUnhandled` behavior.
- `registerAsyncUnhandled(@Nonnull EventPriority priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsyncUnhandled` behavior.
- `registerAsyncUnhandled(short priority, @Nonnull Class<? super EventType> eventClass, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> function)`: Add description.
  - Executes `registerAsyncUnhandled` behavior.
- `dispatchFor(@Nonnull Class<? super EventType> eventClass, KeyType key)`: Add description.
  - Executes `dispatchFor` behavior.
- `dispatchForAsync(@Nonnull Class<? super EventType> eventClass, KeyType key)`: Add description.
  - Executes `dispatchForAsync` behavior.

## Notes
- No additional notes.
