# InstructionContextHelper

## Overview
- Documentation for `InstructionContextHelper`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder`.

## Constructors
- `InstructionContextHelper(InstructionType context)`
  - Creates a `InstructionContextHelper` instance.

## Methods
- `isComponent()`
  - Executes `isComponent` behavior.
- `setComponentContext(ComponentContext context)`
  - Executes `setComponentContext` behavior.
- `isInCorrectInstruction(@Nonnull EnumSet<InstructionType> validTypes)`
  - Executes `isInCorrectInstruction` behavior.
- `isInCorrectInstruction(@Nonnull EnumSet<InstructionType> validTypes, InstructionType instructionContext)`
  - Executes `isInCorrectInstruction` behavior.
- `extraContextMatches(@Nullable EnumSet<ComponentContext> contexts)`
  - Executes `extraContextMatches` behavior.
- `extraContextMatches(@Nullable EnumSet<ComponentContext> validContexts, ComponentContext context)`
  - Executes `extraContextMatches` behavior.
- `addComponentContextEvaluator(BiConsumer<InstructionType, ComponentContext> evaluator)`
  - Executes `addComponentContextEvaluator` behavior.
- `validateComponentContext(InstructionType instructionContext, ComponentContext componentContext)`
  - Executes `validateComponentContext` behavior.
- `getInstructionContext()`
  - Executes `getInstructionContext` behavior.
- `getComponentContext()`
  - Executes `getComponentContext` behavior.

## Notes
- No additional notes.
