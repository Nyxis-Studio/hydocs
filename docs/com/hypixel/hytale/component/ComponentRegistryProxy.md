**Source Hash:** `de9b78657166269e2684684aedc33590538c97d78a4ebead00ec3c39b87103ac`

# ComponentRegistryProxy

## Overview

## Constructor Descriptions
- `ComponentRegistryProxy(List<BooleanConsumer> registrations, ComponentRegistry<ECS_TYPE> registry)`
  - Creates a `ComponentRegistryProxy` instance.

## Method Descriptions
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.
- `registerComponent(@Nonnull Class<? super T> tClass, @Nonnull Supplier<T> supplier)`: Add description.
  - Executes `registerComponent` behavior.
- `registerComponent(@Nonnull Class<? super T> tClass, @Nonnull String id, @Nonnull BuilderCodec<T> codec)`: Add description.
  - Executes `registerComponent` behavior.
- `registerComponent(@Nonnull Class<? super T> tClass, @Nonnull String id, @Nonnull BuilderCodec<T> codec, boolean skipValidation)`: Add description.
  - Executes `registerComponent` behavior.
- `registerResource(@Nonnull Class<? super T> tClass, @Nonnull Supplier<T> supplier)`: Add description.
  - Executes `registerResource` behavior.
- `registerResource(@Nonnull Class<? super T> tClass, @Nonnull String id, @Nonnull BuilderCodec<T> codec)`: Add description.
  - Executes `registerResource` behavior.
- `registerSpatialResource(@Nonnull Supplier<SpatialStructure<Ref<ECS_TYPE>>> supplier)`: Add description.
  - Executes `registerSpatialResource` behavior.
- `registerSystemType(@Nonnull Class<? super T> systemTypeClass)`: Add description.
  - Executes `registerSystemType` behavior.
- `registerEntityEventType(@Nonnull Class<? super T> eventTypeClass)`: Add description.
  - Executes `registerEntityEventType` behavior.
- `registerWorldEventType(@Nonnull Class<? super T> eventTypeClass)`: Add description.
  - Executes `registerWorldEventType` behavior.
- `registerSystemGroup()`: Add description.
  - Executes `registerSystemGroup` behavior.
- `registerSystem(@Nonnull ISystem<ECS_TYPE> system)`: Add description.
  - Executes `registerSystem` behavior.
- `registerSystem(@Nonnull ISystem<ECS_TYPE> system, boolean bypassClassCheck)`: Add description.
  - Executes `registerSystem` behavior.
- `registerComponentType(@Nonnull ComponentType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `registerComponentType` behavior.
- `registerResourceType(@Nonnull ResourceType<ECS_TYPE, T> componentType)`: Add description.
  - Executes `registerResourceType` behavior.
- `registerSystemType(@Nonnull SystemType<ECS_TYPE, T> systemType)`: Add description.
  - Executes `registerSystemType` behavior.
- `registerEntityEventType(@Nonnull EntityEventType<ECS_TYPE, T> eventType)`: Add description.
  - Executes `registerEntityEventType` behavior.
- `registerWorldEventType(@Nonnull WorldEventType<ECS_TYPE, T> eventType)`: Add description.
  - Executes `registerWorldEventType` behavior.
- `registerSystemGroup(@Nonnull SystemGroup<ECS_TYPE> systemGroup)`: Add description.
  - Executes `registerSystemGroup` behavior.

## Notes
- No additional notes.
