# ServerManager

## Overview
- Documentation for `ServerManager`.
- Declared as a class in `com.hypixel.hytale.server.core.io`.

## Constructors
- `ServerManager(@Nonnull JavaPluginInit init)`
  - Creates a `ServerManager` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `init()`
  - Executes `init` behavior.
- `setup()`
  - Executes `setup` behavior.
- `start()`
  - Executes `start` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `unbindAllListeners()`
  - Executes `unbindAllListeners` behavior.
- `getListeners()`
  - Executes `getListeners` behavior.
- `bind(@Nonnull InetSocketAddress address)`
  - Executes `bind` behavior.
- `unbind(@Nonnull Channel channel)`
  - Executes `unbind` behavior.
- `getLocalOrPublicAddress()`
  - Executes `getLocalOrPublicAddress` behavior.
- `getNonLoopbackAddress()`
  - Executes `getNonLoopbackAddress` behavior.
- `getPublicAddress()`
  - Executes `getPublicAddress` behavior.
- `waitForBindComplete()`
  - Executes `waitForBindComplete` behavior.
- `registerSubPacketHandlers(@Nonnull Function<IPacketHandler, SubPacketHandler> supplier)`
  - Executes `registerSubPacketHandlers` behavior.
- `populateSubPacketHandlers(@Nonnull GamePacketHandler packetHandler)`
  - Executes `populateSubPacketHandlers` behavior.
- `bind0(@Nonnull InetSocketAddress address)`
  - Executes `bind0` behavior.
- `unbind0(@Nonnull Channel channel)`
  - Executes `unbind0` behavior.

## Notes
- No additional notes.
