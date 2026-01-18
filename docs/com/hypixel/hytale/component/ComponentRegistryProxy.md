# ComponentRegistryProxy

## Overview
- Documentation for `ComponentRegistryProxy`.
- Declared as a class in `com.hypixel.hytale.component`.

## Constructors
- `ComponentRegistryProxy(List<BooleanConsumer> registrations, ComponentRegistry<ECS_TYPE> registry)`
  - Creates a `ComponentRegistryProxy` instance.

## Methods
- `shutdown()`
  - Executes `shutdown` behavior.
- `registerComponent(@Nonnull Class<? super T> tClass, @Nonnull Supplier<T> supplier)`
  - Executes `registerComponent` behavior.
- `registerComponent(@Nonnull Class<? super T> tClass, @Nonnull String id, @Nonnull BuilderCodec<T> codec)`
  - Executes `registerComponent` behavior.
- `registerComponent(@Nonnull Class<? super T> tClass, @Nonnull String id, @Nonnull BuilderCodec<T> codec, boolean skipValidation)`
  - Executes `registerComponent` behavior.
- `registerResource(@Nonnull Class<? super T> tClass, @Nonnull Supplier<T> supplier)`
  - Executes `registerResource` behavior.
- `registerResource(@Nonnull Class<? super T> tClass, @Nonnull String id, @Nonnull BuilderCodec<T> codec)`
  - Executes `registerResource` behavior.
- `registerSpatialResource(@Nonnull Supplier<SpatialStructure<Ref<ECS_TYPE>>> supplier)`
  - Executes `registerSpatialResource` behavior.
- `registerSystemType(@Nonnull Class<? super T> systemTypeClass)`
  - Executes `registerSystemType` behavior.
- `registerEntityEventType(@Nonnull Class<? super T> eventTypeClass)`
  - Executes `registerEntityEventType` behavior.
- `registerWorldEventType(@Nonnull Class<? super T> eventTypeClass)`
  - Executes `registerWorldEventType` behavior.
- `registerSystemGroup()`
  - Executes `registerSystemGroup` behavior.
- `registerSystem(@Nonnull ISystem<ECS_TYPE> system)`
  - Executes `registerSystem` behavior.
- `registerSystem(@Nonnull ISystem<ECS_TYPE> system, boolean bypassClassCheck)`
  - Executes `registerSystem` behavior.
- `registerComponentType(@Nonnull ComponentType<ECS_TYPE, T> componentType)`
  - Executes `registerComponentType` behavior.
- `registerResourceType(@Nonnull ResourceType<ECS_TYPE, T> componentType)`
  - Executes `registerResourceType` behavior.
- `registerSystemType(@Nonnull SystemType<ECS_TYPE, T> systemType)`
  - Executes `registerSystemType` behavior.
- `registerEntityEventType(@Nonnull EntityEventType<ECS_TYPE, T> eventType)`
  - Executes `registerEntityEventType` behavior.
- `registerWorldEventType(@Nonnull WorldEventType<ECS_TYPE, T> eventType)`
  - Executes `registerWorldEventType` behavior.
- `registerSystemGroup(@Nonnull SystemGroup<ECS_TYPE> systemGroup)`
  - Executes `registerSystemGroup` behavior.

## Notes
- No additional notes.
