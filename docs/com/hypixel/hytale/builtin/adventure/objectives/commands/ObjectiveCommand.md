**Source Hash:** `37370a5779728cf777083dc2dc2bcd059c05d5e2fd57d3f7047c3db715c8af85`
**Last Updated:** 2026-01-18T19:03:47-03:00

# ObjectiveCommand

## Overview
Main command collection for objective-related administrative commands. This class extends AbstractCommandCollection to provide a unified "/objective" (or "/obj") command interface with multiple subcommands for managing, monitoring, and debugging the objective system.

## Constructor Descriptions
- `ObjectiveCommand()`: Creates the main objective command with permission "server.commands.objective" and alias "obj". Registers all objective-related subcommands including start, complete, panel, history, and marker management commands.

## Method Descriptions
No additional methods beyond inherited AbstractCommandCollection functionality.

## Usage Notes
- Requires "server.commands.objective" permission to use
- Provides the "obj" alias for shorter command typing
- All subcommands are administrative tools for objective management
- Subcommands handle objective lifecycle, debugging, and location marker management

## Subcommands Registered
- **ObjectiveStartCommand**: Manually start objectives for testing and debugging
- **ObjectiveCompleteCommand**: Force completion of objectives for testing
- **ObjectivePanelCommand**: Open objective management panels for administrators
- **ObjectiveHistoryCommand**: View objective completion history and statistics
- **ObjectiveLocationMarkerCommand**: Manage objective location markers
- **ObjectiveReachLocationMarkerCommand**: Handle reach location marker functionality

## Examples
```bash
# Command usage examples
/objective start <objective_id> <player>
/obj complete <objective_id> <player>
/objective panel <player>
/obj history <player> [objective_id]
/objective marker list
/obj marker create <name> <x> <y> <z>
```
