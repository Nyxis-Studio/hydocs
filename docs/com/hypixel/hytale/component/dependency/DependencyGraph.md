**Source Hash:** `a4ee78d91616e0c9fa9e666e44b8d587a2ed5ba558689fcfc78526c8b5aa038a`

# DependencyGraph

## Overview

## Constructor Descriptions
- `DependencyGraph(@Nonnull ISystem<ECS_TYPE>[] systems)`
  - Creates a `DependencyGraph` instance.

## Method Descriptions
- `getSystems()`: Add description.
  - Executes `getSystems` behavior.
- `resolveEdges(@Nonnull ComponentRegistry<ECS_TYPE> registry)`: Add description.
  - Executes `resolveEdges` behavior.
- `addEdgeFromRoot(@Nonnull ISystem<ECS_TYPE> afterSystem, int priority)`: Add description.
  - Executes `addEdgeFromRoot` behavior.
- `addEdge(@Nonnull ISystem<ECS_TYPE> beforeSystem, @Nonnull ISystem<ECS_TYPE> afterSystem, int priority)`: Add description.
  - Executes `addEdge` behavior.
- `addEdge(@Nonnull Edge<ECS_TYPE> edge)`: Add description.
  - Executes `addEdge` behavior.
- `sort(ISystem<ECS_TYPE>[] sortedSystems)`: Add description.
  - Executes `sort` behavior.
- `hasEdgeOfLaterPriority(ISystem<ECS_TYPE> system, int priority)`: Add description.
  - Executes `hasEdgeOfLaterPriority` behavior.
- `resolveEdgesFor(ISystem<ECS_TYPE> system)`: Add description.
  - Executes `resolveEdgesFor` behavior.
- `fulfillEdgesFor(ISystem<ECS_TYPE> system)`: Add description.
  - Executes `fulfillEdgesFor` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `emptyArray()`: Add description.
  - Executes `emptyArray` behavior.
- `compareTo(@Nonnull Edge<ECS_TYPE> o)`: Add description.
  - Executes `compareTo` behavior.

## Notes
- No additional notes.
