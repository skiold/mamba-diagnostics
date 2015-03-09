from expects import expect, equal
from server_expects import *
import os

with describe('i18n settings'):
    with before.all:
        self.default_lang = 'en_GB.UTF-8'

    with it('defaults to GB utf-8'):
        lang = os.environ['LANG']
        expect(lang).to(equal(self.default_lang))

    with it('defaults to GB utf-8 for new shells'):
        from shell_command import shell_output
        lang = shell_output("echo $LANG")
        expect(lang).to(equal(self.default_lang))
