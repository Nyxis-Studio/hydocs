# UnknownComponents

## Overview
- Documentation for `UnknownComponents`.
- Declared as a class in `com.hypixel.hytale.component.data.unknown`.

## Constructors
- `UnknownComponents()`
  - Creates a `UnknownComponents` instance.
- `UnknownComponents(Map<String, BsonDocument> unknownComponents)`
  - Creates a `UnknownComponents` instance.

## Methods
- `addComponent(String componentId, Component<ECS_TYPE> component, @Nonnull Codec<Component<ECS_TYPE>> codec)`
  - Executes `addComponent` behavior.
- `addComponent(String componentId, @Nonnull TempUnknownComponent<ECS_TYPE> component)`
  - Executes `addComponent` behavior.
- `contains(String componentId)`
  - Executes `contains` behavior.
- `removeComponent(String componentId, @Nonnull Codec<T> codec)`
  - Executes `removeComponent` behavior.
- `getUnknownComponents()`
  - Executes `getUnknownComponents` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
