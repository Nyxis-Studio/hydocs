# IEventRegistry

## Overview
- Documentation for `IEventRegistry`.
- Declared as a interface in `com.hypixel.hytale.event`.

## Constructors
- None.

## Methods
- `register(@Nonnull Class<? super EventType> var1, @Nonnull Consumer<EventType> var2)`
  - Executes `register` behavior.
- `register(@Nonnull EventPriority var1, @Nonnull Class<? super EventType> var2, @Nonnull Consumer<EventType> var3)`
  - Executes `register` behavior.
- `register(short var1, @Nonnull Class<? super EventType> var2, @Nonnull Consumer<EventType> var3)`
  - Executes `register` behavior.
- `register(@Nonnull Class<? super EventType> var1, @Nonnull KeyType var2, @Nonnull Consumer<EventType> var3)`
  - Executes `register` behavior.
- `register(@Nonnull EventPriority var1, @Nonnull Class<? super EventType> var2, @Nonnull KeyType var3, @Nonnull Consumer<EventType> var4)`
  - Executes `register` behavior.
- `register(short var1, @Nonnull Class<? super EventType> var2, @Nonnull KeyType var3, @Nonnull Consumer<EventType> var4)`
  - Executes `register` behavior.
- `registerAsync(@Nonnull Class<? super EventType> var1, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var2)`
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull EventPriority var1, @Nonnull Class<? super EventType> var2, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var3)`
  - Executes `registerAsync` behavior.
- `registerAsync(short var1, Class<? super EventType> var2, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var3)`
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull Class<? super EventType> var1, @Nonnull KeyType var2, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var3)`
  - Executes `registerAsync` behavior.
- `registerAsync(@Nonnull EventPriority var1, Class<? super EventType> var2, @Nonnull KeyType var3, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var4)`
  - Executes `registerAsync` behavior.
- `registerAsync(short var1, @Nonnull Class<? super EventType> var2, @Nonnull KeyType var3, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var4)`
  - Executes `registerAsync` behavior.
- `registerGlobal(@Nonnull Class<? super EventType> var1, @Nonnull Consumer<EventType> var2)`
  - Executes `registerGlobal` behavior.
- `registerGlobal(@Nonnull EventPriority var1, @Nonnull Class<? super EventType> var2, @Nonnull Consumer<EventType> var3)`
  - Executes `registerGlobal` behavior.
- `registerGlobal(short var1, @Nonnull Class<? super EventType> var2, @Nonnull Consumer<EventType> var3)`
  - Executes `registerGlobal` behavior.
- `registerAsyncGlobal(@Nonnull Class<? super EventType> var1, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var2)`
  - Executes `registerAsyncGlobal` behavior.
- `registerAsyncGlobal(@Nonnull EventPriority var1, @Nonnull Class<? super EventType> var2, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var3)`
  - Executes `registerAsyncGlobal` behavior.
- `registerAsyncGlobal(short var1, @Nonnull Class<? super EventType> var2, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var3)`
  - Executes `registerAsyncGlobal` behavior.
- `registerUnhandled(@Nonnull Class<? super EventType> var1, @Nonnull Consumer<EventType> var2)`
  - Executes `registerUnhandled` behavior.
- `registerUnhandled(@Nonnull EventPriority var1, @Nonnull Class<? super EventType> var2, @Nonnull Consumer<EventType> var3)`
  - Executes `registerUnhandled` behavior.
- `registerUnhandled(short var1, @Nonnull Class<? super EventType> var2, @Nonnull Consumer<EventType> var3)`
  - Executes `registerUnhandled` behavior.
- `registerAsyncUnhandled(@Nonnull Class<? super EventType> var1, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var2)`
  - Executes `registerAsyncUnhandled` behavior.
- `registerAsyncUnhandled(@Nonnull EventPriority var1, @Nonnull Class<? super EventType> var2, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var3)`
  - Executes `registerAsyncUnhandled` behavior.
- `registerAsyncUnhandled(short var1, @Nonnull Class<? super EventType> var2, @Nonnull Function<CompletableFuture<EventType>, CompletableFuture<EventType>> var3)`
  - Executes `registerAsyncUnhandled` behavior.

## Notes
- No additional notes.
