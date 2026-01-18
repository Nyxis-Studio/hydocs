# Evaluator

## Overview
- Documentation for `Evaluator`.
- Declared as a class in `com.hypixel.hytale.server.npc.decisionmaker.core`.

## Constructors
- None.

## Methods
- `initialise()`
  - Executes `initialise` behavior.
- `setupNPC(Role role)`
  - Executes `setupNPC` behavior.
- `setupNPC(Holder<EntityStore> holder)`
  - Executes `setupNPC` behavior.
- `evaluate(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, CommandBuffer<EntityStore> commandBuffer, @Nonnull EvaluationContext context)`
  - Executes `evaluate` behavior.
- `getWeight()`
  - Executes `getWeight` behavior.
- `getWeightCoefficient()`
  - Executes `getWeightCoefficient` behavior.
- `getOption()`
  - Executes `getOption` behavior.
- `getTotalUtility(double threshold)`
  - Executes `getTotalUtility` behavior.
- `tryPick(double currentWeight, double threshold)`
  - Executes `tryPick` behavior.
- `calculateUtility(int var1, ArchetypeChunk<EntityStore> var2, CommandBuffer<EntityStore> var3, EvaluationContext var4)`
  - Executes `calculateUtility` behavior.

## Notes
- No additional notes.
