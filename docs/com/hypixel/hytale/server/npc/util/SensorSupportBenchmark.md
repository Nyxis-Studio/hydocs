# SensorSupportBenchmark

## Overview
- Documentation for `SensorSupportBenchmark`.
- Declared as a class in `com.hypixel.hytale.server.npc.util`.

## Constructors
- None.

## Methods
- `collectPlayerList(long getNanos, double maxPlayerDistanceSorted, double maxPlayerDistance, double maxPlayerDistanceAvoidance, int numPlayers)`
  - Executes `collectPlayerList` behavior.
- `collectEntityList(long getNanos, double maxEntityDistanceSorted, double maxEntityDistance, double maxEntityDistanceAvoidance, int numEntities)`
  - Executes `collectEntityList` behavior.
- `collectLosTest(boolean cacheHit, long time)`
  - Executes `collectLosTest` behavior.
- `collectInverseLosTest(boolean cacheHit)`
  - Executes `collectInverseLosTest` behavior.
- `collectFriendlyBlockingTest(boolean cacheHit)`
  - Executes `collectFriendlyBlockingTest` behavior.
- `tickDone()`
  - Executes `tickDone` behavior.
- `formatHeaderUpdateTimes(@Nonnull Formatter formatter)`
  - Executes `formatHeaderUpdateTimes` behavior.
- `formatValuesUpdateTimePlayer(@Nonnull Formatter formatter)`
  - Executes `formatValuesUpdateTimePlayer` behavior.
- `formatValuesUpdateTimeEntity(@Nonnull Formatter formatter)`
  - Executes `formatValuesUpdateTimeEntity` behavior.
- `formatValuesUpdateTime(@Nonnull Formatter formatter, String kind, @Nonnull TimeRecorder getTime, @Nonnull DiscreteValueRecorder count, @Nonnull DiscreteValueRecorder distanceSorted, @Nonnull DiscreteValueRecorder distance, @Nonnull DiscreteValueRecorder distanceAvoidance)`
  - Executes `formatValuesUpdateTime` behavior.
- `haveUpdateTimes()`
  - Executes `haveUpdateTimes` behavior.
- `formatHeaderLoS(@Nonnull Formatter formatter)`
  - Executes `formatHeaderLoS` behavior.
- `formatValuesLoS(@Nonnull Formatter formatter)`
  - Executes `formatValuesLoS` behavior.

## Notes
- No additional notes.
