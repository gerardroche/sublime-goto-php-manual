# Copyright (C) 2023 Gerard Roche
#
# This file is part of GotoPhpManual.
#
# GotoPhpManual is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GotoPhpManual is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GotoPhpManual.  If not, see <https://www.gnu.org/licenses/>.

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
