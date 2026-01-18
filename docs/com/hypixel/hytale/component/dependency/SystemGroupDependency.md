# SystemGroupDependency

## Overview
- Documentation for `SystemGroupDependency`.
- Declared as a class in `com.hypixel.hytale.component.dependency`.

## Constructors
- `SystemGroupDependency(@Nonnull Order order, @Nonnull SystemGroup<ECS_TYPE> group)`
  - Creates a `SystemGroupDependency` instance.
- `SystemGroupDependency(@Nonnull Order order, @Nonnull SystemGroup<ECS_TYPE> group, int priority)`
  - Creates a `SystemGroupDependency` instance.
- `SystemGroupDependency(@Nonnull Order order, @Nonnull SystemGroup<ECS_TYPE> group, @Nonnull OrderPriority priority)`
  - Creates a `SystemGroupDependency` instance.

## Methods
- `getGroup()`
  - Executes `getGroup` behavior.
- `validate(@Nonnull ComponentRegistry<ECS_TYPE> registry)`
  - Executes `validate` behavior.
- `resolveGraphEdge(@Nonnull ComponentRegistry<ECS_TYPE> registry, @Nonnull ISystem<ECS_TYPE> thisSystem, @Nonnull DependencyGraph<ECS_TYPE> graph)`
  - Executes `resolveGraphEdge` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
