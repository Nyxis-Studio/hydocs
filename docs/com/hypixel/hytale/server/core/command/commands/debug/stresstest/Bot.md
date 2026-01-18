# Bot

## Overview
- Documentation for `Bot`.
- Declared as a class in `com.hypixel.hytale.server.core.command.commands.debug.stresstest`.

## Constructors
- `Bot(String name, @Nonnull BotConfig config, int tickStepNanos)`
  - Creates a `Bot` instance.

## Methods
- `initChannel(@Nonnull SocketChannel channel)`
  - Executes `initChannel` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `tick(float dt)`
  - Executes `tick` behavior.
- `channelActive(@Nonnull ChannelHandlerContext ctx)`
  - Executes `channelActive` behavior.
- `channelInactive(ChannelHandlerContext ctx)`
  - Executes `channelInactive` behavior.
- `exceptionCaught(@Nonnull ChannelHandlerContext ctx, @Nonnull Throwable cause)`
  - Executes `exceptionCaught` behavior.
- `channelRead0(@Nonnull ChannelHandlerContext ctx, @Nonnull Packet packet)`
  - Executes `channelRead0` behavior.
- `updateModelTransform(@Nonnull ModelTransform modelTransform)`
  - Executes `updateModelTransform` behavior.
- `updateRotation(@Nonnull Direction lookOrientation)`
  - Executes `updateRotation` behavior.
- `createMovementPacket()`
  - Executes `createMovementPacket` behavior.
- `toString()`
  - Executes `toString` behavior.
- `findEntityUpdate(@Nonnull EntityUpdates bulkList, int id)`
  - Executes `findEntityUpdate` behavior.

## Notes
- No additional notes.
