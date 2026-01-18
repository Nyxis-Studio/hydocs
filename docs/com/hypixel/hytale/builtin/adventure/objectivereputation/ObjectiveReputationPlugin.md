**Source Hash:** `ba0cbf7fdf7eced18d44411a6eaa18018c79d0a63cadc4715e6889f400765760`
**Last Updated:** 2026-01-18T19:03:47-03:00

# ObjectiveReputationPlugin

## Overview
Plugin that integrates the objective system with reputation mechanics, allowing objectives to reward or penalize player reputation with various groups. This plugin registers reputation-based completion handlers and ensures proper initialization order between objectives and reputation systems.

## Field Descriptions
- `instance`: Static singleton instance of the plugin for global access. Used by other systems that need to interact with objective reputation functionality.

## Constructor Descriptions
- `ObjectiveReputationPlugin(@Nonnull JavaPluginInit init)`: Creates a new plugin instance with the provided initialization context. Standard JavaPlugin constructor pattern.

## Method Descriptions
- `get()`: Returns the singleton plugin instance for global access. Used by other systems to interact with objective reputation functionality.
- `setup()`: Initializes the objective reputation integration system. Registers reputation completion types, history data codecs, and ensures ObjectiveAssets load after ReputationGroups for proper dependency resolution.

## Usage Notes
- This plugin acts as a bridge between the objective and reputation systems
- Reputation completion handlers are automatically executed when objectives are completed
- Asset loading order is important - reputation groups must be loaded before objectives that reference them
- The plugin registers both completion handlers and history data tracking for reputation rewards

## Examples
```java
// Access the plugin instance
ObjectiveReputationPlugin plugin = ObjectiveReputationPlugin.get();

// Reputation completions are registered automatically:
// "Reputation" completion type with ReputationCompletionAsset
// ReputationCompletion handler for processing reputation changes
```
