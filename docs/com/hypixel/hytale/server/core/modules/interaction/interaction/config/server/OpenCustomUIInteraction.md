**Source Hash:** `6a75e6e39efd49e81aea517c645ddc6efa0525f90242549e109dc98ece3d3f4b`

# OpenCustomUIInteraction

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `firstRun(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nonnull CooldownHandler cooldownHandler)`: Add description.
  - Executes `firstRun` behavior.
- `registerCustomPageSupplier(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull S supplier)`: Add description.
  - Executes `registerCustomPageSupplier` behavior.
- `registerSimple(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull Function<PlayerRef, CustomUIPage> supplier)`: Add description.
  - Executes `registerSimple` behavior.
- `registerBlockCustomPage(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull Class<T> stateClass, @Nonnull BlockCustomPageSupplier<T> blockSupplier)`: Add description.
  - Executes `registerBlockCustomPage` behavior.
- `registerBlockCustomPage(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull Class<T> stateClass, @Nonnull BlockCustomPageSupplier<T> blockSupplier, boolean createState)`: Add description.
  - Executes `registerBlockCustomPage` behavior.
- `registerBlockEntityCustomPage(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull BlockEntityCustomPageSupplier blockSupplier)`: Add description.
  - Executes `registerBlockEntityCustomPage` behavior.
- `registerBlockEntityCustomPage(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull BlockEntityCustomPageSupplier blockSupplier, Supplier<Holder<ChunkStore>> creator)`: Add description.
  - Executes `registerBlockEntityCustomPage` behavior.
- `tryCreate(Ref<EntityStore> var1, ComponentAccessor<EntityStore> var2, PlayerRef var3, InteractionContext var4)`: Add description.
  - Executes `tryCreate` behavior.
- `tryCreate(PlayerRef var1, T var2)`: Add description.
  - Executes `tryCreate` behavior.
- `tryCreate(PlayerRef var1, Ref<ChunkStore> var2)`: Add description.
  - Executes `tryCreate` behavior.

## Notes
- No additional notes.
