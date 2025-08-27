#!/usr/bin/env bash

claude mcp add context7 --scope user -- npx -y @upstash/context7-mcp
claude mcp add playwright --scope user -- npx -y @playwright/mcp@latest
claude mcp add serena --scope user -- uv run --directory "$PIXI_PROJECT_ROOT/serena" serena start-mcp-server
if [[ -n "$GITHUB_PAT" ]]; then
  claude mcp add --scope user --transport http github https://api.githubcopilot.com/mcp -H "Authorization: Bearer $(grep GITHUB_PAT .env | cut -d '=' -f2)"
fi
