# NPCSensorStatsCommand

## Overview
- Documentation for `NPCSensorStatsCommand`.
- Declared as a class in `com.hypixel.hytale.server.npc.commands`.

## Constructors
- `NPCSensorStatsCommand()`
  - Creates a `NPCSensorStatsCommand` instance.

## Methods
- `execute(@Nonnull CommandContext context, @Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull PlayerRef playerRef, @Nonnull World world)`
  - Executes `execute` behavior.
- `isRangesEmpty(@Nonnull RoleStats roleStats, boolean isPlayer)`
  - Executes `isRangesEmpty` behavior.
- `formatBuckets(@Nonnull StringBuilder builder, @Nonnull RoleStats roleStats, @Nonnull String label, boolean isPlayer, int width)`
  - Executes `formatBuckets` behavior.
- `formatRanges(@Nonnull StringBuilder builder, @Nonnull RoleStats roleStats, @Nonnull String label, boolean isPlayer, @Nonnull RoleStats.RangeType rangeType, int width)`
  - Executes `formatRanges` behavior.

## Notes
- No additional notes.
