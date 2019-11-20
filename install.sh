#!/bin/bash

COMMIT_HOOK=$(curl -fsSL "https://raw.githubusercontent.com/Stickerpants/emojihook/master/commit-msg")
COMMIT_PATH="./commit-msg"

# TODO: Metrics tagging?

if [ -d ".git/hooks" ]; then
	COMMIT_PATH=".git/hooks/commit-msg"
	echo "Detected hooks folder, writing to '$COMMIT_PATH'..."
else
	echo "Can't determine if this is a git repo. Writing to '$COMMIT_PATH', move it into your hooks folder!"
fi

echo "$COMMIT_HOOK" > $COMMIT_PATH
chmod +x $COMMIT_PATH
