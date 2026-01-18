# NPCLoadTimeValidationHelper

## Overview
- Documentation for `NPCLoadTimeValidationHelper`.
- Declared as a class in `com.hypixel.hytale.server.npc.validators`.

## Constructors
- `NPCLoadTimeValidationHelper(String fileName, Model spawnModel, boolean isAbstract)`
  - Creates a `NPCLoadTimeValidationHelper` instance.

## Methods
- `setInventorySizes(int inventorySize, int hotbarSize, int offHandSize)`
  - Executes `setInventorySizes` behavior.
- `getSpawnModel()`
  - Executes `getSpawnModel` behavior.
- `isAbstract()`
  - Executes `isAbstract` behavior.
- `isParentSensorOnce()`
  - Executes `isParentSensorOnce` behavior.
- `updateParentSensorOnce(boolean parentSensorOnce)`
  - Executes `updateParentSensorOnce` behavior.
- `clearParentSensorOnce()`
  - Executes `clearParentSensorOnce` behavior.
- `setIsVariant()`
  - Executes `setIsVariant` behavior.
- `isVariant()`
  - Executes `isVariant` behavior.
- `getValueStoreValidator()`
  - Executes `getValueStoreValidator` behavior.
- `getCurrentStateName()`
  - Executes `getCurrentStateName` behavior.
- `pushCurrentStateName(@Nonnull String currentStateName)`
  - Executes `pushCurrentStateName` behavior.
- `popCurrentStateName()`
  - Executes `popCurrentStateName` behavior.
- `validateAnimation(@Nullable String animation)`
  - Executes `validateAnimation` behavior.
- `registerMotionControllerType(Class<? extends MotionController> clazz)`
  - Executes `registerMotionControllerType` behavior.
- `requireMotionControllerType(Class<? extends MotionController> clazz)`
  - Executes `requireMotionControllerType` behavior.
- `validateMotionControllers(@Nonnull List<String> errors)`
  - Executes `validateMotionControllers` behavior.
- `validateInventoryHasSlot(int slot, String context, @Nonnull List<String> errors)`
  - Executes `validateInventoryHasSlot` behavior.
- `validateHotbarHasSlot(int slot, String context, @Nonnull List<String> errors)`
  - Executes `validateHotbarHasSlot` behavior.
- `validateOffHandHasSlot(int slot, String context, @Nonnull List<String> errors)`
  - Executes `validateOffHandHasSlot` behavior.
- `pushFilterSet()`
  - Executes `pushFilterSet` behavior.
- `popFilterSet()`
  - Executes `popFilterSet` behavior.
- `hasSeenFilter(String filter)`
  - Executes `hasSeenFilter` behavior.
- `setPrioritiserProvidedFilterTypes(Set<String> prioritiserProvidedFilterTypes)`
  - Executes `setPrioritiserProvidedFilterTypes` behavior.
- `isFilterExternallyProvided(String filter)`
  - Executes `isFilterExternallyProvided` behavior.
- `clearPrioritiserProvidedFilterTypes()`
  - Executes `clearPrioritiserProvidedFilterTypes` behavior.

## Notes
- No additional notes.
