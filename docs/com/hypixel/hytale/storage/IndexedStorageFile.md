**Source Hash:** `bb5ff74b7821a8bfaf8aecbaf9c30888b4e281a4fcdc0b72ffe5b83b04ebcc8b`

# IndexedStorageFile

## Overview

## Constructor Descriptions
- `IndexedStorageFile(path, FileChannel.open(path, options, attrs)`
  - Creates a `IndexedStorageFile` instance.
- `IndexedStorageFile(path, FileChannel.open(path, newOptions, attrs)`
  - Creates a `IndexedStorageFile` instance.
- `IndexedStorageFile(@Nonnull Path path, @Nonnull FileChannel fileChannel)`
  - Creates a `IndexedStorageFile` instance.

## Method Descriptions
- `getTempBuffer(int length)`: Add description.
  - Executes `getTempBuffer` behavior.
- `allocateDirect(int length)`: Add description.
  - Executes `allocateDirect` behavior.
- `open(@Nonnull Path path, OpenOption ... options)`: Add description.
  - Executes `open` behavior.
- `open(@Nonnull Path path, @Nonnull Set<? extends OpenOption> options, FileAttribute<?> ... attrs)`: Add description.
  - Executes `open` behavior.
- `open(@Nonnull Path path, int blobCount, int segmentSize, OpenOption ... options)`: Add description.
  - Executes `open` behavior.
- `open(@Nonnull Path path, int blobCount, int segmentSize, @Nonnull Set<? extends OpenOption> options, FileAttribute<?> ... attrs)`: Add description.
  - Executes `open` behavior.
- `migrateV0(Path path, int blobCount, int segmentSize, Set<? extends OpenOption> options, FileAttribute<?>[] attrs, IndexedStorageFile storageFile)`: Add description.
  - Executes `migrateV0` behavior.
- `getPath()`: Add description.
  - Executes `getPath` behavior.
- `getBlobCount()`: Add description.
  - Executes `getBlobCount` behavior.
- `getSegmentSize()`: Add description.
  - Executes `getSegmentSize` behavior.
- `getCompressionLevel()`: Add description.
  - Executes `getCompressionLevel` behavior.
- `setFlushOnWrite(boolean flushOnWrite)`: Add description.
  - Executes `setFlushOnWrite` behavior.
- `setCompressionLevel(int compressionLevel)`: Add description.
  - Executes `setCompressionLevel` behavior.
- `create(int blobCount, int segmentSize)`: Add description.
  - Executes `create` behavior.
- `writeHeader(int blobCount, int segmentSize)`: Add description.
  - Executes `writeHeader` behavior.
- `readHeader()`: Add description.
  - Executes `readHeader` behavior.
- `memoryMapBlobIndexes()`: Add description.
  - Executes `memoryMapBlobIndexes` behavior.
- `readUsedSegments()`: Add description.
  - Executes `readUsedSegments` behavior.
- `size()`: Add description.
  - Executes `size` behavior.
- `segmentSize()`: Add description.
  - Executes `segmentSize` behavior.
- `segmentCount()`: Add description.
  - Executes `segmentCount` behavior.
- `keys()`: Add description.
  - Executes `keys` behavior.
- `readBlobLength(int blobIndex)`: Add description.
  - Executes `readBlobLength` behavior.
- `readBlobCompressedLength(int blobIndex)`: Add description.
  - Executes `readBlobCompressedLength` behavior.
- `readBlob(int blobIndex)`: Add description.
  - Executes `readBlob` behavior.
- `readBlob(int blobIndex, @Nonnull ByteBuffer dest)`: Add description.
  - Executes `readBlob` behavior.
- `readBlobHeader(int firstSegmentIndex)`: Add description.
  - Executes `readBlobHeader` behavior.
- `readSegments(int firstSegmentIndex, int compressedLength)`: Add description.
  - Executes `readSegments` behavior.
- `writeBlob(int blobIndex, @Nonnull ByteBuffer src)`: Add description.
  - Executes `writeBlob` behavior.
- `removeBlob(int blobIndex)`: Add description.
  - Executes `removeBlob` behavior.
- `writeSegments(@Nonnull ByteBuffer data)`: Add description.
  - Executes `writeSegments` behavior.
- `findFreeSegment(int count)`: Add description.
  - Executes `findFreeSegment` behavior.
- `getSegmentLock(int segmentIndex)`: Add description.
  - Executes `getSegmentLock` behavior.
- `segmentsBase()`: Add description.
  - Executes `segmentsBase` behavior.
- `segmentOffset(int segmentIndex)`: Add description.
  - Executes `segmentOffset` behavior.
- `segmentPosition(int segmentIndex)`: Add description.
  - Executes `segmentPosition` behavior.
- `positionToSegment(long position)`: Add description.
  - Executes `positionToSegment` behavior.
- `requiredSegments(long dataLength)`: Add description.
  - Executes `requiredSegments` behavior.
- `lock()`: Add description.
  - Executes `lock` behavior.
- `force(boolean metaData)`: Add description.
  - Executes `force` behavior.
- `close()`: Add description.
  - Executes `close` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `unlock()`: Add description.
  - Executes `unlock` behavior.
- `next(int len)`: Add description.
  - Executes `next` behavior.
- `length()`: Add description.
  - Executes `length` behavior.

## Notes
- No additional notes.
