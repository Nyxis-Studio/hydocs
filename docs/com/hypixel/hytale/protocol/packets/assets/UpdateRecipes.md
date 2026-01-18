# UpdateRecipes

## Overview
- Documentation for `UpdateRecipes`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.assets`.

## Constructors
- `UpdateRecipes()`
  - Creates a `UpdateRecipes` instance.
- `UpdateRecipes(@Nonnull UpdateType type, @Nullable Map<String, CraftingRecipe> recipes, @Nullable String[] removedRecipes)`
  - Creates a `UpdateRecipes` instance.
- `UpdateRecipes(@Nonnull UpdateRecipes other)`
  - Creates a `UpdateRecipes` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
