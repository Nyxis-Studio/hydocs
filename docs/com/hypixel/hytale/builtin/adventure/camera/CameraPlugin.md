**Source Hash:** `0e2b975517272a087988249c1560bf85d900a60c74602e04e7f579939afb5397`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# CameraPlugin

## Overview
Registers camera-related assets, codecs, commands, and systems. Bootstraps camera shake and view bobbing assets for the server.

## Field Descriptions
- `CODEC_CAMERA_SHAKE`: Codec name used when registering camera shake codecs.

## Constructor Descriptions
- `CameraPlugin(JavaPluginInit init)`: Initializes the plugin with the provided plugin context.

## Method Descriptions
- `setup()`: Registers camera shake and interaction codecs, camera shake/view bobbing asset stores, the command, and the camera effect system.

## Usage Notes
- Registers `CameraShake` and `ViewBobbing` asset stores with packet generators.

## Examples
```java
new CameraPlugin(init);
```
