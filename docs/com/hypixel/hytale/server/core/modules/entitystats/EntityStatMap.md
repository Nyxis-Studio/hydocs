**Source Hash:** `0b962afb52c815e36d2f4ff2e8ec279c9dfb363eda2744afaef905ae106ddd9b`

# EntityStatMap

## Overview

## Constructor Descriptions
- `EntityStatMap()`
  - Creates a `EntityStatMap` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `size()`: Add description.
  - Executes `size` behavior.
- `get(int index)`: Add description.
  - Executes `get` behavior.
- `get(String entityStat)`: Add description.
  - Executes `get` behavior.
- `update()`: Add description.
  - Executes `update` behavior.
- `getModifier(int index, String key)`: Add description.
  - Executes `getModifier` behavior.
- `putModifier(int index, String key, Modifier modifier)`: Add description.
  - Executes `putModifier` behavior.
- `putModifier(Predictable predictable, int index, String key, Modifier modifier)`: Add description.
  - Executes `putModifier` behavior.
- `removeModifier(int index, String key)`: Add description.
  - Executes `removeModifier` behavior.
- `removeModifier(Predictable predictable, int index, String key)`: Add description.
  - Executes `removeModifier` behavior.
- `setStatValue(int index, float newValue)`: Add description.
  - Executes `setStatValue` behavior.
- `setStatValue(Predictable predictable, int index, float newValue)`: Add description.
  - Executes `setStatValue` behavior.
- `addStatValue(int index, float amount)`: Add description.
  - Executes `addStatValue` behavior.
- `addStatValue(Predictable predictable, int index, float amount)`: Add description.
  - Executes `addStatValue` behavior.
- `subtractStatValue(int index, float amount)`: Add description.
  - Executes `subtractStatValue` behavior.
- `subtractStatValue(Predictable predictable, int index, float amount)`: Add description.
  - Executes `subtractStatValue` behavior.
- `minimizeStatValue(int index)`: Add description.
  - Executes `minimizeStatValue` behavior.
- `minimizeStatValue(Predictable predictable, int index)`: Add description.
  - Executes `minimizeStatValue` behavior.
- `maximizeStatValue(int index)`: Add description.
  - Executes `maximizeStatValue` behavior.
- `maximizeStatValue(Predictable predictable, int index)`: Add description.
  - Executes `maximizeStatValue` behavior.
- `resetStatValue(int index)`: Add description.
  - Executes `resetStatValue` behavior.
- `resetStatValue(Predictable predictable, int index)`: Add description.
  - Executes `resetStatValue` behavior.
- `getSelfUpdates()`: Add description.
  - Executes `getSelfUpdates` behavior.
- `getSelfStatValues()`: Add description.
  - Executes `getSelfStatValues` behavior.
- `consumeSelfUpdates()`: Add description.
  - Executes `consumeSelfUpdates` behavior.
- `clearUpdates()`: Add description.
  - Executes `clearUpdates` behavior.
- `consumeOtherUpdates()`: Add description.
  - Executes `consumeOtherUpdates` behavior.
- `updatesToProtocol(@Nonnull Int2ObjectMap<List<EntityStatUpdate>> localUpdates)`: Add description.
  - Executes `updatesToProtocol` behavior.
- `createInitUpdate(boolean all)`: Add description.
  - Executes `createInitUpdate` behavior.
- `consumeSelfNetworkOutdated()`: Add description.
  - Executes `consumeSelfNetworkOutdated` behavior.
- `consumeNetworkOutdated()`: Add description.
  - Executes `consumeNetworkOutdated` behavior.
- `addInitChange(int index, @Nonnull EntityStatValue value)`: Add description.
  - Executes `addInitChange` behavior.
- `addChange(Predictable predictable, int index, @Nonnull EntityStatOp op, float previousValue, float value)`: Add description.
  - Executes `addChange` behavior.
- `addChange(Predictable predictable, int index, @Nonnull EntityStatOp op, float previousValue, float value, Map<String, Modifier> modifierMap)`: Add description.
  - Executes `addChange` behavior.
- `addChange(Predictable predictable, int index, EntityStatOp op, float previousValue, String key, @Nullable Modifier modifier)`: Add description.
  - Executes `addChange` behavior.
- `tryMergeUpdate(@Nonnull List<EntityStatUpdate> updates, @Nonnull EntityStatOp op, float value, @Nullable Map<String, Modifier> modifierMap, boolean isPredictable)`: Add description.
  - Executes `tryMergeUpdate` behavior.
- `processStatChanges(Predictable predictable, @Nonnull Int2FloatMap entityStats, ValueType valueType, @Nonnull ChangeStatBehaviour changeStatBehaviour)`: Add description.
  - Executes `processStatChanges` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `makeInitChange(@Nonnull EntityStatValue value)`: Add description.
  - Executes `makeInitChange` behavior.

## Notes
- No additional notes.
