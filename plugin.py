import os
import re
import webbrowser

from sublime import status_message
import sublime_plugin


class GotoPhpManualCommand(sublime_plugin.WindowCommand):

    def run(self, remote: bool = False) -> None:
        view = self.window.active_view()
        if not view:
            return

        symbol = _get_symbol(view)
        if not symbol:
            return

        if remote:
            self.goto_remote(symbol)
        else:
            path = _get_path(view)
            if not path:
                self.goto_remote(symbol)
                return

            self.goto_local(path, symbol)

    def goto_remote(self, symbol: str) -> None:
        webbrowser.open_new_tab('https://secure.php.net/%s' % symbol)

    def goto_local(self, path: str, symbol: str) -> None:
        # https://secure.php.net/urlhowto.php
        _open_file_in_browser('%s/php/language.types.%s.html' % (path, symbol))
        _open_file_in_browser('%s/php/control-structures.%s.html' % (path, symbol))
        _open_file_in_browser('%s/php/book.%s.html' % (path, symbol))
        _open_file_in_browser('%s/php/class.%s.html' % (path, symbol))
        _open_file_in_browser('%s/php/function.%s.html' % (path, symbol))


def _get_symbol(view):
    symbol = view.substr(view.word(view.sel()[0]))
    if not _is_php_identifier(symbol):
        return None

    return symbol.replace('_', '-').lower()


def _is_php_identifier(value: str) -> bool:
    return bool(re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', value))


def _open_file_in_browser(file_name: str) -> None:
    if os.path.isfile(file_name):
        webbrowser.open_new_tab('file://%s' % file_name)
    else:
        status_message('GotoPhpManual: file not found: %s' % file_name)


def _get_path(view):
    path = view.settings().get('goto_php_manual.path')
    if not path:
        return None

    path = os.path.expanduser(path)
    path = os.path.expandvars(path)

    if not os.path.isdir(path):
        return None

    return path
