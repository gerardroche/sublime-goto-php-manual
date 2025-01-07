# Goto PHP Manual

A Sublime Text commands that open the PHP Manual for a keyword or symbol.

## How to use

Place your cursor on a PHP keyword or symbol and press `f1` to open the **local PHP manual** (if configured), or `shift+f1` to open the **online PHP manual**.

## How to setup a local PHP Manual

Download the [PHP manual](https://www.php.net/download-docs.php), pick the "many HTML files" tar.gz, and unpack it.

Set the PHP manual path of your unpacked local manual.

> Command Palette → Preferences: Settings

```js
"goto_php_manual.path": "~/php-manual/php-chunked-xhtml",
```
## If you use NeoVintageous

Disable the `f1` and `shift+f1` keys.

> Command Palette → Preferences: Settings

```js
"vintageous_handle_keys": {
    "<f1>": false,
    "<S-f1>": false,
},
```

For more information on configuring NeoVintageous see [configuring the NeoVintageous key handler](https://blog.gerardroche.com/2022/09/22/neovintageous-key-handler/).

## If you use GotoDocumentation

If you use [GotoDocumentation](https://packagecontrol.io/packages/GotoDocumentation) and also use the `f1` key binding, then add a context *exclude* for the PHP scope so that `f1` passes through to Goto PHP Manual.

> Command Palette → Preferences → Key Bindings

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

## Key Bindings

Key        | Description
:----------|:-----------
`f1`       | Open local PHP manual with fallback to online PHP manual.
`shift+f1` | Open online PHP manual.

## Settings

**Command Palette → Preferences: Settings**

Setting                   | Description               | Type     | Default
:-------------------------|:--------------------------|:--------:|:-------:
`goto_php_manual.path`    | Path to local php manual. | `string` | `null`
`goto_php_manual.keymaps` | Enable keymaps.           | `bool`   | `true`

## Installation

Install [GotoPhpManual](https://packagecontrol.io/packages/GotoPhpManual) via Package Control.

## License

Released under the [GPL-3.0-or-later License](LICENSE).
