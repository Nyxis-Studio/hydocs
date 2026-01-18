# Example Custom Documentation Template

This file serves as a complete reference example for creating custom documentation.
Use this as a template when writing custom docs for Hytale classes.

---

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
- `doneSetup(PluginBase plugin)`: Called internally by the plugin loader when a plugin completes its setup phase. Increments the setup counter and checks if all plugins are ready to transition to the start phase. Should not be called directly by plugin code.
- `doneStart(PluginBase plugin)`: Called internally when a plugin completes its start phase. Tracks plugin initialization progress and logs any plugins that fail to start within the timeout period.
- `doneStop(PluginBase plugin)`: Called internally when a plugin completes its stop phase during shutdown. Ensures all plugins have a chance to cleanup before final server termination.
- `getPluginManager()`: Returns the plugin manager instance responsible for loading, enabling, and managing server plugins. Use this to register event listeners, access other plugins, or query plugin metadata.
- `getEventBus()`: Returns the central event bus for subscribing to and publishing server events. All game events flow through this bus, making it the primary mechanism for inter-plugin communication.
- `getCommandManager()`: Returns the command manager for registering and executing server commands. Use this to add custom commands, handle command execution, or implement tab completion.
- `getWorldManager()`: Returns the world manager responsible for loading, unloading, and managing game worlds. Provides access to all loaded worlds and handles world generation.
- `reportSaveProgress(World world, int saved, int total)`: Reports world save progress for UI updates. Typically used in singleplayer mode to display save progress to the client. The saved parameter indicates chunks saved so far, total is the total number of chunks to save.
- `sendSingleplayerProgress()`: Sends current server initialization progress to the singleplayer client. Used to update the loading screen during world startup.
- `getServerName()`: Returns the configured server name displayed in the multiplayer server list and MOTD (Message of the Day).
- `isBooting()`: Returns true if the server is currently in the boot phase (before accepting connections). Use this to defer operations that require a fully initialized server.
- `isRunning()`: Returns true if the server is running and accepting connections. Safe to perform game operations when this returns true.
- `isStopping()`: Returns true if the server is in the shutdown sequence. Use this to skip non-critical operations during shutdown.
- `getTPS()`: Returns the current server tick rate (ticks per second). A healthy server maintains close to SERVER_TICK_RATE. Values significantly below target indicate server lag.
- `getTickTime()`: Returns the average time taken to process a single server tick, in milliseconds. Useful for performance monitoring and lag diagnosis.

## Usage Notes

- **Always use `HytaleServer.get()` to access the server instance** - Never store your own reference as the instance may change during restarts or tests.
- **Shutdown should be triggered through `shutdownServer()` methods** - Never call `System.exit()` or kill the process directly, as this prevents proper cleanup and can cause data corruption.
- **The server follows a strict lifecycle**: boot → setup → start → running → stop → shutdown. Each phase has specific guarantees about system availability.
- **Plugin initialization happens in phases**: All plugins complete setup before any start, ensuring dependencies are initialized in the correct order.
- **Event handling is asynchronous by default** - Use synchronous event handlers sparingly as they can block the main server thread.
- **World saves are automatic** - The server periodically saves world data. Manual saves are only necessary before critical operations.
- **The server is not thread-safe** - Most operations must be performed on the main server thread. Use `getScheduledExecutor()` to schedule work on the main thread.

## Examples

```java
// Getting the server instance
HytaleServer server = HytaleServer.get();

// Graceful shutdown with reason
server.shutdownServer(ShutdownReason.SHUTDOWN);

// Check server state before performing operations
if (server.isRunning()) {
    // Safe to perform game operations
    WorldManager worlds = server.getWorldManager();
    World overworld = worlds.getWorld("overworld");
}

// Register shutdown hook for SIGINT (Ctrl+C)
Runtime.getRuntime().addShutdownHook(new Thread(() -> {
    HytaleServer.get().shutdownServer(ShutdownReason.SIGINT);
}));

// Monitor server performance
HytaleServer server = HytaleServer.get();
double tps = server.getTPS();
if (tps < 15.0) {
    logger.warn("Server is lagging! TPS: " + tps);
}

// Access managers
PluginManager plugins = server.getPluginManager();
EventBus events = server.getEventBus();
CommandManager commands = server.getCommandManager();

// Register an event listener
events.subscribe(ServerStartedEvent.class, event -> {
    logger.info("Server has fully started!");
});

// Execute code on main thread
server.getScheduledExecutor().execute(() -> {
    // This runs on the main server thread
    // Safe to modify game state here
});

// Custom server startup with configuration
HytaleServerConfig config = new HytaleServerConfig();
config.setPort(25566);
config.setMaxPlayers(100);
config.setMotd("Custom Hytale Server");

HytaleServer server = new HytaleServer(config);
server.start(); // Blocking call
```

