# BuilderModifier

## Overview
- Documentation for `BuilderModifier`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder`.

## Constructors
- `BuilderModifier(Object2ObjectMap<String, ExpressionHolder> builderExpressionMap, StatePair[] exportedStateIndexes, StateMappingHelper stateHelper, String combatConfig, Map<String, String> interactionVars)`
  - Creates a `BuilderModifier` instance.
- `BuilderModifier(map, (StatePair[])`
  - Creates a `BuilderModifier` instance.

## Methods
- `getCombatConfig()`
  - Executes `getCombatConfig` behavior.
- `getInteractionVars()`
  - Executes `getInteractionVars` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `exportedStateCount()`
  - Executes `exportedStateCount` behavior.
- `applyComponentStateMap(@Nonnull BuilderSupport support)`
  - Executes `applyComponentStateMap` behavior.
- `popComponentStateMap(@Nonnull BuilderSupport support)`
  - Executes `popComponentStateMap` behavior.
- `createScope(@Nonnull BuilderSupport builderSupport, @Nonnull BuilderParameters builderParameters, Scope globalScope)`
  - Executes `createScope` behavior.
- `createScope(ExecutionContext executionContext, @Nonnull BuilderParameters builderParameters, @Nullable Scope globalScope)`
  - Executes `createScope` behavior.
- `fromJSON(@Nonnull JsonObject jsonObject, @Nonnull BuilderParameters builderParameters, @Nonnull StateMappingHelper helper, @Nonnull ExtraInfo extraInfo)`
  - Executes `fromJSON` behavior.
- `readModifierObject(@Nonnull JsonObject jsonObject, @Nonnull BuilderParameters builderParameters, @Nonnull StringHolder holder, @Nonnull Consumer<StringHolder> referenceConsumer, @Nonnull Consumer<BuilderModifier> builderModifierConsumer, @Nonnull StateMappingHelper helper, @Nonnull ExtraInfo extraInfo)`
  - Executes `readModifierObject` behavior.
- `toSchema(@Nonnull SchemaContext context)`
  - Executes `toSchema` behavior.
- `hasInterfaceMappedExpression(String interfaceKey)`
  - Executes `hasInterfaceMappedExpression` behavior.
- `addInterfaceMappedExpression(String interfaceKey, BuilderExpression expression)`
  - Executes `addInterfaceMappedExpression` behavior.
- `getExpression(@Nullable String interfaceKey)`
  - Executes `getExpression` behavior.
- `getSchemaName()`
  - Executes `getSchemaName` behavior.

## Notes
- No additional notes.
