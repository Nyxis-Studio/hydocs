# SubTypeTypeAdapterFactory

## Overview
- Documentation for `SubTypeTypeAdapterFactory`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `SubTypeTypeAdapterFactory(Class<?> baseClassType, String typeFieldName)`
  - Creates a `SubTypeTypeAdapterFactory` instance.
- `SubTypeTypeAdapterFactory(baseClass, typeFieldName)`
  - Creates a `SubTypeTypeAdapterFactory` instance.

## Methods
- `of(Class<?> baseClass, String typeFieldName)`
  - Executes `of` behavior.
- `registerSubType(Class<?> clazz, String name)`
  - Executes `registerSubType` behavior.
- `create(@Nonnull Gson gson, @Nonnull TypeToken<T> type)`
  - Executes `create` behavior.
- `write(JsonWriter out, @Nonnull T value)`
  - Executes `write` behavior.
- `read(JsonReader in)`
  - Executes `read` behavior.

## Notes
- No additional notes.
