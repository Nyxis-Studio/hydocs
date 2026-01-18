# CooldownHandler

## Overview
- Documentation for `CooldownHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction`.

## Constructors
- None.

## Methods
- `isOnCooldown(@Nonnull RootInteraction root, @Nonnull String id, float maxTime, @Nonnull float[] chargeTimes, boolean interruptRecharge)`
  - Executes `isOnCooldown` behavior.
- `resetCooldown(@Nonnull String id, float maxTime, @Nonnull float[] chargeTimes, boolean interruptRecharge)`
  - Executes `resetCooldown` behavior.
- `getCooldown(@Nonnull String id, float maxTime, @Nonnull float[] chargeTimes, boolean force, boolean interruptRecharge)`
  - Executes `getCooldown` behavior.
- `getCooldown(@Nonnull String id)`
  - Executes `getCooldown` behavior.
- `tick(float dt)`
  - Executes `tick` behavior.
- `setCooldownMax(float cooldownMax)`
  - Executes `setCooldownMax` behavior.
- `setCharges(@Nonnull float[] charges)`
  - Executes `setCharges` behavior.
- `hasCooldown(boolean deduct)`
  - Executes `hasCooldown` behavior.
- `hasMaxCharges()`
  - Executes `hasMaxCharges` behavior.
- `resetCharges()`
  - Executes `resetCharges` behavior.
- `resetCooldown()`
  - Executes `resetCooldown` behavior.
- `deductCharge()`
  - Executes `deductCharge` behavior.
- `getCooldown()`
  - Executes `getCooldown` behavior.
- `getCharges()`
  - Executes `getCharges` behavior.
- `interruptRecharge()`
  - Executes `interruptRecharge` behavior.
- `replenishCharge(int amount, boolean interrupt)`
  - Executes `replenishCharge` behavior.
- `increaseTime(float time)`
  - Executes `increaseTime` behavior.
- `increaseChargeTime(float time)`
  - Executes `increaseChargeTime` behavior.

## Notes
- No additional notes.
