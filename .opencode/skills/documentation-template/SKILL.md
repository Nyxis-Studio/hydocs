---
name: documentation-template
description: Provides the standard custom documentation template and guidance for Hydocs
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: documentation
---

## What I Do

Provide the standard custom documentation template and guidance. Use this skill whenever you create or update documentation in `docs/`.

## Template Format

Use this structure for all custom docs:

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

## Quality Checklist

Before submitting custom documentation, verify:

- [ ] Overview is concise and informative (not generic)
- [ ] All public fields have meaningful descriptions
- [ ] Constructor differences are clearly explained
- [ ] Method descriptions explain behavior, not just signature
- [ ] Side effects and important behaviors are documented
- [ ] Usage notes cover common patterns and pitfalls
- [ ] Examples are complete and runnable
- [ ] No duplication of auto-generated content
- [ ] Thread safety is mentioned where relevant
- [ ] Performance implications are noted where significant

## Example Output

## Overview
Central server class that manages the Hytale server lifecycle, including boot sequence, plugin management, event bus coordination, and graceful shutdown procedures. Acts as the main entry point for all server-side operations and maintains the singleton server instance accessible throughout the codebase.

## Field Descriptions
- `DEFAULT_PORT`: The default network port used by the Hytale server for client connections (typically 25565 for compatibility with Minecraft protocol).
- `SCHEDULED_EXECUTOR`: Global scheduled executor service used for asynchronous task scheduling and periodic operations. Shared across all server components for efficient thread pool management.
- `SERVER_TICK_RATE`: Target number of game ticks per second (TPS). The server attempts to maintain this rate for consistent game simulation.
- `MAX_PLAYERS`: Maximum number of concurrent players allowed on the server. Can be configured through server properties.
- `PROTOCOL_VERSION`: Current network protocol version used for client-server communication. Used for version compatibility checks.

## Constructor Descriptions
- `HytaleServer()`: Creates a new HytaleServer instance with default configuration. Initializes the event bus, plugin manager, command registry, and all core subsystems. This is the primary constructor used during normal server startup.
- `HytaleServer(HytaleServerConfig config)`: Creates a server instance with custom configuration. Use this constructor when you need to override default settings such as port, max players, or resource pack URLs. Useful for testing scenarios or specialized server setups.

## Method Descriptions
- `get()`: Returns the singleton instance of the HytaleServer. This is the standard way to access the server instance from anywhere in the codebase. Thread-safe and guaranteed to return a non-null instance after server initialization.
- `start()`: Initiates the server startup sequence. Loads plugins, initializes worlds, binds network listeners, and begins accepting client connections. This is a blocking operation that runs the main server loop.
- `stop()`: Initiates graceful server shutdown. Disconnects all players with a shutdown message, saves all world data, unloads plugins in reverse order, and closes network connections. Blocks until shutdown is complete.
- `shutdownServer()`: Convenience method that calls stop() with a default shutdown reason. Equivalent to shutdownServer(ShutdownReason.SHUTDOWN).
- `shutdownServer(ShutdownReason reason)`: Shuts down the server with a specific reason code. The reason is logged and can be used by monitoring systems to distinguish between normal shutdowns, crashes, and other termination causes. Triggers ServerShutdownEvent before beginning shutdown sequence.

## Usage Notes
- Always use `HytaleServer.get()` to access the server instance. Never store your own reference.
- Shutdown should be triggered through `shutdownServer()` methods. Do not call `System.exit()`.
- The server follows a strict lifecycle: boot -> setup -> start -> running -> stop -> shutdown.
- Event handling is asynchronous by default. Use synchronous handlers sparingly.
- The server is not thread-safe. Perform operations on the main server thread.

## Examples
```java
// Getting the server instance
HytaleServer server = HytaleServer.get();

// Graceful shutdown with reason
server.shutdownServer(ShutdownReason.SHUTDOWN);

// Check server state before performing operations
if (server.isRunning()) {
    WorldManager worlds = server.getWorldManager();
    World overworld = worlds.getWorld("overworld");
}
```
