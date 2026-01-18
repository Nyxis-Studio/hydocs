# RootDependency

## Overview
- Documentation for `RootDependency`.
- Declared as a class in `com.hypixel.hytale.component.dependency`.

## Constructors
- `RootDependency(OrderPriority.CLOSEST)`
  - Creates a `RootDependency` instance.
- `RootDependency(OrderPriority.FURTHEST)`
  - Creates a `RootDependency` instance.
- `RootDependency(int priority)`
  - Creates a `RootDependency` instance.
- `RootDependency(@Nonnull OrderPriority priority)`
  - Creates a `RootDependency` instance.

## Methods
- `first()`
  - Executes `first` behavior.
- `last()`
  - Executes `last` behavior.
- `firstSet()`
  - Executes `firstSet` behavior.
- `lastSet()`
  - Executes `lastSet` behavior.
- `validate(@Nonnull ComponentRegistry<ECS_TYPE> registry)`
  - Executes `validate` behavior.
- `resolveGraphEdge(@Nonnull ComponentRegistry<ECS_TYPE> registry, @Nonnull ISystem<ECS_TYPE> thisSystem, @Nonnull DependencyGraph<ECS_TYPE> graph)`
  - Executes `resolveGraphEdge` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
