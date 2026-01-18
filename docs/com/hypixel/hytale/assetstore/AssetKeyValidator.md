# AssetKeyValidator

**Overview**
Asset key validator integrated with schema and validation systems.
Wraps an `AssetStore` to validate references and expose metadata to schemas.

**Constructors**
- `AssetKeyValidator(Supplier<AssetStore<K, ?, ?>> store)`: receives the store supplier used for validation.

**Methods**
- `getStore()`: resolves the current `AssetStore` from the supplier.
- `accept(K k, ValidationResults results)`: validates `k` using the store and records issues in `results`.
- `updateSchema(SchemaContext context, Schema target)`: annotates the schema with the referenced asset type.

**Notes**
- Implements `Validator<K>` and delegates to `AssetStore.validate`.
