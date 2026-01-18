# CommandListPage

## Overview
- Documentation for `CommandListPage`.
- Declared as a class in `com.hypixel.hytale.server.core.command.system.pages`.

## Constructors
- `CommandListPage(@Nonnull PlayerRef playerRef)`
  - Creates a `CommandListPage` instance.
- `CommandListPage(@Nonnull PlayerRef playerRef, @Nullable String initialCommand)`
  - Creates a `CommandListPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull CommandListPageEventData data)`
  - Executes `handleDataEvent` behavior.
- `handleSendToChat(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `handleSendToChat` behavior.
- `buildCurrentCommandString()`
  - Executes `buildCurrentCommandString` behavior.
- `buildCommandList(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `buildCommandList` behavior.
- `selectCommand(@Nonnull Ref<EntityStore> ref, @Nonnull String commandName, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `selectCommand` behavior.
- `selectSubcommand(@Nonnull Ref<EntityStore> ref, @Nonnull String subcommandName, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `selectSubcommand` behavior.
- `selectVariant(@Nonnull Ref<EntityStore> ref, int variantIndex, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `selectVariant` behavior.
- `navigateUp(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `navigateUp` behavior.
- `buildSubcommandTabs(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildSubcommandTabs` behavior.
- `updateTitleWithBreadcrumb(@Nonnull UICommandBuilder commandBuilder)`
  - Executes `updateTitleWithBreadcrumb` behavior.
- `updateTitleWithVariantSuffix(@Nonnull UICommandBuilder commandBuilder)`
  - Executes `updateTitleWithVariantSuffix` behavior.
- `buildAliasesSection(@Nonnull AbstractCommand command, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `buildAliasesSection` behavior.
- `buildPermissionSection(@Nonnull AbstractCommand command, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `buildPermissionSection` behavior.
- `buildVariantsSection(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildVariantsSection` behavior.
- `displayCommandInfo(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `displayCommandInfo` behavior.
- `getSimplifiedUsage(@Nonnull AbstractCommand command, @Nonnull Player playerComponent)`
  - Executes `getSimplifiedUsage` behavior.
- `buildParametersSection(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `buildParametersSection` behavior.
- `buildArgumentTypesSection(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `buildArgumentTypesSection` behavior.

## Notes
- No additional notes.
