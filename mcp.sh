#!/usr/bin/env bash

set -x

claude mcp add context7 --scope user -- npx -y @upstash/context7-mcp
# claude mcp add serena --scope user -- uv run --directory "$PIXI_PROJECT_ROOT/serena" serena start-mcp-server
claude mcp add --scope user --transport http github https://api.githubcopilot.com/mcp -H "Authorization: Bearer $(gh auth token)"
claude mcp add codex --scope user -- codex --model gpt-5 --config model_reasoning_effort=high mcp
claude mcp add repomix --scope user -- repomix --mcp
