# InstancesPlugin

## Overview
- Documentation for `InstancesPlugin`.
- Declared as a class in `com.hypixel.hytale.builtin.instances`.

## Constructors
- `InstancesPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `InstancesPlugin` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `spawnInstance(@Nonnull String name, @Nonnull World forWorld, @Nonnull Transform returnPoint)`
  - Executes `spawnInstance` behavior.
- `spawnInstance(@Nonnull String name, @Nullable String worldName, @Nonnull World forWorld, @Nonnull Transform returnPoint)`
  - Executes `spawnInstance` behavior.
- `teleportPlayerToLoadingInstance(@Nonnull Ref<EntityStore> entityRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull CompletableFuture<World> worldFuture, @Nullable Transform overrideReturn)`
  - Executes `teleportPlayerToLoadingInstance` behavior.
- `teleportPlayerToInstance(@Nonnull Ref<EntityStore> playerRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull World targetWorld, @Nullable Transform overrideReturn)`
  - Executes `teleportPlayerToInstance` behavior.
- `exitInstance(@Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `exitInstance` behavior.
- `safeRemoveInstance(@Nonnull String worldName)`
  - Executes `safeRemoveInstance` behavior.
- `safeRemoveInstance(@Nonnull UUID worldUUID)`
  - Executes `safeRemoveInstance` behavior.
- `safeRemoveInstance(@Nullable World instanceWorld)`
  - Executes `safeRemoveInstance` behavior.
- `getInstanceAssetPath(@Nonnull String name)`
  - Executes `getInstanceAssetPath` behavior.
- `doesInstanceAssetExist(@Nonnull String name)`
  - Executes `doesInstanceAssetExist` behavior.
- `loadInstanceAssetForEdit(@Nonnull String name)`
  - Executes `loadInstanceAssetForEdit` behavior.
- `getInstanceAssets()`
  - Executes `getInstanceAssets` behavior.
- `preVisitDirectory(@Nonnull Path dir, @Nonnull BasicFileAttributes attrs)`
  - Executes `preVisitDirectory` behavior.
- `onPlayerConnect(@Nonnull PlayerConnectEvent event)`
  - Executes `onPlayerConnect` behavior.
- `onPlayerAddToWorld(@Nonnull AddPlayerToWorldEvent event)`
  - Executes `onPlayerAddToWorld` behavior.
- `onPlayerReady(@Nonnull PlayerReadyEvent event)`
  - Executes `onPlayerReady` behavior.
- `showInstanceDiscovery(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull UUID instanceUuid, @Nonnull InstanceDiscoveryConfig discoveryConfig)`
  - Executes `showInstanceDiscovery` behavior.
- `onPlayerDrainFromWorld(@Nonnull DrainPlayerFromWorldEvent event)`
  - Executes `onPlayerDrainFromWorld` behavior.
- `generateSchema(@Nonnull GenerateSchemaEvent event)`
  - Executes `generateSchema` behavior.
- `validateInstanceAssets(@Nonnull LoadAssetEvent event)`
  - Executes `validateInstanceAssets` behavior.
- `safeName(@Nonnull String name)`
  - Executes `safeName` behavior.
- `getInstanceDataResourceType()`
  - Executes `getInstanceDataResourceType` behavior.
- `getInstanceEntityConfigComponentType()`
  - Executes `getInstanceEntityConfigComponentType` behavior.
- `getInstanceBlockComponentType()`
  - Executes `getInstanceBlockComponentType` behavior.
- `getConfigurableInstanceBlockComponentType()`
  - Executes `getConfigurableInstanceBlockComponentType` behavior.

## Notes
- No additional notes.
