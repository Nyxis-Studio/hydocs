**Source Hash:** `b8e6d2a0232cc5ebbfc36e68d3be6ea5c062179861fed5865944432541a8a5dd`

# StdScope

## Overview

## Constructor Descriptions
- `StdScope(Scope parent)`
  - Creates a `StdScope` instance.
- `StdScope(other.parent)`
  - Creates a `StdScope` instance.

## Method Descriptions
- `copyOf(@Nonnull StdScope other)`: Add description.
  - Executes `copyOf` behavior.
- `merge(@Nonnull StdScope other)`: Add description.
  - Executes `merge` behavior.
- `mergeScopes(@Nonnull StdScope first, @Nonnull StdScope second)`: Add description.
  - Executes `mergeScopes` behavior.
- `mergeSymbols(@Nonnull StdScope other)`: Add description.
  - Executes `mergeSymbols` behavior.
- `add(String name, Symbol symbol)`: Add description.
  - Executes `add` behavior.
- `addConst(String name, @Nullable String value)`: Add description.
  - Executes `addConst` behavior.
- `addConst(String name, double value)`: Add description.
  - Executes `addConst` behavior.
- `addConst(String name, boolean value)`: Add description.
  - Executes `addConst` behavior.
- `addConst(String name, @Nullable String[] value)`: Add description.
  - Executes `addConst` behavior.
- `addConst(String name, @Nullable double[] value)`: Add description.
  - Executes `addConst` behavior.
- `addConst(String name, @Nullable boolean[] value)`: Add description.
  - Executes `addConst` behavior.
- `addConstEmptyArray(String name)`: Add description.
  - Executes `addConstEmptyArray` behavior.
- `addVar(String name, @Nullable String value)`: Add description.
  - Executes `addVar` behavior.
- `addVar(String name, double value)`: Add description.
  - Executes `addVar` behavior.
- `addVar(String name, boolean value)`: Add description.
  - Executes `addVar` behavior.
- `addVar(String name, @Nullable String[] value)`: Add description.
  - Executes `addVar` behavior.
- `addVar(String name, @Nullable double[] value)`: Add description.
  - Executes `addVar` behavior.
- `addVar(String name, @Nullable boolean[] value)`: Add description.
  - Executes `addVar` behavior.
- `addInvariant(@Nonnull String name, Scope.Function function, ValueType returnType, ValueType ... argumentTypes)`: Add description.
  - Executes `addInvariant` behavior.
- `addVariant(@Nonnull String name, Scope.Function function, ValueType returnType, ValueType ... argumentTypes)`: Add description.
  - Executes `addVariant` behavior.
- `addSupplier(String name, Supplier<String> value)`: Add description.
  - Executes `addSupplier` behavior.
- `addSupplier(String name, DoubleSupplier value)`: Add description.
  - Executes `addSupplier` behavior.
- `addSupplier(String name, BooleanSupplier value)`: Add description.
  - Executes `addSupplier` behavior.
- `addStringArraySupplier(String name, Supplier<String[]> value)`: Add description.
  - Executes `addStringArraySupplier` behavior.
- `addDoubleArraySupplier(String name, Supplier<double[]> value)`: Add description.
  - Executes `addDoubleArraySupplier` behavior.
- `addBooleanArraySupplier(String name, Supplier<boolean[]> value)`: Add description.
  - Executes `addBooleanArraySupplier` behavior.
- `get(String name)`: Add description.
  - Executes `get` behavior.
- `get(String name, ValueType valueType)`: Add description.
  - Executes `get` behavior.
- `replace(String name, @Nonnull Symbol symbol)`: Add description.
  - Executes `replace` behavior.
- `changeValue(String name, @Nullable String value)`: Add description.
  - Executes `changeValue` behavior.
- `changeValue(String name, double value)`: Add description.
  - Executes `changeValue` behavior.
- `changeValue(String name, boolean value)`: Add description.
  - Executes `changeValue` behavior.
- `changeValue(String name, @Nullable String[] value)`: Add description.
  - Executes `changeValue` behavior.
- `changeValue(String name, @Nullable double[] value)`: Add description.
  - Executes `changeValue` behavior.
- `changeValue(String name, @Nullable boolean[] value)`: Add description.
  - Executes `changeValue` behavior.
- `changeValueToEmptyArray(String name)`: Add description.
  - Executes `changeValueToEmptyArray` behavior.
- `getStringSupplier(String name)`: Add description.
  - Executes `getStringSupplier` behavior.
- `getNumberSupplier(String name)`: Add description.
  - Executes `getNumberSupplier` behavior.
- `getBooleanSupplier(String name)`: Add description.
  - Executes `getBooleanSupplier` behavior.
- `getStringArraySupplier(String name)`: Add description.
  - Executes `getStringArraySupplier` behavior.
- `getNumberArraySupplier(String name)`: Add description.
  - Executes `getNumberArraySupplier` behavior.
- `getBooleanArraySupplier(String name)`: Add description.
  - Executes `getBooleanArraySupplier` behavior.
- `isConstant(String name)`: Add description.
  - Executes `isConstant` behavior.
- `getType(String name)`: Add description.
  - Executes `getType` behavior.

## Notes
- No additional notes.
