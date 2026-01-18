# HudManager

## Overview
- Documentation for `HudManager`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities.player.hud`.

## Constructors
- `HudManager()`
  - Creates a `HudManager` instance.
- `HudManager(@Nonnull HudManager other)`
  - Creates a `HudManager` instance.

## Methods
- `getCustomHud()`
  - Executes `getCustomHud` behavior.
- `getVisibleHudComponents()`
  - Executes `getVisibleHudComponents` behavior.
- `setVisibleHudComponents(@Nonnull PlayerRef ref, HudComponent ... hudComponents)`
  - Executes `setVisibleHudComponents` behavior.
- `setVisibleHudComponents(@Nonnull PlayerRef ref, @Nonnull Set<HudComponent> hudComponents)`
  - Executes `setVisibleHudComponents` behavior.
- `showHudComponents(@Nonnull PlayerRef ref, HudComponent ... hudComponents)`
  - Executes `showHudComponents` behavior.
- `showHudComponents(@Nonnull PlayerRef ref, @Nonnull Set<HudComponent> hudComponents)`
  - Executes `showHudComponents` behavior.
- `hideHudComponents(@Nonnull PlayerRef ref, HudComponent ... hudComponents)`
  - Executes `hideHudComponents` behavior.
- `setCustomHud(@Nonnull PlayerRef ref, @Nullable CustomUIHud hud)`
  - Executes `setCustomHud` behavior.
- `resetHud(@Nonnull PlayerRef ref)`
  - Executes `resetHud` behavior.
- `resetUserInterface(@Nonnull PlayerRef ref)`
  - Executes `resetUserInterface` behavior.
- `sendVisibleHudComponents(@Nonnull PacketHandler packetHandler)`
  - Executes `sendVisibleHudComponents` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
