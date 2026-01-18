**Source Hash:** `3e5a63c76bb55739a6478ad3717f92a0cd5cdea537725ccf6b13a44c8bfdd01d`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetPack

## Overview
Represents an asset pack loaded from a root path and an optional file system. Stores pack metadata such as name, location, plugin manifest, and immutability.

## Field Descriptions
- `name`: Pack identifier string.
- `root`: Root path within the pack that contains asset data.
- `fileSystem`: Optional filesystem that backs the pack when loaded from archives.
- `isImmutable`: Whether the pack is considered read-only.
- `manifest`: Optional plugin manifest associated with the pack.
- `packLocation`: Original path used to locate the pack.

## Constructor Descriptions
- `AssetPack(Path packLocation, String name, Path root, FileSystem fileSystem, boolean isImmutable, PluginManifest manifest)`: Stores pack metadata and filesystem context.

## Method Descriptions
- `getName()`: Returns the pack name.
- `getRoot()`: Returns the pack root path.
- `getFileSystem()`: Returns the associated filesystem, or null when the default filesystem is used.
- `getManifest()`: Returns the plugin manifest associated with the pack.
- `isImmutable()`: Returns true if the pack is read-only.
- `getPackLocation()`: Returns the original pack location.
- `equals(Object o)`: Returns true when name and root match another asset pack.
- `hashCode()`: Computes a hash from the pack name and root path.
- `toString()`: Returns a string with the pack name, root, and filesystem.

## Usage Notes
- `fileSystem` can be null when the pack is on the default filesystem.

## Examples
```java
AssetPack pack = new AssetPack(location, "default", root, null, true, manifest);
```
