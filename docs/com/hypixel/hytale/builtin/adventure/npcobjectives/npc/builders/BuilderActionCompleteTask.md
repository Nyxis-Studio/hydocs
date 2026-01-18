**Source Hash:** `7d827078ba836cdbd8bea4bfdd70b33d56aec276a457c9aff5a4016c068935cb`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# BuilderActionCompleteTask

## Overview
Builder configuration for the `ActionCompleteTask` NPC action. Supports optional animation playback configuration and enforces interaction instruction usage.

## Field Descriptions
- `playAnimation`: Boolean holder controlling whether completion animations should play.

## Constructor Descriptions
- `BuilderActionCompleteTask()`: Creates the action builder.

## Method Descriptions
- `getShortDescription()`: Returns a brief description for UI/tooling.
- `getLongDescription()`: Returns the detailed description of the action.
- `build(BuilderSupport builderSupport)`: Creates an `ActionCompleteTask` instance.
- `readConfig(JsonElement data)`: Reads configuration data and validates instruction type.
- `getBuilderDescriptorState()`: Returns the stable descriptor state.
- `isPlayAnimation(BuilderSupport support)`: Returns whether to play the completion animation.

## Usage Notes
- `PlayAnimation` defaults to true if not specified in config.

## Examples
```java
BuilderActionCompleteTask builder = new BuilderActionCompleteTask();
```
