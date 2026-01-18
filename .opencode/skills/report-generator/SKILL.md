---
name: report-generator
description: Generates detailed change reports comparing documentation hashes and detecting function modifications
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: documentation
---

## What I Do

Generate comprehensive change reports that include summary statistics and per-class details.

## Report Template

Always use this format:

# Documentation Change Report

**Generated:** YYYY-MM-DD HH:MM
**Comparison:** [old version] -> [new version]
**Total Classes Analyzed:** X

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Classes Changed | X |
| Methods Added | Y |
| Methods Removed | Z |
| Fields Added | A |
| Fields Removed | B |
| Unchanged Classes | C |

### Key Changes

1. **[Most significant change]** - Brief description
2. **[Second most significant]** - Brief description
3. **[Third most significant]** - Brief description

---

## Detailed Changes

### [Package Name]

#### [ClassName]

**File:** `path/to/documentation.md`
**Hash:** `old_hash` -> `new_hash`
**Status:** MODIFIED | NEW | REMOVED

##### Methods Added
- `methodName(ParamType param): ReturnType` - [brief description if available]

##### Methods Removed
- `oldMethodName()` - [reason if known]

##### Methods Modified
- `existingMethod(...)` - Signature changed from X to Y

##### Fields Added
- `NEW_FIELD: Type`

##### Fields Removed
- `OLD_FIELD`

---

## Classes Without Changes

<details>
<summary>X classes unchanged (click to expand)</summary>

- `com.package.Class1`
- `com.package.Class2`
- ...

</details>

---

## Recommendations

1. **[Recommendation 1]** - Action to take
2. **[Recommendation 2]** - Action to take

## Next Steps

- [ ] Review high-priority classes
- [ ] Update custom documentation for changed APIs
- [ ] Run `python3 hydocs.py --only-docs` to regenerate

## Example Output

# Documentation Change Report

**Generated:** 2026-01-18 14:45
**Comparison:** Build 1.0.0 -> Build 1.1.0
**Total Classes Analyzed:** 4851

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Classes Changed | 63 |
| Methods Added | 127 |
| Methods Removed | 23 |
| Fields Added | 45 |
| Fields Removed | 8 |
| Unchanged Classes | 4788 |

### Key Changes

1. **HytaleServer** - Major refactoring with 12 new lifecycle methods
2. **WorldGenerator** - New biome generation system added
3. **PluginManager** - Deprecated methods removed, async loading added

---

## Detailed Changes

### com.hypixel.hytale.server.core

#### HytaleServer

**File:** `docs/com/hypixel/hytale/server/core/HytaleServer.md`
**Hash:** `a9162add3c6c...` -> `b8273bce4d7d...`
**Status:** MODIFIED

##### Methods Added
- `getAsyncExecutor(): ExecutorService` - Returns async task executor
- `registerShutdownHook(Runnable hook): void` - Registers shutdown callback
- `getUptime(): Duration` - Returns server uptime

##### Methods Removed
- `getOldExecutor()` - Replaced by getAsyncExecutor

##### Fields Added
- `ASYNC_EXECUTOR: ExecutorService`

---

## Recommendations

1. **Update HytaleServer documentation** - Major API changes require custom docs review
2. **Review deprecated method usage** - 23 methods were removed
3. **Document new async patterns** - New executor system needs usage examples

## Next Steps

- [ ] Review HytaleServer changes (high priority)
- [ ] Update WorldGenerator documentation
- [ ] Regenerate all documentation with new hashes
