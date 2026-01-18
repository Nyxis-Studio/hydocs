# ISensorEntityCollector

## Overview
- Documentation for `ISensorEntityCollector`.
- Declared as a interface in `com.hypixel.hytale.server.npc.corecomponents`.

## Constructors
- `ISensorEntityCollector()`
  - Creates a `ISensorEntityCollector` instance.

## Methods
- `init(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `init` behavior.
- `collectMatching(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `collectMatching` behavior.
- `collectNonMatching(@Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `collectNonMatching` behavior.
- `terminateOnFirstMatch()`
  - Executes `terminateOnFirstMatch` behavior.
- `cleanup()`
  - Executes `cleanup` behavior.
- `init(@Nonnull Ref<EntityStore> var1, @Nonnull Role var2, @Nonnull ComponentAccessor<EntityStore> var3)`
  - Executes `init` behavior.
- `collectMatching(@Nonnull Ref<EntityStore> var1, @Nonnull Ref<EntityStore> var2, @Nonnull ComponentAccessor<EntityStore> var3)`
  - Executes `collectMatching` behavior.
- `collectNonMatching(@Nonnull Ref<EntityStore> var1, @Nonnull ComponentAccessor<EntityStore> var2)`
  - Executes `collectNonMatching` behavior.

## Notes
- No additional notes.
