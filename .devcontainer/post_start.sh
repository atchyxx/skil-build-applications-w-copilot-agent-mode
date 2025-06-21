#!/bin/bash
# This script is run after the container is started.

# open ports for Python Django server and React app
# Use the full `codespace` subcommand to avoid issues with shell aliasing
gh codespace ports visibility 8000:public -c "$CODESPACE_NAME"
gh codespace ports visibility 3000:public -c "$CODESPACE_NAME"
