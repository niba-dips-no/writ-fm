#!/bin/bash
# Metadata script for ezstream — prints current artist/title.
cd /Volumes/K3/agent-working-space/projects/active/2025-12-29-radio-station
exec uv run python mac/next_track.py --metadata
