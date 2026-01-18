# BackupTask

## Overview
- Documentation for `BackupTask`.
- Declared as a class in `com.hypixel.hytale.server.core.util.backup`.

## Constructors
- `BackupTask(universeDir, backupDir)`
  - Creates a `BackupTask` instance.
- `BackupTask(final @Nonnull Path universeDir, final @Nonnull Path backupDir)`
  - Creates a `BackupTask` instance.

## Methods
- `start(@Nonnull Path universeDir, @Nonnull Path backupDir)`
  - Executes `start` behavior.
- `run()`
  - Executes `run` behavior.
- `cleanOrArchiveOldBackups(@Nonnull Path sourceDir, @Nonnull Path archiveDir)`
  - Executes `cleanOrArchiveOldBackups` behavior.
- `cleanOldBackups(@Nonnull Path dir)`
  - Executes `cleanOldBackups` behavior.
- `getMostRecentArchive(@Nonnull Path dir)`
  - Executes `getMostRecentArchive` behavior.

## Notes
- No additional notes.
