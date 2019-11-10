# emojihook
Spice up your life (and your git commits)

# Installation

From the root of your repo folder, run the following:

	sh -c "$(curl -fsSL https://raw.githubusercontent.com/Stickerpants/emojihook/master/install.sh)"

# Emojis

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
```

# Uninstall

Delete the `commit-msg` hook:

	rm .git/hooks/commit-msg

# TODO

* Better windows support (doesn't work if run from windows... because file handling differences?)