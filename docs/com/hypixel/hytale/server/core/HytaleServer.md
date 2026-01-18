**Source Hash:** `b97569b8e34516304d571447bf0b49da09c90655af153217612440d4b1400be3`
**Last Updated:** `2026-01-18T16:58:46-03:00`

## Overview
Singleton server runtime coordinator that owns boot, plugin setup, and shutdown orchestration for the Hytale server process. Loads configuration and authentication, initializes core subsystems (Netty, assets, metrics), and drives plugin lifecycle phases before signaling universe readiness. Provides access to core managers and exposes boot/shutdown state for consumers.

## Field Descriptions
- `DEFAULT_PORT`: Default TCP port (5520) used when binding listeners.
- `SCHEDULED_EXECUTOR`: Single-thread scheduler used for periodic tasks like config persistence and delayed forced shutdown.
- `METRICS_REGISTRY`: Registry exporting boot timestamps, boot/shutdown state, plugin manager metrics, config snapshots, and JVM metrics.

## Constructor Descriptions
- `HytaleServer()`: Instantiates the singleton server, configures logging and options, initializes auth/Sentry/Netty/asset loaders, registers core plugins and GC hooks, then executes the full boot sequence with setup, asset validation, plugin start, and universe readiness checks.

## Method Descriptions
- `doneSetup(PluginBase)`: Increments setup phase progress and emits singleplayer progress updates.
- `doneStart(PluginBase)`: Increments start phase progress and emits singleplayer progress updates.
- `doneStop(PluginBase)`: Decrements progress during shutdown and emits singleplayer progress updates.
- `get()`: Returns the singleton server instance created during construction.
- `getBoot()`: Returns the Instant captured at the start of server construction.
- `getBootStart()`: Returns the boot start timestamp in nanoseconds for timing calculations.
- `getCommandManager()`: Returns the command manager used for command registration and execution.
- `getConfig()`: Returns the loaded server configuration instance.
- `getEventBus()`: Returns the event bus used to dispatch lifecycle events.
- `getPluginManager()`: Returns the plugin manager that coordinates plugin setup, start, and shutdown phases.
- `getServerName()`: Returns the configured server name.
- `getShutdownReason()`: Returns the shutdown reason if shutdown has been triggered.
- `isBooted()`: Indicates whether boot completed and listeners are bound.
- `isBooting()`: Indicates whether the boot sequence is currently running.
- `isShuttingDown()`: Indicates whether shutdown has been initiated.
- `reportSaveProgress(World, int, int)`: Reports chunk save progress during shutdown, emitting singleplayer UI signals or periodic log updates in multiplayer.
- `reportSingleplayerStatus(String)`: Emits a singleplayer status message for UI display.
- `sendSingleplayerProgress()`: Emits singleplayer progress signals based on plugin manager state and shutdown progress.
- `shutdownServer()`: Initiates a graceful shutdown using the default shutdown reason.
- `shutdownServer(ShutdownReason)`: Sets the shutdown reason, emits singleplayer status if provided, and starts the shutdown thread.

## Usage Notes
- Use `get()` for global access; the constructor is invoked once during boot.
- Boot performs setup, asset validation, plugin startup, and waits for universe readiness before dispatching `BootEvent`.
- Shutdown dispatches `ShutdownEvent`, shuts down plugins and commands, saves config changes, then forces halt after a delay.
- Singleplayer progress/status messages are only emitted when `Constants.SINGLEPLAYER` is enabled.

## Examples
```java
HytaleServer server = HytaleServer.get();

if (server.isBooted()) {
    server.reportSingleplayerStatus("Server ready");
}

server.shutdownServer(ShutdownReason.SHUTDOWN);
```
