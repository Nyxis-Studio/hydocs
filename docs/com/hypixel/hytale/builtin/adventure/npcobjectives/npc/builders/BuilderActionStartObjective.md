**Source Hash:** `69dd93b23f694946aa8a0153e4c49afe562eb063ab92e5e6a32549bd42d4e69e`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# BuilderActionStartObjective

## Overview
Builder configuration for the `ActionStartObjective` NPC action. Reads the objective asset ID and enforces interaction instruction usage.

## Field Descriptions
- `objectiveId`: Asset holder for the objective ID to start.

## Constructor Descriptions
- `BuilderActionStartObjective()`: Creates the action builder.

## Method Descriptions
- `getShortDescription()`: Returns a brief description for tooling.
- `getLongDescription()`: Returns the same description as the short description.
- `build(BuilderSupport builderSupport)`: Creates an `ActionStartObjective` instance.
- `getBuilderDescriptorState()`: Returns the stable descriptor state.
- `readConfig(JsonElement data)`: Reads the objective ID and validates instruction type.
- `getObjectiveId(BuilderSupport support)`: Returns the configured objective ID.

## Usage Notes
- Requires the `Objective` asset to exist; validation is handled by `ObjectiveExistsValidator`.

## Examples
```java
BuilderActionStartObjective builder = new BuilderActionStartObjective();
```
