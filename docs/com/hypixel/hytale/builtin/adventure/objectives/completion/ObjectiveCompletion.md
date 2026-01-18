**Source Hash:** `f98d1ce03af9054c709170b5b8bc6337446fada2669bfc8778a1af700785fd5d`
**Last Updated:** 2026-01-18T19:03:47-03:00

# ObjectiveCompletion

## Overview
Abstract base class for objective completion handlers that define what happens when players complete objectives. This class provides the framework for various completion types like item rewards, reputation changes, or custom actions. Subclasses implement the specific logic for processing completion rewards.

## Field Descriptions
- `asset`: The ObjectiveCompletionAsset that defines the configuration for this completion handler. Protected final field that contains all necessary data for completion processing.

## Constructor Descriptions
- `ObjectiveCompletion(@Nonnull ObjectiveCompletionAsset asset)`: Creates a new completion handler with the specified asset configuration. The asset determines the type and parameters of the completion action.

## Method Descriptions
- `getAsset()`: Returns the ObjectiveCompletionAsset associated with this completion handler. Provides access to the configuration data used for completion processing.
- `handle(@Nonnull Objective objective, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Abstract method that subclasses must implement to define completion behavior. Called when an objective is completed, with access to the objective and entity store for processing rewards.
- `toString()`: Returns a string representation including the asset configuration for debugging and logging purposes.

## Usage Notes
- This class is abstract and must be subclassed to implement specific completion behaviors
- Completion handlers are registered with the ObjectivePlugin during setup
- The handle method is called automatically by the objective system when objectives complete
- Common completion types include item rewards, reputation changes, and custom scripted actions
- Completion handlers should be stateless to ensure consistent behavior

## Examples
```java
// Example subclass implementation
public class CustomCompletion extends ObjectiveCompletion {
    public CustomCompletion(@Nonnull CustomCompletionAsset asset) {
        super(asset);
    }
    
    @Override
    public void handle(@Nonnull Objective objective, 
                      @Nonnull ComponentAccessor<EntityStore> componentAccessor) {
        // Process completion logic here
        CustomCompletionAsset customAsset = (CustomCompletionAsset) getAsset();
        // Apply rewards, effects, or other completion actions
    }
}
```
