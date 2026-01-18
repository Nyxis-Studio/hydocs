# WorldNotificationHandler

## Overview
- Documentation for `WorldNotificationHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world`.

## Constructors
- `WorldNotificationHandler(@Nonnull World world)`
  - Creates a `WorldNotificationHandler` instance.

## Methods
- `updateState(int x, int y, int z, BlockState state, BlockState oldState)`
  - Executes `updateState` behavior.
- `updateState(int x, int y, int z, BlockState state, BlockState oldState, @Nullable Predicate<PlayerRef> skip)`
  - Executes `updateState` behavior.
- `updateChunk(long indexChunk)`
  - Executes `updateChunk` behavior.
- `sendBlockParticle(double x, double y, double z, int id, @Nonnull BlockParticleEvent particleType)`
  - Executes `sendBlockParticle` behavior.
- `sendBlockParticle(@Nonnull PlayerRef playerRef, double x, double y, double z, int id, @Nonnull BlockParticleEvent particleType)`
  - Executes `sendBlockParticle` behavior.
- `updateBlockDamage(int x, int y, int z, float health, float healthDelta)`
  - Executes `updateBlockDamage` behavior.
- `updateBlockDamage(int x, int y, int z, float health, float healthDelta, @Nullable Predicate<PlayerRef> filter)`
  - Executes `updateBlockDamage` behavior.
- `sendPacketIfChunkLoaded(@Nonnull Packet packet, int x, int z)`
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull Packet packet, long indexChunk)`
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull Packet packet, int x, int z, @Nullable Predicate<PlayerRef> filter)`
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull Packet packet, long indexChunk, @Nullable Predicate<PlayerRef> filter)`
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull PlayerRef player, @Nonnull Packet packet, int x, int z)`
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull PlayerRef playerRef, @Nonnull Packet packet, long indexChunk)`
  - Executes `sendPacketIfChunkLoaded` behavior.
- `getBlockParticlePacket(double x, double y, double z, int id, @Nonnull BlockParticleEvent particleType)`
  - Executes `getBlockParticlePacket` behavior.
- `getBlockDamagePacket(int x, int y, int z, float health, float healthDelta)`
  - Executes `getBlockDamagePacket` behavior.

## Notes
- No additional notes.
