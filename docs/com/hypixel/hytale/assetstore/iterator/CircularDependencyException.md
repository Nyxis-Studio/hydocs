# CircularDependencyException

**Overview**
Runtime exception raised when asset store processing detects a circular dependency.
Builds a detailed message listing waiting stores and their unresolved dependencies.

**Constructors**
- `CircularDependencyException(Collection<AssetStore<?, ?, ?>> values, AssetStoreIterator iterator)`: formats a message from pending stores and iterator state.

**Methods**
- `makeMessage(Collection<AssetStore<?, ?, ?>> values, AssetStoreIterator iterator)`: builds a detailed dependency report for the exception.

**Notes**
- Resolves dependent stores via `AssetRegistry.getAssetStore` and fails if a store is missing.
