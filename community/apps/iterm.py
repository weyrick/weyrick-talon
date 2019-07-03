from talon.voice import Key, Context

ctx = Context("iterm", bundle="com.googlecode.iterm2")

keymap = {
    "broadcaster": Key("cmd-alt-i"),
    "password": Key("cmd-alt-f"),
    # Pane creation and navigation
    "split horizontal": Key("cmd-shift-d"),
    "split vertical": Key("cmd-d"),
    "pane next": Key("cmd-]"),
    "pane last": Key("cmd-["),
    "goneck": Key("cmd-shift-]"),
    "gopreev": Key("cmd-shift-["),
}

ctx.keymap(keymap)
