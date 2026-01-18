# LatencySimulationHandler

## Overview
- Documentation for `LatencySimulationHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.io.netty`.

## Constructors
- `LatencySimulationHandler(long delay, @Nonnull TimeUnit unit)`
  - Creates a `LatencySimulationHandler` instance.
- `LatencySimulationHandler(delay, unit)`
  - Creates a `LatencySimulationHandler` instance.

## Methods
- `read(ChannelHandlerContext ctx)`
  - Executes `read` behavior.
- `write(ChannelHandlerContext ctx, Object msg, ChannelPromise promise)`
  - Executes `write` behavior.
- `flush(ChannelHandlerContext ctx)`
  - Executes `flush` behavior.
- `handlerRemoved(ChannelHandlerContext ctx)`
  - Executes `handlerRemoved` behavior.
- `close(ChannelHandlerContext ctx, ChannelPromise promise)`
  - Executes `close` behavior.
- `setLatency(@Nonnull Channel channel, long delay, @Nonnull TimeUnit unit)`
  - Executes `setLatency` behavior.
- `run()`
  - Executes `run` behavior.
- `getDelay(@Nonnull TimeUnit unit)`
  - Executes `getDelay` behavior.
- `compareTo(@Nonnull Delayed o)`
  - Executes `compareTo` behavior.

## Notes
- No additional notes.
