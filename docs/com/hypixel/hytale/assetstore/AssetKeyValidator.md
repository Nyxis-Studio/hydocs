**Source Hash:** `a2194c1566f91be543565896a30802a44eca63adb7e1a311d4662c7e45c6c886`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetKeyValidator

## Overview
Asset key validator integrated with schema and validation systems. Wraps an `AssetStore` supplier to validate asset keys and annotate schema metadata.

## Field Descriptions
- `store`: Supplier that resolves the `AssetStore` used for validation and schema updates.

## Constructor Descriptions
- `AssetKeyValidator(Supplier<AssetStore<K, ?, ?>> store)`: Stores the asset store supplier used for later validation.

## Method Descriptions
- `getStore()`: Returns the current `AssetStore` instance from the supplier.
- `accept(K k, ValidationResults results)`: Delegates key validation to the asset store and records issues into the provided results.
- `updateSchema(SchemaContext context, Schema target)`: Sets the schema's asset reference name from the store's asset class.

## Usage Notes
- Implements `Validator<K>` and delegates to `AssetStore.validate` with the extra info from validation results.

## Examples
```java
Validator<String> validator = new AssetKeyValidator<>(storeSupplier);
validator.accept("my_key", results);
```
