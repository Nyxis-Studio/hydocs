# PacketStatsRecorderImpl

## Overview
- Documentation for `PacketStatsRecorderImpl`.
- Declared as a class in `com.hypixel.hytale.server.core.io`.

## Constructors
- `PacketStatsRecorderImpl()`
  - Creates a `PacketStatsRecorderImpl` instance.

## Methods
- `recordSend(int packetId, int uncompressedSize, int compressedSize)`
  - Executes `recordSend` behavior.
- `recordReceive(int packetId, int uncompressedSize, int compressedSize)`
  - Executes `recordReceive` behavior.
- `getEntry(int packetId)`
  - Executes `getEntry` behavior.
- `pruneOld(Queue<SizeRecord> queue, long now)`
  - Executes `pruneOld` behavior.
- `hasData()`
  - Executes `hasData` behavior.
- `getPacketId()`
  - Executes `getPacketId` behavior.
- `getName()`
  - Executes `getName` behavior.
- `getSentCount()`
  - Executes `getSentCount` behavior.
- `getSentUncompressedTotal()`
  - Executes `getSentUncompressedTotal` behavior.
- `getSentCompressedTotal()`
  - Executes `getSentCompressedTotal` behavior.
- `getSentUncompressedMin()`
  - Executes `getSentUncompressedMin` behavior.
- `getSentUncompressedMax()`
  - Executes `getSentUncompressedMax` behavior.
- `getSentCompressedMin()`
  - Executes `getSentCompressedMin` behavior.
- `getSentCompressedMax()`
  - Executes `getSentCompressedMax` behavior.
- `getSentUncompressedAvg()`
  - Executes `getSentUncompressedAvg` behavior.
- `getSentCompressedAvg()`
  - Executes `getSentCompressedAvg` behavior.
- `getReceivedCount()`
  - Executes `getReceivedCount` behavior.
- `getReceivedUncompressedTotal()`
  - Executes `getReceivedUncompressedTotal` behavior.
- `getReceivedCompressedTotal()`
  - Executes `getReceivedCompressedTotal` behavior.
- `getReceivedUncompressedMin()`
  - Executes `getReceivedUncompressedMin` behavior.
- `getReceivedUncompressedMax()`
  - Executes `getReceivedUncompressedMax` behavior.
- `getReceivedCompressedMin()`
  - Executes `getReceivedCompressedMin` behavior.
- `getReceivedCompressedMax()`
  - Executes `getReceivedCompressedMax` behavior.
- `getReceivedUncompressedAvg()`
  - Executes `getReceivedUncompressedAvg` behavior.
- `getReceivedCompressedAvg()`
  - Executes `getReceivedCompressedAvg` behavior.
- `reset()`
  - Executes `reset` behavior.
- `SizeRecord(long nanos, int uncompressedSize, int compressedSize)`
  - Executes `SizeRecord` behavior.

## Notes
- No additional notes.
