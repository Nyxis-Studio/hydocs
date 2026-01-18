**Source Hash:** `19134595adb77b306da1bf32ee85d4a7024b491e06fff363a5295d4742cfade2`

# CommandListPage

## Overview

## Constructor Descriptions
- `CommandListPage(@Nonnull PlayerRef playerRef)`
  - Creates a `CommandListPage` instance.
- `CommandListPage(@Nonnull PlayerRef playerRef, @Nullable String initialCommand)`
  - Creates a `CommandListPage` instance.

## Method Descriptions
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull CommandListPageEventData data)`: Add description.
  - Executes `handleDataEvent` behavior.
- `handleSendToChat(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `handleSendToChat` behavior.
- `buildCurrentCommandString()`: Add description.
  - Executes `buildCurrentCommandString` behavior.
- `buildCommandList(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `buildCommandList` behavior.
- `selectCommand(@Nonnull Ref<EntityStore> ref, @Nonnull String commandName, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `selectCommand` behavior.
- `selectSubcommand(@Nonnull Ref<EntityStore> ref, @Nonnull String subcommandName, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `selectSubcommand` behavior.
- `selectVariant(@Nonnull Ref<EntityStore> ref, int variantIndex, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `selectVariant` behavior.
- `navigateUp(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `navigateUp` behavior.
- `buildSubcommandTabs(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`: Add description.
  - Executes `buildSubcommandTabs` behavior.
- `updateTitleWithBreadcrumb(@Nonnull UICommandBuilder commandBuilder)`: Add description.
  - Executes `updateTitleWithBreadcrumb` behavior.
- `updateTitleWithVariantSuffix(@Nonnull UICommandBuilder commandBuilder)`: Add description.
  - Executes `updateTitleWithVariantSuffix` behavior.
- `buildAliasesSection(@Nonnull AbstractCommand command, @Nonnull UICommandBuilder commandBuilder)`: Add description.
  - Executes `buildAliasesSection` behavior.
- `buildPermissionSection(@Nonnull AbstractCommand command, @Nonnull UICommandBuilder commandBuilder)`: Add description.
  - Executes `buildPermissionSection` behavior.
- `buildVariantsSection(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`: Add description.
  - Executes `buildVariantsSection` behavior.
- `displayCommandInfo(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`: Add description.
  - Executes `displayCommandInfo` behavior.
- `getSimplifiedUsage(@Nonnull AbstractCommand command, @Nonnull Player playerComponent)`: Add description.
  - Executes `getSimplifiedUsage` behavior.
- `buildParametersSection(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder)`: Add description.
  - Executes `buildParametersSection` behavior.
- `buildArgumentTypesSection(@Nonnull AbstractCommand command, @Nonnull Player playerComponent, @Nonnull UICommandBuilder commandBuilder)`: Add description.
  - Executes `buildArgumentTypesSection` behavior.

## Notes
- No additional notes.
