# Contributing to CCPlugins

Thanks for your interest in improving CCPlugins! This project helps developers save time with practical automation.

## Branch Strategy

We keep it simple:

1. **`main`** - Stable code, always working
2. **`add/your-feature`** - Any contribution (new command, fix, docs)

### Workflow Example:
```bash
git checkout -b add/new-command
# make your changes
git push origin add/new-command
# open PR to main
```

## How to Contribute

### 1. New Commands
We welcome commands that solve real developer problems. Good commands:
- Save at least 5 minutes of repetitive work
- Are language/framework agnostic when possible
- Use context analysis rather than rigid rules

**To add a command:**
1. Create `commands/yourcommand.md`
2. Follow the existing command structure
3. Test it solves a real problem
4. Submit a PR with a clear use case

### 2. Improving Existing Commands
Found a bug or have an enhancement? Great! Please:
- Describe the current vs desired behavior
- Include examples if relevant
- Keep changes focused and minimal
- Consider adding validation phases for complex commands
- Use extended thinking for sophisticated analysis scenarios

### 3. Bug Reports
Open an issue with:
- What command failed
- What you expected
- Error message (if any)
- Your OS and Claude Code version

## Development Setup

```bash
git clone https://github.com/brennercruvinel/CCPlugins
cd CCPlugins
python install.py  # Test your changes
```

## Pull Request Guidelines

1. **One command per PR** - Makes review easier
2. **Test your changes** - Run `python install.py` to verify
3. **Keep it simple** - This project values pragmatism over perfection
4. **Update README** - Add your command to the table with a one-line description
5. **Quick merges** - If it works and helps, we merge it

### Commit Messages
Keep them simple:
- `add: command-name` for new commands
- `fix: what you fixed` for fixes
- `docs: what you updated` for documentation

## Command Quality Checklist

- [ ] Saves real time (5+ minutes)
- [ ] Works without configuration
- [ ] Handles common edge cases
- [ ] Clear, actionable output
- [ ] Under 100 lines
- [ ] Includes validation phase for complex commands
- [ ] No emojis in git-related output

## Advanced Command Features

For complex commands, consider implementing:

### Validation Phases
Commands like `/refactor` and `/implement` should include validation:
```
/refactor validate  # Check completeness, find loose ends
/implement validate # Verify integration completeness
```

### Extended Thinking
Use `<think>` blocks for sophisticated analysis in:
- Complex architectural refactoring
- Security vulnerability detection
- Multi-step problem solving

### Command Integration
Minimal, pragmatic suggestions for natural workflow:
- Suggest `/test` after major changes
- Suggest `/commit` at logical checkpoints
- Avoid over-engineering command chains

## What We're Looking For

**Yes:**
- Commands that automate tedious tasks
- Cross-platform compatibility improvements  
- Real-world workflow optimizations
- Validation phases for complex operations
- Pragmatic command integration

**No:**
- Framework-specific tools (unless very popular)
- Commands requiring external dependencies
- Overly complex multi-step wizards
- Over-engineered command orchestration

## Issue Templates

When creating issues, please use these templates:

### Bug Report
```
**Command:** /command-name
**Expected behavior:** What should happen
**Actual behavior:** What actually happened
**Steps to reproduce:**
1. Run command with these arguments
2. See error

**Environment:**
- OS: Windows/Linux/macOS
- Claude Code version: X.X.X
```

### Feature Request
```
**Problem:** What repetitive task are you doing?
**Solution:** How would the command help?
**Time saved:** Estimate minutes saved per use
**Example usage:** /proposed-command argument
```

## Community Standards

1. **Professional Communication** - Clear, concise, technical
2. **No Emojis in Code** - Keep commands, commits, PRs, and issues clean and professional
3. **Respect Time** - Quick reviews, fast merges for good contributions
4. **Test Before Submit** - Ensure your command works on major platforms
5. **Clean Architecture** - Follow clean code principles, no over-engineering

## Continuous Improvement

CCPlugins is actively maintained. We:
- Test commands thoroughly before release
- Refine based on real usage patterns
- Fix issues as they're discovered
- Welcome community feedback

Remember: Every command should make a developer's day a little easier.
