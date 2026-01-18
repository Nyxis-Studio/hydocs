**Source Hash:** `8029c26ae15f111440fe72a1e05d5721f6a51a3b2169e2623eb952123c7ba2d9`
**Last Updated:** 2026-01-18T19:03:47-03:00

# ShopExistsValidator

## Overview
Asset validator that verifies the existence of shop assets by their identifier. This validator is used during NPC action configuration to ensure that referenced shops actually exist in the game's asset registry before allowing actions to be created.

## Field Descriptions
- `DEFAULT_INSTANCE`: Static singleton instance of ShopExistsValidator used for required validation. Provides a shared validator instance to avoid unnecessary object creation.

## Constructor Descriptions
- `ShopExistsValidator()`: Private default constructor that creates a basic validator instance. Used internally for the singleton pattern.
- `ShopExistsValidator(EnumSet<AssetValidator.Config> config)`: Private constructor that creates a validator with specific configuration options. Used by the withConfig factory method.

## Method Descriptions
- `getDomain()`: Returns "Shop" as the domain name for this validator. Used to identify the type of asset being validated in error messages and logging.
- `test(String marker)`: Tests whether a shop asset with the given marker (ID) exists in the ShopAsset registry. Returns true if the shop exists, false otherwise.
- `errorMessage(String marker, String attributeName)`: Generates a descriptive error message when validation fails, indicating which shop asset was not found for which attribute.
- `getAssetName()`: Returns the simple class name "ShopAsset" to identify the asset type being validated. Used in error reporting and debugging.
- `required()`: Static factory method that returns the singleton DEFAULT_INSTANCE for required validation scenarios. This is the standard way to obtain a validator.
- `withConfig(EnumSet<AssetValidator.Config> config)`: Static factory method that creates a new validator instance with custom configuration options.

## Usage Notes
- Use `required()` for standard validation scenarios where shop assets must exist
- The validator checks against the ShopAsset registry, not the filesystem
- Error messages include both the missing shop ID and the attribute name for debugging
- Validation occurs during NPC action configuration, not at runtime

## Examples
```java
// Standard usage for required validation
AssetValidator validator = ShopExistsValidator.required();

// Custom configuration
EnumSet<AssetValidator.Config> config = EnumSet.of(AssetValidator.Config.OPTIONAL);
ShopExistsValidator customValidator = ShopExistsValidator.withConfig(config);

// Validation test
boolean exists = validator.test("village_blacksmith_shop");
if (!exists) {
    String error = validator.errorMessage("village_blacksmith_shop", "Shop");
}
```
