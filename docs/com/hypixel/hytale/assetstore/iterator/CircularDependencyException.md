**Source Hash:** `c7f73db4b99ae07aec2821ea81f2c170c624985092844f21920d43a8d609669f`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# CircularDependencyException

## Overview
Runtime exception raised when asset store processing detects a circular dependency. Builds a detailed message listing waiting stores and their unresolved dependencies.

## Field Descriptions
- `none`: Exception type defines no fields.

## Constructor Descriptions
- `CircularDependencyException(Collection<AssetStore<?, ?, ?>> values, AssetStoreIterator iterator)`: Builds an error message from the pending stores and iterator state.

## Method Descriptions
- `makeMessage(Collection<AssetStore<?, ?, ?>> values, AssetStoreIterator iterator)`: Builds a dependency report listing stores still waiting and their unresolved dependencies.

## Usage Notes
- Throws an `IllegalArgumentException` if a referenced asset store is missing while building the message.

## Examples
```java
throw new CircularDependencyException(stores, iterator);
```
