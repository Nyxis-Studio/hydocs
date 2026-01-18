**Source Hash:** `56269d29363669e7ac02607b74066493fc64d90053c7e5fd8cdac776e16091be`

# WorldNotificationHandler

## Overview

## Constructor Descriptions
- `WorldNotificationHandler(@Nonnull World world)`
  - Creates a `WorldNotificationHandler` instance.

## Method Descriptions
- `updateState(int x, int y, int z, BlockState state, BlockState oldState)`: Add description.
  - Executes `updateState` behavior.
- `updateState(int x, int y, int z, BlockState state, BlockState oldState, @Nullable Predicate<PlayerRef> skip)`: Add description.
  - Executes `updateState` behavior.
- `updateChunk(long indexChunk)`: Add description.
  - Executes `updateChunk` behavior.
- `sendBlockParticle(double x, double y, double z, int id, @Nonnull BlockParticleEvent particleType)`: Add description.
  - Executes `sendBlockParticle` behavior.
- `sendBlockParticle(@Nonnull PlayerRef playerRef, double x, double y, double z, int id, @Nonnull BlockParticleEvent particleType)`: Add description.
  - Executes `sendBlockParticle` behavior.
- `updateBlockDamage(int x, int y, int z, float health, float healthDelta)`: Add description.
  - Executes `updateBlockDamage` behavior.
- `updateBlockDamage(int x, int y, int z, float health, float healthDelta, @Nullable Predicate<PlayerRef> filter)`: Add description.
  - Executes `updateBlockDamage` behavior.
- `sendPacketIfChunkLoaded(@Nonnull Packet packet, int x, int z)`: Add description.
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull Packet packet, long indexChunk)`: Add description.
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull Packet packet, int x, int z, @Nullable Predicate<PlayerRef> filter)`: Add description.
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull Packet packet, long indexChunk, @Nullable Predicate<PlayerRef> filter)`: Add description.
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull PlayerRef player, @Nonnull Packet packet, int x, int z)`: Add description.
  - Executes `sendPacketIfChunkLoaded` behavior.
- `sendPacketIfChunkLoaded(@Nonnull PlayerRef playerRef, @Nonnull Packet packet, long indexChunk)`: Add description.
  - Executes `sendPacketIfChunkLoaded` behavior.
- `getBlockParticlePacket(double x, double y, double z, int id, @Nonnull BlockParticleEvent particleType)`: Add description.
  - Executes `getBlockParticlePacket` behavior.
- `getBlockDamagePacket(int x, int y, int z, float health, float healthDelta)`: Add description.
  - Executes `getBlockDamagePacket` behavior.

## Notes
- No additional notes.
