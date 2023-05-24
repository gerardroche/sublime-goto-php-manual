# GotoPhpManual

A Sublime Text plugin for jumping to tags in the PHP Manual.

## Installation

**Pending availability in Package Control.**

Install via [Package Control](https://packagecontrol.io/packages/GotoPhpManual).

## Setup

Add your preferred key bindings.

**Menu → Preferences → Key Bindings**

```js
{
    "keys": ["f1"],
    "command": "goto_php_manual",
    "context": [
        {
            "key": "selector",
            "operator": "equal",
            "operand": "embedding.php",
            "match_all": true
        }
    ]
},
{
    "keys": ["shift+f1"],
    "command": "goto_php_manual",
    "args": {"remote": true},
    "context": [
        {
            "key": "selector",
            "operator": "equal",
            "operand": "embedding.php",
            "match_all": true
        }
     ]
},
```

If you use the GotoDocumentation plugin, exclude the PHP scope:

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

If you want to be able to goto local manual files, [download the PHP Documentation](https://www.php.net/download-docs.php) and set the location:

```js
"goto_php_manual.path": "~/path/to/php/manual",
```

## Settings

**Menu → Preferences → Settings**

Setting                 | Description                   | Type      | Default
:---                    | :----------                   | :---      | :------
`goto_php_manual.path`  | Path to local PHP manual.     | `string`  | Remote manual.

## License

Released under the [GPL-3.0-or-later License](LICENSE).
