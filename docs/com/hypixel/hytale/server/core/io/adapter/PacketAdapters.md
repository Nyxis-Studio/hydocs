# PacketAdapters

## Overview
- Documentation for `PacketAdapters`.
- Declared as a class in `com.hypixel.hytale.server.core.io.adapter`.

## Constructors
- None.

## Methods
- `registerInbound(@Nonnull PacketWatcher watcher)`
  - Executes `registerInbound` behavior.
- `registerInbound(PacketFilter predicate)`
  - Executes `registerInbound` behavior.
- `registerOutbound(@Nonnull PacketWatcher watcher)`
  - Executes `registerOutbound` behavior.
- `registerOutbound(PacketFilter predicate)`
  - Executes `registerOutbound` behavior.
- `registerInbound(@Nonnull PlayerPacketFilter filter)`
  - Executes `registerInbound` behavior.
- `registerOutbound(@Nonnull PlayerPacketFilter filter)`
  - Executes `registerOutbound` behavior.
- `registerInbound(@Nonnull PlayerPacketWatcher watcher)`
  - Executes `registerInbound` behavior.
- `registerOutbound(@Nonnull PlayerPacketWatcher watcher)`
  - Executes `registerOutbound` behavior.
- `deregisterInbound(PacketFilter predicate)`
  - Executes `deregisterInbound` behavior.
- `deregisterOutbound(PacketFilter predicate)`
  - Executes `deregisterOutbound` behavior.
- `__handleInbound(PacketHandler player, Packet packet)`
  - Executes `__handleInbound` behavior.
- `handle(@Nonnull List<PacketFilter> list, PacketHandler player, T packet)`
  - Executes `handle` behavior.
- `__handleOutbound(PacketHandler player, Packet packet)`
  - Executes `__handleOutbound` behavior.

## Notes
- No additional notes.
