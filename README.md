# Goto PHP Manual

A Sublime Text plugin for jumping to the PHP Manual for the current symbol.

Put your cursor on a php symbol and press `f1` or `shift+f1` to open the php manual in your browser.

Handy if you need the php manual when working offline.

## Installation

Install [GotoPhpManual](https://packagecontrol.io/packages/GotoPhpManual) via Package Control.

## Setup

### Local PHP Manual

To use a local php manual, [download the manual](https://www.php.net/download-docs.php), the "Many HTML files" tarball, unpack it somewhere, and set the location:

```js
"goto_php_manual.path": "~/manuals/php",
```

If you use the [GotoDocumentation](https://packagecontrol.io/packages/GotoDocumentation) plugin and use `f1` for it, then add a context exclude for PHP scope: Menu → Preferences → Key Bindings:

```js
{
    "keys": ["f1"],
    "command": "goto_documentation",
    "context": [
        {
            "key": "selector",
            "operator": "equal",
            "operand": "-embedding.php",
            "match_all": true
        }
    ]
},
```

If you use [NeoVintageous](https://packagecontrol.io/packages/NeoVintageous), disable the `f1` and `shift+f1` keys.

Menu → Preferences → Settings

```js
"vintageous_handle_keys": {
    "<f1>": false,
    "<S-f1>": false,
},
```

Read [configuring the NeoVintageous sublime vim key handler](https://blog.gerardroche.com/2022/09/22/neovintageous-key-handler/) for a short guide on configuring the vim key handler in sublime.

## Key Bindings

Key        | Description
:----------|:-----------
`f1`       | Goto local manual or remote manual.
`shift+f1` | Goto remote manual

## Settings

**Menu → Preferences → Settings**

Setting                   | Description               | Type     | Default
:-------------------------|:--------------------------|:--------:|:-------:
`goto_php_manual.path`    | Path to local php manual. | `string` | `null`
`goto_php_manual.keymaps` | Enable keymaps.           | `bool`   | `true`

## License

Released under the [GPL-3.0-or-later License](LICENSE).
