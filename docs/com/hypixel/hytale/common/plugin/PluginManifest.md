**Source Hash:** `e42d3ac72ac641cf800c3aaf93944f6ae866d1ccc0ab2a3cad3bf198bbcb3106`

# PluginManifest

## Overview

## Constructor Descriptions
- `PluginManifest()`
  - Creates a `PluginManifest` instance.
- `PluginManifest(@Nonnull String group, @Nonnull String name, @Nonnull Semver version, @Nullable String description, @Nonnull List<AuthorInfo> authors, @Nullable String website, @Nullable String main, @Nullable SemverRange serverVersion, @Nonnull Map<PluginIdentifier, SemverRange> dependencies, @Nonnull Map<PluginIdentifier, SemverRange> optionalDependencies, @Nonnull Map<PluginIdentifier, SemverRange> loadBefore, @Nonnull List<PluginManifest> subPlugins, boolean disabledByDefault)`
  - Creates a `PluginManifest` instance.
- `PluginManifest(this.group, this.name, this.version, this.description, Collections.emptyList()`
  - Creates a `PluginManifest` instance.

## Method Descriptions
- `getGroup()`: Add description.
  - Executes `getGroup` behavior.
- `getName()`: Add description.
  - Executes `getName` behavior.
- `getVersion()`: Add description.
  - Executes `getVersion` behavior.
- `getDescription()`: Add description.
  - Executes `getDescription` behavior.
- `getAuthors()`: Add description.
  - Executes `getAuthors` behavior.
- `getWebsite()`: Add description.
  - Executes `getWebsite` behavior.
- `setGroup(@Nonnull String group)`: Add description.
  - Executes `setGroup` behavior.
- `setName(@Nonnull String name)`: Add description.
  - Executes `setName` behavior.
- `setVersion(@Nullable Semver version)`: Add description.
  - Executes `setVersion` behavior.
- `setDescription(@Nullable String description)`: Add description.
  - Executes `setDescription` behavior.
- `setAuthors(@Nonnull List<AuthorInfo> authors)`: Add description.
  - Executes `setAuthors` behavior.
- `setWebsite(@Nullable String website)`: Add description.
  - Executes `setWebsite` behavior.
- `getMain()`: Add description.
  - Executes `getMain` behavior.
- `getServerVersion()`: Add description.
  - Executes `getServerVersion` behavior.
- `getDependencies()`: Add description.
  - Executes `getDependencies` behavior.
- `injectDependency(PluginIdentifier identifier, SemverRange range)`: Add description.
  - Executes `injectDependency` behavior.
- `getOptionalDependencies()`: Add description.
  - Executes `getOptionalDependencies` behavior.
- `getLoadBefore()`: Add description.
  - Executes `getLoadBefore` behavior.
- `isDisabledByDefault()`: Add description.
  - Executes `isDisabledByDefault` behavior.
- `includesAssetPack()`: Add description.
  - Executes `includesAssetPack` behavior.
- `getSubPlugins()`: Add description.
  - Executes `getSubPlugins` behavior.
- `inherit(@Nonnull PluginManifest manifest)`: Add description.
  - Executes `inherit` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `corePlugin(@Nonnull Class<?> pluginClass)`: Add description.
  - Executes `corePlugin` behavior.
- `description(@Nonnull String description)`: Add description.
  - Executes `description` behavior.
- `depends(Class<?> ... dependencies)`: Add description.
  - Executes `depends` behavior.
- `optDepends(Class<?> ... dependencies)`: Add description.
  - Executes `optDepends` behavior.
- `loadsBefore(Class<?> ... plugins)`: Add description.
  - Executes `loadsBefore` behavior.
- `build()`: Add description.
  - Executes `build` behavior.

## Notes
- No additional notes.
