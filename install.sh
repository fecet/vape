#!/usr/bin/env bash

pixi global install pnpm
pixi global install uv
npm install -g bun
npm install -g @anthropic-ai/claude-code
npm install -g ccstatusline
npm install -g ccusage
npm install -g @openai/codex

./mcp.sh
python CCPlugins/install.py
