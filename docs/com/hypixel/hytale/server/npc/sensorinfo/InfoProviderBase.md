# InfoProviderBase

## Overview
- Documentation for `InfoProviderBase`.
- Declared as a class in `com.hypixel.hytale.server.npc.sensorinfo`.

## Constructors
- `InfoProviderBase()`
  - Creates a `InfoProviderBase` instance.
- `InfoProviderBase(ParameterProvider parameterProvider)`
  - Creates a `InfoProviderBase` instance.
- `InfoProviderBase(ParameterProvider parameterProvider, ExtraInfoProvider ... providers)`
  - Creates a `InfoProviderBase` instance.

## Methods
- `getParameterProvider(int parameter)`
  - Executes `getParameterProvider` behavior.
- `getExtraInfo(Class<E> clazz)`
  - Executes `getExtraInfo` behavior.
- `passExtraInfo(E provider)`
  - Executes `passExtraInfo` behavior.
- `getPassedExtraInfo(Class<E> clazz)`
  - Executes `getPassedExtraInfo` behavior.

## Notes
- No additional notes.
