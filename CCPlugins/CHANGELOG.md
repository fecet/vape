# Changelog

All notable changes to CCPlugins will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Extended Thinking Mode:**
  - Added to `/refactor` for complex architectural refactoring analysis
  - Added to `/security-scan` for sophisticated vulnerability detection
  - Triggers on complex scenarios requiring deep analysis

- **Minimal Command Orchestration:**
  - `/implement` suggests `/test` and `/commit` after milestones
  - `/refactor` suggests `/test` and `/commit` at logical checkpoints
  - `/security-scan` suggests `/test` and `/commit` for critical fixes
  - `/fix-todos` suggests `/test` and `/commit` after resolving critical TODOs
  - Pragmatic integration without over-engineering

### Removed
- `/human-mode` command - Functionality was redundant with Claude's natural adaptability

## [2.5.2] - 2025-08-02

### Added
- **Session Persistence for Complex Commands:**
  - `/implement`, `/refactor`, `/fix-todos`, `/scaffold`, `/security-scan`, `/fix-imports` now maintain state across Claude sessions
  - Session files stored in command-specific folders for better organization
  - Auto-resume capabilities with progress tracking and statistics
  - Intelligent plan creation before execution to ensure consistency

- **Cross-Platform Compatibility:**
  - All commands now work on Windows, Linux, and macOS
  - Replaced shell-specific commands with Claude native tools
  - Path handling uses forward slashes for universal compatibility
  - Removed dependencies on bash-specific features

### Enhanced
- **Command Improvements:**
  - Reduced verbosity while maintaining clarity (73% reduction in `/implement`, 56% in `/refactor`)
  - Added mandatory plan creation before execution in complex commands
  - Improved error handling and recovery strategies
  - Better integration between related commands

- **Documentation:**
  - Added continuous development notice highlighting active maintenance
  - Enhanced architecture description with visual flow diagrams
  - Added developer mood emojis to problem statements
  - Improved high-level technical documentation

- **Git Safety:**
  - Added explicit AI attribution prevention to all git-related commands
  - Ensures no "Co-authored-by" or AI signatures in commits
  - Protects user ownership of all code changes

### Fixed
- **Critical Path Resolution Fix:**
  - Fixed Claude LS tool not recognizing hidden folders starting with dot (.)
  - Changed from hidden `.claude/` folder to visible command-specific folders
  - Each command now creates its own folder: `refactor/`, `implement/`, `fix-imports/`, `security-scan/`, `scaffold/`
  - Resolved issue where Claude would fail to find existing session files and create duplicate folders
  - Commands now correctly resume sessions without path confusion
- Session files now save in project directory instead of global Claude installation
- Fixed Claude interpreting relative paths incorrectly (was looking in parent directories)
- Removed shell command dependencies for Windows compatibility
- Corrected session persistence logic to always create plans first

## [2.5.1] - 2025-08-02

### Added
- **New Command:**
  - `/refactor` - Intelligent code restructuring engine with cross-session continuity
    - Strategic thinking process for safe refactoring decisions
    - Session state management for large refactoring operations
    - Auto-detection and resume capabilities across context windows
    - Support for multiple refactoring modes (conservative, balanced, architectural, migration)
    - Comprehensive rollback and recovery options
    - Integration with existing CCPlugins workflow

### Enhanced
- **Documentation:**
  - Updated README with `/refactor` command and new workflow examples
  - Added refactoring metrics to performance table
  - Updated total time savings calculation

## [2.5.0] - 2025-08-02

### Added
- **New Command:**
  - `/implement` - Smart implementation engine that imports and adapts code from any source (GitHub, CodePen, local folders, or multiple references)
    - Intelligent dependency resolution using existing packages
    - Best practices validation and modern pattern enforcement
    - Multi-source merge capabilities
    - Research mode for implementing concepts without specific source

- **Think Tool Integration:**
  - Added strategic thinking process to 7 critical commands for improved decision-making
  - Commands enhanced: `/scaffold`, `/make-it-pretty`, `/cleanproject`, `/predict-issues`, `/fix-todos`, `/contributing`, `/fix-imports`
  - Based on Anthropic's "think" tool research showing 50%+ improvement in complex tasks

### Enhanced
- **Dependency Management:**
  - All commands now check existing packages before suggesting new dependencies
  - Smart mapping of source dependencies to existing project packages
  - Version compatibility validation

- **Code Quality:**
  - Enhanced pattern detection and adaptation in implementation commands
  - Improved best practices enforcement based on 2025 standards
  - Better security validation for imported code

## [2.4.2] - 2025-08-01

### Added
- **New Commands:**
  - `/create-todos` - Intelligently creates contextual TODO comments in code based on recent operations
  - `/fix-todos` - Analyzes and implements TODO fixes with full context understanding
  - `/understand` - Analyzes entire project architecture, patterns, and component relationships
  - `/docs` - Smart documentation management with multiple modes (read, update, session-based)
  
- **Security Enhancements:**
  - Added anti-attribution instructions to all git/GitHub commands
  - Prevents AI signatures in commits, issues, and PRs
  - Protects user identity and maintains code ownership

### Enhanced
- **`/contributing` Command:**
  - Full context awareness for different development scenarios
  - Mandatory pre-flight checks before GitHub operations
  - Intelligent remote repository scanning for issue linking
  - Professional standards enforcement (no emojis, concise)
  - Automated issue creation and PR management
