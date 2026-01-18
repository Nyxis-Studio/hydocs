**Source Hash:** `c5c80504a1ab5596e948d640d3b4a6b7a41171a05e7c7701903ce94d58c89080`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# KillTrackerSystem

## Overview
Death system that reports NPC deaths to active kill task transactions. Iterates tracked tasks and forwards kill events for completion checks.

## Constructor Descriptions
- `KillTrackerSystem()`: Creates the kill tracker system.

## Method Descriptions
- `getQuery()`: Tracks NPC entities only.
- `onComponentAdded(Ref<EntityStore> ref, DeathComponent component, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`: Notifies all tracked kill tasks of the NPC death.

## Usage Notes
- Tasks are iterated in reverse order so removals during callbacks are safe.

## Examples
```java
KillTrackerSystem system = new KillTrackerSystem();
```
