---
description: Analyze documentation changes and generate a detailed report
agent: documentation-analyzer
subtask: true
---

Analyze documentation changes for this project:

1. Load current hashes from `build/hashes.json`
2. Scan all custom documentation in `docs/`
3. Compare hashes to identify changed classes
4. For each changed class, analyze added/removed/modified methods and fields
5. Generate a detailed report using the `report-generator` skill
6. Generate a checklist using the `checklist-generator` skill

Focus on:
- Classes where the hash differs from the documented hash
- New classes without custom documentation
- Removed classes that still have documentation

$ARGUMENTS