- **`/test` Command:**
  - Context awareness for different testing scenarios
  - Smart test selection based on current work
  - Session awareness with CLAUDE.md integration
  - Build verification before running tests
  - Console output and log monitoring
  - Auto-fix for common test failures
  - Pattern detection for memory leaks, port conflicts, timeouts
  - Advanced diagnostics with log analysis

- **`/todos-to-issues` Command:**
  - Mandatory quality checks before creating GitHub issues
  - Complete project context analysis
  - Reads all documentation (README, CONTRIBUTING, templates)
  - Adapts to repository type (fork, personal, organization)
  - Follows upstream guidelines for forks
  - Smart issue generation matching project style
  
- **`/commit` Command:**
  - Pre-commit quality checks
  - Build and test verification before committing

### Fixed
- Removed specific build tool references from `/test` for better framework agnosticism
- Updated all git-related commands with security instructions

## [2.0.0] - 2025-08-01

### Added
- **New Commands (5):**
  - `/security-scan` - Comprehensive security analysis with dependency health checking
  - `/scaffold` - Intelligent feature scaffolding with auto-generated tests and docs
  - `/predict-issues` - Proactive problem detection with timeline estimates  
  - `/contributing` - Complete contribution readiness analysis comparing local vs remote
  - `/explain-like-senior` - Senior-level code explanations with architectural context

- **Claude Code CLI Native Integration:**
  - Migration to native tools (Grep, Glob, Read, TodoWrite) across all commands
  - Sub-agent architecture for specialized analysis (security, performance, quality, architecture)
  - CLAUDE.md memory system integration replacing parallel session system
  - Git checkpoint safety replacing custom backup systems

- **Advanced Features:**
  - Multi-step operation tracking with TodoWrite integration
  - Context-aware analysis without technology stack assumptions
  - Intelligent issue creation with duplicate detection
  - Professional workflow integration examples
  - Streamlined CI/CD command chaining

### Changed
- **Performance Optimizations:**
  - Reduced verbosity across all commands for senior developer efficiency
  - Native tool usage for improved performance on large codebases
  - Parallel execution optimization where beneficial
  - Streamlined command outputs with actionable results

- **Architecture Improvements:**
  - `/review` now uses specialized sub-agents (security, performance, quality, architecture)
  - `/session-start` and `/session-end` integrated with Claude Code CLI memory system
  - `/cleanproject` uses git checkpoints instead of custom backup directories
  - `/find-todos` and `/fix-imports` migrated to native Grep/Glob tools
  - All commands follow consistent safety-first design with git checkpoints

- **Documentation:**
  - Complete README overhaul with technical architecture details
  - Professional workflow integration examples
  - Performance metrics updated with new command capabilities
  - Streamlined installation and usage instructions

### Enhanced
- **Security:**
  - Input validation and sanitization across all commands
  - Safe file operations with proper validation
  - Secure handling of sensitive information detection
  - Security audit of all existing commands

- **Functionality Consolidation:**
  - Dependency health analysis integrated into `/security-scan`
  - Architecture review capabilities added to `/review` sub-agents
  - Auto-documentation and smart test generation integrated into `/scaffold`
  - Improvement suggestions distributed across relevant analysis commands

### Fixed
- Session management system now uses native CLAUDE.md instead of parallel tracking
- Commands no longer use framework-specific detection, rely on intelligent analysis
- Removed all hardcoded technology references for true framework agnosticism
- Git safety operations consistent across all destructive commands
- TodoWrite integration prevents lost progress in multi-step operations

### Removed
- `/context-cache` - Removed as Claude Code already maintains context automatically
- `/cleanup-types` - Merged functionality into `/make-it-pretty`
- Custom backup systems replaced with git checkpoint safety
- Parallel session directory system replaced with CLAUDE.md integration

## [1.6.0] - 2025-01-25

### Added
- Basic testing with Kimi K2 compatibility
- Cross-platform installation support (Windows/Mac/Linux)
- 11 productivity commands for common development workflows
- `/cleanproject` - Remove debug artifacts and clean up after development sessions
- `/commit` - Analyze changes and create conventional commit messages
- `/format` - Auto-detect and run the project's code formatter
- `/test` - Run tests and automatically fix simple failures
- `/review` - Comprehensive code review for bugs, security, and performance
- `/remove-comments` - Remove obvious comments while preserving valuable documentation
- `/cleanup-types` - Remove TypeScript 'any' types and suggest proper types (now part of `/make-it-pretty`)
- `/fix-imports` - Fix broken imports after moving or renaming files
- `/find-todos` - Find all TODO, FIXME, and HACK comments in your codebase
- `/session-start` - Begin a documented coding session with goals tracking
- `/session-end` - Summarize accomplishments and prepare handoff notes

### Changed
- Improved README with better examples and time-saving metrics
- Enhanced installation process with automatic backup of existing commands

### Fixed
- Installation script compatibility across different operating systems

## [1.5.0] - 2025-12-15

### Added
- Initial release with core command set
- Python-based installer
- Shell script for Unix-like systems

[Unreleased]: https://github.com/brennercruvinel/CCPlugins/compare/v2.5.2...HEAD
[2.5.2]: https://github.com/brennercruvinel/CCPlugins/compare/v2.5.1...v2.5.2
[2.5.1]: https://github.com/brennercruvinel/CCPlugins/compare/v2.0.0...v2.5.1
[2.0.0]: https://github.com/brennercruvinel/CCPlugins/compare/v1.6.0...v2.0.0
[1.6.0]: https://github.com/brennercruvinel/CCPlugins/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/brennercruvinel/CCPlugins/releases/tag/v1.5.0
