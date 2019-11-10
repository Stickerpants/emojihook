# emojihook
Spice up your life (and your git commits)

# Installation

From your repo folder, navigate to `.git/hooks` and run:

	curl https://raw.githubusercontent.com/Stickerpants/emojihook/master/commit-msg > commit-msg && chmod +x commit-msg

# Emojis

```
:trash:       🗑
:spicy:       🔥
:ok:          👌
:bdb:         🍆
:thinking:    🤔
:orange:      🔶
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