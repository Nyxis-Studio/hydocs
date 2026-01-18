# OpenCustomUIInteraction

## Overview
- Documentation for `OpenCustomUIInteraction`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.server`.

## Constructors
- None.

## Methods
- `firstRun(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `firstRun` behavior.
- `registerCustomPageSupplier(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull S supplier)`
  - Executes `registerCustomPageSupplier` behavior.
- `registerSimple(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull Function<PlayerRef, CustomUIPage> supplier)`
  - Executes `registerSimple` behavior.
- `registerBlockCustomPage(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull Class<T> stateClass, @Nonnull BlockCustomPageSupplier<T> blockSupplier)`
  - Executes `registerBlockCustomPage` behavior.
- `registerBlockCustomPage(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull Class<T> stateClass, @Nonnull BlockCustomPageSupplier<T> blockSupplier, boolean createState)`
  - Executes `registerBlockCustomPage` behavior.
- `registerBlockEntityCustomPage(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull BlockEntityCustomPageSupplier blockSupplier)`
  - Executes `registerBlockEntityCustomPage` behavior.
- `registerBlockEntityCustomPage(@Nonnull PluginBase plugin, Class<?> tClass, String id, @Nonnull BlockEntityCustomPageSupplier blockSupplier, Supplier<Holder<ChunkStore>> creator)`
  - Executes `registerBlockEntityCustomPage` behavior.
- `tryCreate(Ref<EntityStore> var1, ComponentAccessor<EntityStore> var2, PlayerRef var3, InteractionContext var4)`
  - Executes `tryCreate` behavior.
- `tryCreate(PlayerRef var1, T var2)`
  - Executes `tryCreate` behavior.
- `tryCreate(PlayerRef var1, Ref<ChunkStore> var2)`
  - Executes `tryCreate` behavior.

## Notes
- No additional notes.
