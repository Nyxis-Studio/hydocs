# HistoricMetric

## Overview
- Documentation for `HistoricMetric`.
- Declared as a class in `com.hypixel.hytale.metrics.metric`.

## Constructors
- `HistoricMetric()`
  - Creates a `HistoricMetric` instance.
- `HistoricMetric(@Nonnull Builder builder)`
  - Creates a `HistoricMetric` instance.
- `HistoricMetric(this)`
  - Creates a `HistoricMetric` instance.

## Methods
- `getPeriodsNanos()`
  - Executes `getPeriodsNanos` behavior.
- `calculateMin(int periodIndex)`
  - Executes `calculateMin` behavior.
- `getAverage(int periodIndex)`
  - Executes `getAverage` behavior.
- `calculateMax(int periodIndex)`
  - Executes `calculateMax` behavior.
- `clear()`
  - Executes `clear` behavior.
- `add(long timestampNanos, long value)`
  - Executes `add` behavior.
- `getTimestamps(int periodIndex)`
  - Executes `getTimestamps` behavior.
- `getValues(int periodIndex)`
  - Executes `getValues` behavior.
- `getAllTimestamps()`
  - Executes `getAllTimestamps` behavior.
- `getAllValues()`
  - Executes `getAllValues` behavior.
- `setAllTimestamps(@Nonnull long[] timestamps)`
  - Executes `setAllTimestamps` behavior.
- `setAllValues(@Nonnull long[] values)`
  - Executes `setAllValues` behavior.
- `getLastValue()`
  - Executes `getLastValue` behavior.
- `builder(long minimumInterval, @Nonnull TimeUnit unit)`
  - Executes `builder` behavior.
- `addPeriod(long period, @Nonnull TimeUnit unit)`
  - Executes `addPeriod` behavior.
- `build()`
  - Executes `build` behavior.

## Notes
- No additional notes.
