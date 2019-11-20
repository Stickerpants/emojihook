# Emojihook
Spice up your life (and your git commits)!

# Installation

Tested and compatible on Windows, Linux, and MacOS.

From the root of your repo folder, run the following:

	sh -c "$(curl -fsSL https://raw.githubusercontent.com/Stickerpants/emojihook/master/install.sh)"

# Emoji List

```
:trash:       🗑
:spicy:       🔥,🔶,📙
:ok:          👌,🆗✋
:bdb:         🍆
:thinking:    🤔
:gun:         🔫
:brain:       🧠
:zoop:        👉😎👉
:sus:         🤨
:no:          🚫
:x:           ❌
:warning:     ⚠️
:checkbox:    ✅
:checkmark:   ✔️
:bug:         🐛
:cowboy:      🤠,🐄👦
```

# Uninstall

Delete the `commit-msg` hook:

	rm .git/hooks/commit-msg

# TODO

De-duplicate the emoji list in `README.md` and `emojis.txt`