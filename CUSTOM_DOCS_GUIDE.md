# Custom Documentation Guide

This guide explains how to write custom documentation for Hytale classes using the new format.

## Overview

The custom documentation system allows you to add meaningful descriptions to auto-generated documentation without duplicating structural information. Custom docs are stored in the `/docs/` directory and follow the same package structure as the generated docs.

## Key Principles

1. **Descriptions Only** - Custom docs contain ONLY descriptions, not structure
2. **No Duplication** - Never repeat class declarations, signatures, or structural elements
3. **Useful Content** - Focus on "why" and "when", not just "what"
4. **Structured Format** - Use specific sections that the parser understands

## File Structure

Custom documentation files should be placed in `/docs/` following the package structure:

```
docs/
└── com/
    └── hypixel/
        └── hytale/
            ├── Main.md
            └── server/
                └── core/
                    └── HytaleServer.md
```

## Template Format

Here's the complete template for custom documentation:

```markdown
## Overview
[2-3 sentence description of the class purpose and main responsibilities]

## Field Descriptions
- `FIELD_NAME_1`: [Description of what this field represents and its purpose]
- `FIELD_NAME_2`: [Another field description]

## Constructor Descriptions
- `ClassName()`: [What this no-args constructor does]
- `ClassName(ParamType param)`: [What this parameterized constructor does]

## Method Descriptions
- `methodName()`: [Useful description of what the method does and when to use it]
- `methodName(ParamType param)`: [Description for overloaded method]

## Usage Notes
[Important notes about how to use this class]
- Common usage patterns
- Important considerations
- Pitfalls to avoid
- Lifecycle information

## Examples
```java
// Practical code examples showing how to use the class
ClassName instance = new ClassName();
instance.methodName();
```
```

## Section Details

### Overview
- **Required:** Yes (highly recommended)
- **Format:** Plain text, 2-3 sentences
- **Purpose:** Provide a concise summary of the class's role
- **Example:**
  ```markdown
  ## Overview
  Central server class that manages the Hytale server lifecycle, including boot, plugin management, event bus, and shutdown procedures. Acts as the main entry point for server-side operations.
  ```

### Field Descriptions
- **Required:** No
- **Format:** Bullet list with field name in backticks
- **Purpose:** Explain what each field represents
- **Example:**
  ```markdown
  ## Field Descriptions
  - `DEFAULT_PORT`: The default port number used by the Hytale server (typically 25565).
  - `SCHEDULED_EXECUTOR`: Global scheduled executor service for async task scheduling.
  ```

### Constructor Descriptions
- **Required:** No
- **Format:** Bullet list with constructor signature in backticks
- **Purpose:** Explain what each constructor does and when to use it
- **Example:**
  ```markdown
  ## Constructor Descriptions
  - `HytaleServer()`: Creates a new HytaleServer instance. Initializes the event bus, plugin manager, and command manager.
  - `HytaleServer(HytaleServerConfig config)`: Creates a server with custom configuration. Use this when you need non-default settings.
  ```

### Method Descriptions
- **Required:** No
- **Format:** Bullet list with method signature in backticks
- **Purpose:** Explain method behavior, use cases, and important details
- **Example:**
  ```markdown
  ## Method Descriptions
  - `get()`: Returns the singleton instance of the HytaleServer. Used throughout the codebase to access server functionality.
  - `shutdownServer()`: Shuts down the server with the default shutdown reason.
  - `shutdownServer(ShutdownReason reason)`: Shuts down the server with a specific reason. Triggers shutdown events and cleanup procedures.
  ```

### Usage Notes
- **Required:** No
- **Format:** Markdown text (paragraphs, lists, etc.)
- **Purpose:** Provide important usage information
- **Example:**
  ```markdown
  ## Usage Notes
  - Always use `HytaleServer.get()` to access the server instance.
  - Shutdown should be triggered through `shutdownServer()` methods, not by killing the process.
  - The server follows a strict lifecycle: boot → setup → start → running → stop → shutdown.
  - Do not call initialization methods directly - they are managed by the server lifecycle.
  ```

### Examples
- **Required:** No
- **Format:** Java code block
- **Purpose:** Show practical usage examples
- **Example:**
  ```markdown
  ## Examples
  ```java
  // Get the server instance
  HytaleServer server = HytaleServer.get();

  // Graceful shutdown
  server.shutdownServer(ShutdownReason.SHUTDOWN);

  // Check server state
  if (server.isBooting()) {
      // Server is still booting
  }
  ```
  ```

## Best Practices

### ✅ DO

- **Be specific and useful**
  ```markdown
  - `save()`: Persists all world data to disk, including chunks, entities, and player data. This is a blocking operation that may take several seconds for large worlds.
  ```

- **Explain when and why to use something**
  ```markdown
  - `validate(ValidationOption... options)`: Validates world integrity with specific options. Use this after world generation or when corruption is suspected.
  ```

- **Mention important side effects**
  ```markdown
  - `reload()`: Reloads all configuration files and reinitializes plugins. Warning: This will disconnect all players.
  ```

- **Document relationships and dependencies**
  ```markdown
  ## Usage Notes
  - This class must be initialized before PluginManager
  - Always call cleanup() in a finally block
  - Depends on EventBus being available
  ```

