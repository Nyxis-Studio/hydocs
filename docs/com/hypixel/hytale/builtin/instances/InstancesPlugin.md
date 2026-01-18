**Source Hash:** `1b641cfa97c32b0d67e44268b2cc399c4c0fbd7c3f9aab93ad5a95fd6a2e7718`

# InstancesPlugin

## Overview

## Constructor Descriptions
- `InstancesPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `InstancesPlugin` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `spawnInstance(@Nonnull String name, @Nonnull World forWorld, @Nonnull Transform returnPoint)`: Add description.
  - Executes `spawnInstance` behavior.
- `spawnInstance(@Nonnull String name, @Nullable String worldName, @Nonnull World forWorld, @Nonnull Transform returnPoint)`: Add description.
  - Executes `spawnInstance` behavior.
- `teleportPlayerToLoadingInstance(@Nonnull Ref<EntityStore> entityRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull CompletableFuture<World> worldFuture, @Nullable Transform overrideReturn)`: Add description.
  - Executes `teleportPlayerToLoadingInstance` behavior.
- `teleportPlayerToInstance(@Nonnull Ref<EntityStore> playerRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull World targetWorld, @Nullable Transform overrideReturn)`: Add description.
  - Executes `teleportPlayerToInstance` behavior.
- `exitInstance(@Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `exitInstance` behavior.
- `safeRemoveInstance(@Nonnull String worldName)`: Add description.
  - Executes `safeRemoveInstance` behavior.
- `safeRemoveInstance(@Nonnull UUID worldUUID)`: Add description.
  - Executes `safeRemoveInstance` behavior.
- `safeRemoveInstance(@Nullable World instanceWorld)`: Add description.
  - Executes `safeRemoveInstance` behavior.
- `getInstanceAssetPath(@Nonnull String name)`: Add description.
  - Executes `getInstanceAssetPath` behavior.
- `doesInstanceAssetExist(@Nonnull String name)`: Add description.
  - Executes `doesInstanceAssetExist` behavior.
- `loadInstanceAssetForEdit(@Nonnull String name)`: Add description.
  - Executes `loadInstanceAssetForEdit` behavior.
- `getInstanceAssets()`: Add description.
  - Executes `getInstanceAssets` behavior.
- `preVisitDirectory(@Nonnull Path dir, @Nonnull BasicFileAttributes attrs)`: Add description.
  - Executes `preVisitDirectory` behavior.
- `onPlayerConnect(@Nonnull PlayerConnectEvent event)`: Add description.
  - Executes `onPlayerConnect` behavior.
- `onPlayerAddToWorld(@Nonnull AddPlayerToWorldEvent event)`: Add description.
  - Executes `onPlayerAddToWorld` behavior.
- `onPlayerReady(@Nonnull PlayerReadyEvent event)`: Add description.
  - Executes `onPlayerReady` behavior.
- `showInstanceDiscovery(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull UUID instanceUuid, @Nonnull InstanceDiscoveryConfig discoveryConfig)`: Add description.
  - Executes `showInstanceDiscovery` behavior.
- `onPlayerDrainFromWorld(@Nonnull DrainPlayerFromWorldEvent event)`: Add description.
  - Executes `onPlayerDrainFromWorld` behavior.
- `generateSchema(@Nonnull GenerateSchemaEvent event)`: Add description.
  - Executes `generateSchema` behavior.
- `validateInstanceAssets(@Nonnull LoadAssetEvent event)`: Add description.
  - Executes `validateInstanceAssets` behavior.
- `safeName(@Nonnull String name)`: Add description.
  - Executes `safeName` behavior.
- `getInstanceDataResourceType()`: Add description.
  - Executes `getInstanceDataResourceType` behavior.
- `getInstanceEntityConfigComponentType()`: Add description.
  - Executes `getInstanceEntityConfigComponentType` behavior.
- `getInstanceBlockComponentType()`: Add description.
  - Executes `getInstanceBlockComponentType` behavior.
- `getConfigurableInstanceBlockComponentType()`: Add description.
  - Executes `getConfigurableInstanceBlockComponentType` behavior.

## Notes
- No additional notes.
