#!/usr/bin/env bash

pixi global install pnpm
pixi global install uv
pnpm install -g bun
pnpm install -g @anthropic-ai/claude-code
pnpm install -g ccstatusline
pnpm install -g ccusage
pnpm install -g @openai/codex
pnpm install -g repomix
