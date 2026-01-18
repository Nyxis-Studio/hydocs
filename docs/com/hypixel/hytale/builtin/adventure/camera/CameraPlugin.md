# CameraPlugin

**Overview**
Registers camera-related assets, codecs, commands, and systems.
Bootstraps camera shake and view bobbing assets for the server.

**Constructors**
- `CameraPlugin(JavaPluginInit init)`: initializes the plugin.

**Methods**
- `setup()`: registers codecs, asset stores, commands, and systems.

**Notes**
- Registers `CameraShake` and `ViewBobbing` stores with packet generators.
- Adds `CameraEffectCommand` and `CameraEffectSystem` during setup.
