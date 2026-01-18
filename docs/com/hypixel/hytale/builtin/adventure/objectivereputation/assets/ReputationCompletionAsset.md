**Source Hash:** `1ae56b5e1d37784cb4b699618cf1d65d2aa790ef437ea680fb36420c9fffc512`
**Last Updated:** 2026-01-18T19:03:47-03:00

# ReputationCompletionAsset

## Overview
Asset configuration for reputation-based objective completion rewards. This class extends ObjectiveCompletionAsset to define how completing objectives affects player reputation with specific groups. It specifies which reputation group receives the change and the amount of reputation to award or deduct.

## Field Descriptions
- `CODEC`: BuilderCodec for serializing and deserializing ReputationCompletionAsset instances. Handles validation of reputation group ID and amount fields with appropriate constraints.
- `reputationGroupId`: String identifier of the reputation group that will be affected by this completion reward. Must be a valid, existing reputation group.
- `amount`: Integer amount of reputation change to apply, defaults to 1. Cannot be zero due to codec validation. Positive values increase reputation, negative values decrease it.

## Constructor Descriptions
- `ReputationCompletionAsset(String reputationGroupId, int amount)`: Creates a new reputation completion asset with specified group ID and amount. Used when programmatically creating completion rewards.
- `ReputationCompletionAsset()`: Protected default constructor for codec deserialization. Should not be used directly in application code.

## Method Descriptions
- `getReputationGroupId()`: Returns the ID of the reputation group that will be affected by this completion reward. Used by the reputation system to identify which group to modify.
- `getAmount()`: Returns the amount of reputation change to apply. Positive values increase reputation, negative values decrease it.
- `toString()`: Returns a string representation including reputation group ID and amount, along with inherited ObjectiveCompletionAsset information for debugging.

## Usage Notes
- The reputation group ID must correspond to an existing ReputationGroup asset
- The amount cannot be zero - use positive values for rewards and negative for penalties
- This completion type is automatically processed when objectives are completed
- Reputation changes are applied immediately upon objective completion

## Examples
```java
// Create a positive reputation reward
ReputationCompletionAsset reward = new ReputationCompletionAsset("village_guards", 10);

// Create a negative reputation penalty
ReputationCompletionAsset penalty = new ReputationCompletionAsset("thieves_guild", -5);

// Access configuration data
String groupId = asset.getReputationGroupId();
int reputationChange = asset.getAmount();
```
