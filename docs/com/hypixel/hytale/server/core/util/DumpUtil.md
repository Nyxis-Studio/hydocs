# DumpUtil

## Overview
- Documentation for `DumpUtil`.
- Declared as a class in `com.hypixel.hytale.server.core.util`.

## Constructors
- None.

## Methods
- `dumpToJson()`
  - Executes `dumpToJson` behavior.
- `collectPlayerComponentMetrics()`
  - Executes `collectPlayerComponentMetrics` behavior.
- `collectPlayerTextData()`
  - Executes `collectPlayerTextData` behavior.
- `hexDump(@Nonnull ByteBuf buf)`
  - Executes `hexDump` behavior.
- `hexDump(@Nonnull byte[] data)`
  - Executes `hexDump` behavior.
- `dump(boolean crash, boolean printToConsole)`
  - Executes `dump` behavior.
- `createDumpPath(boolean crash, String ext)`
  - Executes `createDumpPath` behavior.
- `write(@Nonnull PrintWriter writer)`
  - Executes `write` behavior.
- `printPacketStats(@Nonnull PrintWriter writer, @Nonnull String indent, @Nonnull String label, int count, long uncompressedTotal, long compressedTotal, long uncompressedMin, long uncompressedMax, long compressedMin, long compressedMax, double uncompressedAvg, double compressedAvg, int recentSeconds)`
  - Executes `printPacketStats` behavior.
- `printComponentStore(@Nonnull PrintWriter writer, int width, int height, String name, long startNanos, @Nonnull Store<?> componentStore)`
  - Executes `printComponentStore` behavior.
- `section(String name, @Nonnull Runnable runnable, @Nonnull PrintWriter writer)`
  - Executes `section` behavior.
- `printIndented(@Nonnull PrintWriter writer, @Nonnull String text, @Nonnull String indent)`
  - Executes `printIndented` behavior.
- `writeMemoryUsage(@Nonnull PrintWriter writer, String title, @Nonnull MemoryUsage memoryUsage)`
  - Executes `writeMemoryUsage` behavior.
- `writeClassLoader(@Nonnull PrintWriter writer, @Nullable ClassLoader systemClassLoader)`
  - Executes `writeClassLoader` behavior.
- `PlayerTextData(@Nonnull UUID uuid, @Nullable String movementStates, @Nullable String movementManager, @Nullable String cameraManager)`
  - Executes `PlayerTextData` behavior.

## Notes
- No additional notes.
