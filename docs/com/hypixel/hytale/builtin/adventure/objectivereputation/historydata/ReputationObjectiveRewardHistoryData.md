**Source Hash:** `731f292cb250489f1fad530201f9bd27793b20ba0c6eb54d55d3681c3b107be3`
**Last Updated:** 2026-01-18T19:03:47-03:00

# ReputationObjectiveRewardHistoryData

## Overview
History data record that tracks reputation rewards given to players upon objective completion. This final class extends ObjectiveRewardHistoryData to maintain a permanent record of which reputation group was affected and how much reputation was awarded, enabling tracking and potential rollback of reputation changes.

## Field Descriptions
- `CODEC`: BuilderCodec for serializing and deserializing history data instances. Validates reputation group ID existence and handles amount serialization.
- `reputationGroupId`: String identifier of the reputation group that was affected by the reward. Must be a valid existing reputation group.
- `amount`: Integer amount of reputation that was awarded or deducted. Can be positive for rewards or negative for penalties.

## Constructor Descriptions
- `ReputationObjectiveRewardHistoryData(String reputationGroupId, int amount)`: Creates a new history record with the specified reputation group and amount. Used when recording completed reputation rewards.
- `ReputationObjectiveRewardHistoryData()`: Protected default constructor for codec deserialization. Should not be used directly in application code.

## Method Descriptions
- `getReputationGroupId()`: Returns the ID of the reputation group that was affected by this historical reward. Used for tracking and auditing reputation changes.
- `getAmount()`: Returns the amount of reputation that was awarded or deducted. Positive values represent rewards, negative values represent penalties.
- `toString()`: Returns a string representation including reputation group ID and amount, along with inherited history data for debugging and logging.

## Usage Notes
- This class is final and cannot be extended to ensure data integrity
- History records are immutable once created to maintain accurate historical tracking
- The reputation group ID is validated against existing groups during codec operations
- These records enable administrative features like reputation reward auditing and rollback
- Automatically created by ReputationCompletion handlers when objectives are completed

## Examples
```java
// Create a history record for a completed reputation reward
ReputationObjectiveRewardHistoryData history = 
    new ReputationObjectiveRewardHistoryData("village_guards", 15);

// Access historical reward information
String affectedGroup = history.getReputationGroupId();
int reputationAwarded = history.getAmount();

// Used in objective history tracking
objectiveHistoryData.addRewardForPlayerUUID(playerUUID, history);
```
