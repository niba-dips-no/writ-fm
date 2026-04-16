#!/bin/bash
# Wrapper for next_track.py — ezstream calls this for each track.
# Passes all arguments through.
cd /Volumes/K3/agent-working-space/projects/active/2025-12-29-radio-station
exec uv run python mac/next_track.py "$@"