---

## Guidelines for This Template

### What Makes Good Documentation

**✅ DO:**
- Explain the "why" and "when", not just the "what"
- Mention side effects and important behaviors
- Include performance considerations
- Document thread safety requirements
- Show real-world usage examples
- Explain relationships with other components
- Note common pitfalls and how to avoid them
- Specify pre-conditions and post-conditions

**❌ DON'T:**
- Repeat method signatures (already auto-generated)
- Use generic descriptions like "Executes X behavior"
- Include implementation details that could change
- Duplicate structural information (class name, type, etc.)
- Write overly verbose descriptions
- Include deprecated or experimental features without noting them

### Section Guidelines

#### Overview
- **Length:** 2-4 sentences
- **Focus:** High-level purpose and primary responsibilities
- **Format:** Prose, not bullet points
- **Example:** "Central server class that manages the Hytale server lifecycle..."

#### Field Descriptions
- **Format:** `- FIELD_NAME: Description`
- **Focus:** What the field represents and why it exists
- **Include:** Default values, valid ranges, usage context
- **Example:** `- DEFAULT_PORT: The default network port used by the Hytale server for client connections (typically 25565 for compatibility with Minecraft protocol).`

#### Constructor Descriptions
- **Format:** `- Constructor(ParamType param): Description`
- **Focus:** When to use each constructor, what it initializes
- **Include:** Difference between overloaded constructors
- **Example:** `- HytaleServer(HytaleServerConfig config): Creates a server instance with custom configuration. Use this constructor when you need to override default settings...`

#### Method Descriptions
- **Format:** `- methodName(ParamType param): Description`
- **Focus:** What the method does, when to call it, what it returns
- **Include:** Side effects, exceptions, thread safety, performance notes
- **Example:** `- shutdownServer(ShutdownReason reason): Shuts down the server with a specific reason code. The reason is logged and can be used by monitoring systems...`

#### Usage Notes
- **Format:** Markdown paragraphs and lists
- **Focus:** Important patterns, gotchas, lifecycle information
- **Include:** Common mistakes, best practices, integration tips
- **Structure:** Use bullet points for specific items, paragraphs for explanations

#### Examples
- **Format:** Java code blocks with comments
- **Focus:** Common use cases, complete working code
- **Include:** Multiple scenarios showing different features
- **Style:** Real-world examples, not trivial toy code

### Quality Checklist

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

### Common Patterns

**For Manager Classes:**
```markdown
## Overview
Manages [what] by providing [functionality]. Responsible for [lifecycle/coordination].

## Method Descriptions
- `get[Resource]()`: Returns [resource]. Thread-safe singleton access.
- `register[Thing]()`: Registers [thing] with [system]. Must be called during [phase].
```

**For Event Classes:**
```markdown
## Overview
Fired when [condition]. Allows plugins to [react/modify/cancel] [behavior].

## Method Descriptions
- `isCancelled()`: Returns true if this event has been cancelled by a handler.
- `setCancelled(boolean)`: Cancels this event, preventing [default behavior].
```

**For Configuration Classes:**
```markdown
## Overview
Configuration container for [system]. Loaded from [source] and applied during [phase].

## Field Descriptions
- `[option]`: [What it controls]. Default: [value]. Valid values: [range/options].
```

**For Utility Classes:**
```markdown
## Overview
Utility class providing [category] operations. All methods are static and thread-safe.

## Method Descriptions
- `[operation]()`: [What it does]. Useful for [use case]. Time complexity: O([complexity]).
```

---

## Quick Reference

**Minimum Viable Documentation:**
```markdown
## Overview
[2-3 sentences about the class]

## Method Descriptions
- `methodName()`: [What it does and when to use it]
```

**Complete Documentation:**
```markdown
## Overview
[Detailed class description]

## Field Descriptions
- `FIELD`: [Description with context]

## Constructor Descriptions
- `Constructor(params)`: [What it initializes]

## Method Descriptions
- `method(params)`: [Detailed behavior and usage]

## Usage Notes
- [Important patterns]
- [Common pitfalls]
- [Integration tips]

## Examples
[Multiple real-world code examples]
```

---

## When to Write Custom Docs

**High Priority:**
- Public APIs used by plugins
- Core manager classes
- Common utility classes
- Complex lifecycle classes
- Configuration classes

**Medium Priority:**
- Event classes
- Data structures
- Service providers
- Factory classes

**Low Priority:**
- Internal implementation classes
- Private helper classes
- Auto-generated classes
- Deprecated classes

Focus on documenting classes that developers will actually use!
