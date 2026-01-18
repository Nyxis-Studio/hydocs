**Source Hash:** `95b6d3465b2898a63eb6a0c1903cf7ac7f72ad9885fe7d1fe4c269a4c530e4de`
**Last Updated:** 2026-01-18T19:03:47-03:00

# ReputationCompletion

## Overview
Completion handler that processes reputation-based rewards when objectives are completed. This class extends ObjectiveCompletion to handle reputation changes for all participants of an objective, applying the configured reputation amount to the specified reputation group and recording the change in objective history.

## Constructor Descriptions
- `ReputationCompletion(@Nonnull ReputationCompletionAsset asset)`: Creates a new reputation completion handler with the specified asset configuration. The asset defines which reputation group and amount will be affected.

## Method Descriptions
- `getAsset()`: Returns the ReputationCompletionAsset that defines the reputation group and amount for this completion handler. Cast from the parent ObjectiveCompletion asset.
- `handle(@Nonnull Objective objective, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Processes reputation rewards for all objective participants. Iterates through each participant, applies the reputation change via ReputationPlugin, and records the change in objective history data.
- `toString()`: Returns a string representation of this completion handler including inherited ObjectiveCompletion information for debugging purposes.

## Usage Notes
- This handler is automatically invoked when objectives with reputation completion rewards are completed
- Reputation changes are applied to all participants of the objective simultaneously
- The handler validates that participants are valid Player entities before applying changes
- Reputation changes are recorded in objective history for tracking and potential reversal
- Uses the ReputationPlugin to ensure proper reputation group validation and application

## Examples
```java
// Create reputation completion from asset
ReputationCompletionAsset asset = new ReputationCompletionAsset("village_guards", 10);
ReputationCompletion completion = new ReputationCompletion(asset);

// The handler automatically processes when objectives complete:
// 1. Finds all objective participants
// 2. Applies reputation change to each participant
// 3. Records the change in objective history
```
