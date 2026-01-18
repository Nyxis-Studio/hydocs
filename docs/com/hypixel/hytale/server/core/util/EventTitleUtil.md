# EventTitleUtil

## Overview
- Documentation for `EventTitleUtil`.
- Declared as a class in `com.hypixel.hytale.server.core.util`.

## Constructors
- None.

## Methods
- `showEventTitleToUniverse(@Nonnull Message primaryTitle, @Nonnull Message secondaryTitle, boolean isMajor, String icon, float duration, float fadeInDuration, float fadeOutDuration)`
  - Executes `showEventTitleToUniverse` behavior.
- `showEventTitleToWorld(@Nonnull Message primaryTitle, @Nonnull Message secondaryTitle, boolean isMajor, String icon, float duration, float fadeInDuration, float fadeOutDuration, @Nonnull Store<EntityStore> store)`
  - Executes `showEventTitleToWorld` behavior.
- `hideEventTitleFromWorld(float fadeOutDuration, @Nonnull Store<EntityStore> store)`
  - Executes `hideEventTitleFromWorld` behavior.
- `showEventTitleToPlayer(@Nonnull PlayerRef playerRefComponent, @Nonnull Message primaryTitle, @Nonnull Message secondaryTitle, boolean isMajor, @Nullable String icon, float duration, float fadeInDuration, float fadeOutDuration)`
  - Executes `showEventTitleToPlayer` behavior.
- `showEventTitleToPlayer(@Nonnull PlayerRef playerRefComponent, @Nonnull Message primaryTitle, @Nonnull Message secondaryTitle, boolean isMajor)`
  - Executes `showEventTitleToPlayer` behavior.
- `hideEventTitleFromPlayer(@Nonnull PlayerRef playerRefComponent, float fadeOutDuration)`
  - Executes `hideEventTitleFromPlayer` behavior.

## Notes
- No additional notes.
