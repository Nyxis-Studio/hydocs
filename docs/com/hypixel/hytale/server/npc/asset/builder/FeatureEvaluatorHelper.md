# FeatureEvaluatorHelper

## Overview
- Documentation for `FeatureEvaluatorHelper`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder`.

## Constructors
- `FeatureEvaluatorHelper()`
  - Creates a `FeatureEvaluatorHelper` instance.
- `FeatureEvaluatorHelper(boolean couldRequireFeature)`
  - Creates a `FeatureEvaluatorHelper` instance.

## Methods
- `isDisallowParameterProviders()`
  - Executes `isDisallowParameterProviders` behavior.
- `add(ProviderEvaluator evaluator)`
  - Executes `add` behavior.
- `canAddProvider()`
  - Executes `canAddProvider` behavior.
- `lock()`
  - Executes `lock` behavior.
- `setContainsReference()`
  - Executes `setContainsReference` behavior.
- `addProviderReferenceValidator(BiConsumer<BuilderManager, ExecutionContext> referenceValidator)`
  - Executes `addProviderReferenceValidator` behavior.
- `addComponentRequirementValidator(BiConsumer<FeatureEvaluatorHelper, ExecutionContext> validator)`
  - Executes `addComponentRequirementValidator` behavior.
- `getProviders()`
  - Executes `getProviders` behavior.
- `requiresProviderReferenceEvaluation()`
  - Executes `requiresProviderReferenceEvaluation` behavior.
- `belongsToFeatureRequiringComponent()`
  - Executes `belongsToFeatureRequiringComponent` behavior.
- `validateProviderReferences(BuilderManager manager, ExecutionContext context)`
  - Executes `validateProviderReferences` behavior.
- `validateComponentRequirements(FeatureEvaluatorHelper providers, ExecutionContext context)`
  - Executes `validateComponentRequirements` behavior.
- `disallowParameterProviders()`
  - Executes `disallowParameterProviders` behavior.

## Notes
- No additional notes.
