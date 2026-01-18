# DependencyGraph

## Overview
- Documentation for `DependencyGraph`.
- Declared as a class in `com.hypixel.hytale.component.dependency`.

## Constructors
- `DependencyGraph(@Nonnull ISystem<ECS_TYPE>[] systems)`
  - Creates a `DependencyGraph` instance.

## Methods
- `getSystems()`
  - Executes `getSystems` behavior.
- `resolveEdges(@Nonnull ComponentRegistry<ECS_TYPE> registry)`
  - Executes `resolveEdges` behavior.
- `addEdgeFromRoot(@Nonnull ISystem<ECS_TYPE> afterSystem, int priority)`
  - Executes `addEdgeFromRoot` behavior.
- `addEdge(@Nonnull ISystem<ECS_TYPE> beforeSystem, @Nonnull ISystem<ECS_TYPE> afterSystem, int priority)`
  - Executes `addEdge` behavior.
- `addEdge(@Nonnull Edge<ECS_TYPE> edge)`
  - Executes `addEdge` behavior.
- `sort(ISystem<ECS_TYPE>[] sortedSystems)`
  - Executes `sort` behavior.
- `hasEdgeOfLaterPriority(ISystem<ECS_TYPE> system, int priority)`
  - Executes `hasEdgeOfLaterPriority` behavior.
- `resolveEdgesFor(ISystem<ECS_TYPE> system)`
  - Executes `resolveEdgesFor` behavior.
- `fulfillEdgesFor(ISystem<ECS_TYPE> system)`
  - Executes `fulfillEdgesFor` behavior.
- `toString()`
  - Executes `toString` behavior.
- `emptyArray()`
  - Executes `emptyArray` behavior.
- `compareTo(@Nonnull Edge<ECS_TYPE> o)`
  - Executes `compareTo` behavior.

## Notes
- No additional notes.
