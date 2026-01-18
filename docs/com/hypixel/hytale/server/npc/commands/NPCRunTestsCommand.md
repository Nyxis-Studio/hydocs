# NPCRunTestsCommand

## Overview
- Documentation for `NPCRunTestsCommand`.
- Declared as a class in `com.hypixel.hytale.server.npc.commands`.

## Constructors
- `NPCRunTestsCommand()`
  - Creates a `NPCRunTestsCommand` instance.

## Methods
- `execute(@Nonnull CommandContext context, @Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull PlayerRef playerRef, @Nonnull World world)`
  - Executes `execute` behavior.
- `setNextRole(@Nonnull NPCTestData testData, @Nonnull Ref<EntityStore> reference, @Nonnull Store<EntityStore> store, @Nonnull World world)`
  - Executes `setNextRole` behavior.
- `cleanupNPC(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `cleanupNPC` behavior.
- `spawnNPC(@Nonnull Ref<EntityStore> playerReference, @Nonnull NPCTestData testData, int index, @Nonnull Vector3d position, @Nullable Vector3f rotation, @Nonnull Store<EntityStore> store)`
  - Executes `spawnNPC` behavior.
- `reportResults(@Nonnull Ref<EntityStore> playerReference, @Nonnull NPCTestData testData, @Nonnull Store<EntityStore> store)`
  - Executes `reportResults` behavior.
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
