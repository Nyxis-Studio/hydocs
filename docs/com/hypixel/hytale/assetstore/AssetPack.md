# AssetPack

**Overview**
Represents an asset pack loaded from a root path and an optional file system.
Stores pack metadata such as name, location, plugin manifest, and immutability.

**Constructors**
- `AssetPack(Path packLocation, String name, Path root, FileSystem fileSystem, boolean isImmutable, PluginManifest manifest)`: initializes the pack with location, root, and manifest.

**Methods**
- `getName()`: returns the pack name.
- `getRoot()`: returns the pack root path.
- `getFileSystem()`: returns the associated `FileSystem`, if any.
- `getManifest()`: returns the pack `PluginManifest`.
- `isImmutable()`: indicates whether the pack is read-only.
- `getPackLocation()`: returns the original pack location.
- `equals(Object o)`: compares by name and root.
- `hashCode()`: hashes name and root.
- `toString()`: returns a textual representation of the pack.

**Notes**
- `fileSystem` may be null when the pack lives on the default filesystem.
