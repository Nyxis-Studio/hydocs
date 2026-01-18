# InteractionModule

## Overview
- Documentation for `InteractionModule`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction`.

## Constructors
- `InteractionModule(@Nonnull JavaPluginInit init)`
  - Creates a `InteractionModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `handledLoadedRootInteractions(@Nonnull LoadedAssetsEvent<String, RootInteraction, ?> event)`
  - Executes `handledLoadedRootInteractions` behavior.
- `handledLoadedInteractions(@Nonnull LoadedAssetsEvent<String, Interaction, ?> event)`
  - Executes `handledLoadedInteractions` behavior.
- `handledRemovedInteractions(@Nonnull RemovedAssetsEvent<String, Interaction, ?> event)`
  - Executes `handledRemovedInteractions` behavior.
- `doMouseInteraction(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull MouseInteraction packet, @Nonnull Player playerComponent, @Nonnull PlayerRef playerRefComponent)`
  - Executes `doMouseInteraction` behavior.
- `getInteractionsComponentType()`
  - Executes `getInteractionsComponentType` behavior.
- `getInteractionManagerComponent()`
  - Executes `getInteractionManagerComponent` behavior.
- `getPlacedByComponentType()`
  - Executes `getPlacedByComponentType` behavior.
- `getBlockCounterResourceType()`
  - Executes `getBlockCounterResourceType` behavior.
- `getTrackedPlacementComponentType()`
  - Executes `getTrackedPlacementComponentType` behavior.

## Notes
- No additional notes.
