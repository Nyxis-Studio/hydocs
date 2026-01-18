---
name: checklist-generator
description: Generates standardized checklists for documentation tasks and quality validation
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: documentation
---

## What I Do

Generate consistent, structured checklists for documentation review and validation tasks.

## Checklist Template

Always use this format:

# [Checklist Title]

**Generated:** YYYY-MM-DD HH:MM
**Scope:** [short scope description]

## Summary

- Total items: X
- Completed: Y
- Pending: Z

---

## High Priority

- [ ] **[Item Name]** - [brief description]
  - File: `path/to/file`
  - Reason: [why this is high priority]

## Medium Priority

- [ ] **[Item Name]** - [brief description]
  - File: `path/to/file`

## Low Priority

- [ ] **[Item Name]** - [brief description]

---

## Notes

[Any additional context or instructions]

## Example Output

# Documentation Review Checklist

**Generated:** 2026-01-18 14:30
**Scope:** Classes with hash mismatches requiring review

## Summary

- Total items: 15
- Completed: 0
- Pending: 15

---

## High Priority

- [ ] **HytaleServer** - Core server class with 12 method changes
  - File: `docs/com/hypixel/hytale/server/core/HytaleServer.md`
  - Reason: Critical class, many changes detected

- [ ] **PluginManager** - Plugin loading system modified
  - File: `docs/com/hypixel/hytale/plugin/PluginManager.md`
  - Reason: API changes may affect documentation accuracy

## Medium Priority

- [ ] **EventBus** - 3 new methods added
  - File: `docs/com/hypixel/hytale/event/EventBus.md`

## Low Priority

- [ ] **StringUtil** - Minor utility changes
  - File: `docs/com/hypixel/hytale/common/util/StringUtil.md`

---

## Notes

Run `python3 hydocs.py --only-docs` after reviewing to regenerate documentation.
