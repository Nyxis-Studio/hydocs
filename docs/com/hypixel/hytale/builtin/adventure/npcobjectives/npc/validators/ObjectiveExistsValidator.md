**Source Hash:** `9c5d20034f60c3313e9a41e591f1f47278b4040424bf434e862c897f3ed7b997`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# ObjectiveExistsValidator

## Overview
Asset validator that ensures an objective asset exists for a given name. Used by NPC builder configuration to validate objective references.

## Field Descriptions
- `DEFAULT_INSTANCE`: Shared validator instance used for required validation.

## Constructor Descriptions
- `ObjectiveExistsValidator()`: Creates the default validator instance.
- `ObjectiveExistsValidator(EnumSet<AssetValidator.Config> config)`: Creates a validator with custom configuration.

## Method Descriptions
- `getDomain()`: Returns the domain name "Objective".
- `test(String objective)`: Returns true when the objective asset exists.
- `errorMessage(String objective, String attributeName)`: Returns an error message for missing objectives.
- `getAssetName()`: Returns the asset class name for validation output.
- `required()`: Returns the shared validator instance.
- `withConfig(EnumSet<AssetValidator.Config> config)`: Returns a validator with custom configuration.

## Examples
```java
ObjectiveExistsValidator validator = ObjectiveExistsValidator.required();
```
