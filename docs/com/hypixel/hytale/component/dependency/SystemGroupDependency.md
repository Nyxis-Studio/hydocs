**Source Hash:** `a63f3238169a446a7aef52b0ceda81fee8c9627207047788e5332bf9ec26b0d4`

# SystemGroupDependency

## Overview

## Constructor Descriptions
- `SystemGroupDependency(@Nonnull Order order, @Nonnull SystemGroup<ECS_TYPE> group)`
  - Creates a `SystemGroupDependency` instance.
- `SystemGroupDependency(@Nonnull Order order, @Nonnull SystemGroup<ECS_TYPE> group, int priority)`
  - Creates a `SystemGroupDependency` instance.
- `SystemGroupDependency(@Nonnull Order order, @Nonnull SystemGroup<ECS_TYPE> group, @Nonnull OrderPriority priority)`
  - Creates a `SystemGroupDependency` instance.

## Method Descriptions
- `getGroup()`: Add description.
  - Executes `getGroup` behavior.
- `validate(@Nonnull ComponentRegistry<ECS_TYPE> registry)`: Add description.
  - Executes `validate` behavior.
- `resolveGraphEdge(@Nonnull ComponentRegistry<ECS_TYPE> registry, @Nonnull ISystem<ECS_TYPE> thisSystem, @Nonnull DependencyGraph<ECS_TYPE> graph)`: Add description.
  - Executes `resolveGraphEdge` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
