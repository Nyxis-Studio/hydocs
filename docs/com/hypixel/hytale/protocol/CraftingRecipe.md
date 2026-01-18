# CraftingRecipe

## Overview
- Documentation for `CraftingRecipe`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `CraftingRecipe()`
  - Creates a `CraftingRecipe` instance.
- `CraftingRecipe(@Nullable String id, @Nullable MaterialQuantity[] inputs, @Nullable MaterialQuantity[] outputs, @Nullable MaterialQuantity primaryOutput, @Nullable BenchRequirement[] benchRequirement, boolean knowledgeRequired, float timeSeconds, int requiredMemoriesLevel)`
  - Creates a `CraftingRecipe` instance.
- `CraftingRecipe(@Nonnull CraftingRecipe other)`
  - Creates a `CraftingRecipe` instance.

## Methods
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
