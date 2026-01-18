# IComponentRegistry

## Overview
- Documentation for `IComponentRegistry`.
- Declared as a interface in `com.hypixel.hytale.component`.

## Constructors
- None.

## Methods
- `registerComponent(@Nonnull Class<? super T> var1, @Nonnull Supplier<T> var2)`
  - Executes `registerComponent` behavior.
- `registerComponent(@Nonnull Class<? super T> var1, @Nonnull String var2, @Nonnull BuilderCodec<T> var3)`
  - Executes `registerComponent` behavior.
- `registerResource(@Nonnull Class<? super T> var1, @Nonnull Supplier<T> var2)`
  - Executes `registerResource` behavior.
- `registerResource(@Nonnull Class<? super T> var1, @Nonnull String var2, @Nonnull BuilderCodec<T> var3)`
  - Executes `registerResource` behavior.
- `registerSystemType(@Nonnull Class<? super T> var1)`
  - Executes `registerSystemType` behavior.
- `registerEntityEventType(@Nonnull Class<? super T> var1)`
  - Executes `registerEntityEventType` behavior.
- `registerWorldEventType(@Nonnull Class<? super T> var1)`
  - Executes `registerWorldEventType` behavior.
- `registerSystemGroup()`
  - Executes `registerSystemGroup` behavior.
- `registerSystem(@Nonnull ISystem<ECS_TYPE> var1)`
  - Executes `registerSystem` behavior.
- `registerSpatialResource(@Nonnull Supplier<SpatialStructure<Ref<ECS_TYPE>>> var1)`
  - Executes `registerSpatialResource` behavior.

## Notes
- No additional notes.
