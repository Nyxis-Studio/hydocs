# WorldTimeResource

## Overview
- Documentation for `WorldTimeResource`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.time`.

## Constructors
- `WorldTimeResource()`
  - Creates a `WorldTimeResource` instance.

## Methods
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `getSecondsPerTick(World world)`
  - Executes `getSecondsPerTick` behavior.
- `tick(float dt, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `getMoonPhase()`
  - Executes `getMoonPhase` behavior.
- `setMoonPhase(int moonPhase, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setMoonPhase` behavior.
- `updateMoonPhase(@Nonnull World world, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `updateMoonPhase` behavior.
- `isMoonPhaseWithinRange(@Nonnull World world, int minMoonPhase, int maxMoonPhase)`
  - Executes `isMoonPhaseWithinRange` behavior.
- `setGameTime0(@Nonnull Instant gameTime)`
  - Executes `setGameTime0` behavior.
- `updateSunlightFactor(int dayProgress, float halfNight)`
  - Executes `updateSunlightFactor` behavior.
- `updateScaledTime(float dayProgress, float dayDuration, float halfNight)`
  - Executes `updateScaledTime` behavior.
- `getGameTime()`
  - Executes `getGameTime` behavior.
- `getGameDateTime()`
  - Executes `getGameDateTime` behavior.
- `getSunlightFactor()`
  - Executes `getSunlightFactor` behavior.
- `setGameTime(@Nonnull Instant gameTime, @Nonnull World world, @Nonnull Store<EntityStore> store)`
  - Executes `setGameTime` behavior.
- `setDayTime(double dayTime, @Nonnull World world, @Nonnull Store<EntityStore> store)`
  - Executes `setDayTime` behavior.
- `broadcastTimePacket(@Nonnull Store<EntityStore> store)`
  - Executes `broadcastTimePacket` behavior.
- `sendTimePackets(@Nonnull PlayerRef playerRef)`
  - Executes `sendTimePackets` behavior.
- `isDayTimeWithinRange(double minTime, double maxTime)`
  - Executes `isDayTimeWithinRange` behavior.
- `updateTimePacket(@Nonnull UpdateTime currentTimePacket)`
  - Executes `updateTimePacket` behavior.
- `updateTimeSettingsPacket(@Nonnull UpdateTimeSettings settings, @Nonnull World world)`
  - Executes `updateTimeSettingsPacket` behavior.
- `isScaledDayTimeWithinRange(double minTime, double maxTime)`
  - Executes `isScaledDayTimeWithinRange` behavior.
- `isYearWithinRange(double minTime, double maxTime)`
  - Executes `isYearWithinRange` behavior.
- `getCurrentHour()`
  - Executes `getCurrentHour` behavior.
- `getDayProgress()`
  - Executes `getDayProgress` behavior.
- `getSunDirection()`
  - Executes `getSunDirection` behavior.
- `instantToInstantData(@Nonnull Instant instant)`
  - Executes `instantToInstantData` behavior.
- `instantDataToInstant(@Nonnull InstantData instantData)`
  - Executes `instantDataToInstant` behavior.
- `clone()`
  - Executes `clone` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
