#!/bin/bash

COMMIT_HOOK=$(curl "curl https://raw.githubusercontent.com/Stickerpants/emojihook/master/commit-msg")
COMMIT_PATH="./commit-msg"

if [ -d ".git/hooks" ]; then
	COMMIT_PATH=".git/hooks/commit-msg"
fi

echo "$COMMIT_HOOK" > COMMIT_PATH
chmod +x COMMIT_PATH

# TODO: Test me