### ❌ DON'T

- **Use generic, uninformative descriptions**
  ```markdown
  - `save()`: Executes save behavior.  ❌
  ```

- **Repeat the method signature**
  ```markdown
  - `setName(String name)`: Sets the name to the provided name parameter.  ❌
  ```

- **Duplicate structural information**
  ```markdown
  ## Methods  ❌
  ### save()
  - Returns: void
  - Parameters: none
  ```

- **Include implementation details**
  ```markdown
  - `calculate()`: First initializes array with size 10, then iterates using for loop...  ❌
  ```

## Real Examples

### Example 1: Main.md

```markdown
## Overview
Entry point class for the Hytale server. Handles JVM initialization and sets up the transforming class loader for runtime bytecode modification.

## Method Descriptions
- `main(String[] args)`: Main entry point for the Hytale server JVM. Initializes the transforming class loader and delegates to the actual server bootstrap.
- `launchWithTransformingClassLoader(@Nonnull String[] args)`: Sets up the transforming class loader environment and launches the server with runtime class transformation capabilities.
- `getClasspathUrls()`: Retrieves all classpath URLs for dynamic class loading and transformation.

## Usage Notes
- This class should not be instantiated directly - it serves as the JVM entry point
- The transforming class loader is essential for server plugins and runtime modifications
- Always launch the server through this main class to ensure proper initialization
```

### Example 2: HytaleServer.md (hypothetical)

```markdown
## Overview
Central server class that manages the Hytale server lifecycle, including boot, plugin management, event bus, and shutdown procedures. Acts as the main entry point for server-side operations.

## Field Descriptions
- `DEFAULT_PORT`: The default port number used by the Hytale server (typically 25565).
- `SCHEDULED_EXECUTOR`: Global scheduled executor service for async task scheduling.

## Constructor Descriptions
- `HytaleServer()`: Creates a new HytaleServer instance. Initializes the event bus, plugin manager, and command manager.

## Method Descriptions
- `get()`: Returns the singleton instance of the HytaleServer. Used throughout the codebase to access server functionality.
- `shutdownServer()`: Shuts down the server with the default shutdown reason.
- `shutdownServer(ShutdownReason reason)`: Shuts down the server with a specific reason. Triggers shutdown events and cleanup procedures.
- `doneSetup(PluginBase plugin)`: Called when a plugin completes its setup phase. Used internally by the plugin loading system.
- `reportSaveProgress(World world, int saved, int total)`: Reports world save progress, typically used for displaying save status in singleplayer mode.

## Usage Notes
- Always use `HytaleServer.get()` to access the server instance.
- Shutdown should be triggered through `shutdownServer()` methods, not by killing the process.
- The server follows a strict lifecycle: boot → setup → start → running → stop → shutdown.

## Examples
```java
// Get server instance
HytaleServer server = HytaleServer.get();

// Graceful shutdown
server.shutdownServer(ShutdownReason.SHUTDOWN);

// Register shutdown hook
Runtime.getRuntime().addShutdownHook(new Thread(() -> {
    server.shutdownServer(ShutdownReason.SIGINT);
}));
```
```

## How Descriptions Are Merged

When generating documentation, the system:

1. Parses your custom docs file
2. Extracts each section (overview, field descriptions, etc.)
3. Merges them inline into the auto-generated structure:
   - **Overview** replaces the generic placeholder
   - **Field descriptions** are added as `- **Description:** ...` under each field
   - **Method descriptions** are added as `**Description:** ...` under each method
   - **Usage Notes** and **Examples** become their own sections at the end

## Lookup Keys

The system uses specific keys to match descriptions:

- **Fields:** Exact field name (e.g., `DEFAULT_PORT`)
- **Constructors:** Full signature (e.g., `HytaleServer(HytaleServerConfig config)`)
- **Methods:** Full signature (e.g., `shutdownServer(ShutdownReason reason)`)

**Important:** Make sure your signatures match exactly, including parameter types.

## Workflow

1. **Generate docs** without custom descriptions first:
   ```bash
   python3 hydocs.py --only-docs
   ```

2. **Identify classes** that need better descriptions

3. **Create custom docs** file in `/docs/` matching the package structure

4. **Add descriptions** using the template format

5. **Regenerate docs** to see merged output:
   ```bash
   python3 hydocs.py --only-docs
   ```

6. **Verify** the output in `/build/`

## Tips

- Start with high-level, frequently-used classes
- Focus on public APIs that developers will use
- Don't document every private implementation detail
- Keep descriptions concise but informative
- Use the `## Examples` section to show common use cases
- Update custom docs when the API changes

## Validation

After adding custom docs, verify:

- [ ] Overview appears in generated file
- [ ] Method descriptions are merged correctly
- [ ] No structural duplication
- [ ] Descriptions are useful and specific
- [ ] Code examples are syntactically correct

## Questions?

If you're unsure whether something belongs in custom docs:

- **Does it explain "why" or "when"?** → Include it
- **Does it repeat structural information?** → Exclude it
- **Is it useful for someone using this class?** → Include it
- **Is it an implementation detail?** → Exclude it
