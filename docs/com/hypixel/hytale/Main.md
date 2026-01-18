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
