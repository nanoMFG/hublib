from __future__ import print_function
import pytest
import sys
import ipywidgets as widgets
from . import setup_test_comm, teardown_test_comm
import hublib.ui as ui
from collections import Counter


class TestToggle:

    callbacks = Counter()
    cval = ''

    @staticmethod
    def cb(name, val):
        TestToggle.callbacks[name] += 1
        TestToggle.cval = val

    @classmethod
    def setup_class(cls):
        setup_test_comm()

    @classmethod
    def teardown_class(cls):
        teardown_test_comm()

    def test_basic(self):
        x = ui.Togglebuttons(
            name='Nut',
            description="Type of nut to eat.",
            value='almond',
            options=['peanut', 'walnut', 'almond', 'pecan'],
            width='50%'
        )

        assert x.value == 'almond'

        x.value = 'walnut'
        assert x.value == 'walnut'

        with pytest.raises(ValueError):
            x.value = 'pistachio'

    def test_callback(self):
        x = ui.Togglebuttons(
            name='Nut',
            description="Type of nut to eat.",
            value='almond',
            options=['peanut', 'walnut', 'almond', 'pecan'],
            cb=self.cb
        )

        x.value = 'walnut'
        assert x.value == 'walnut'
        assert TestToggle.cval == 'walnut'
        assert TestToggle.callbacks['Nut'] == 1

        x.value = 'pecan'
        assert x.value == 'pecan'
        assert TestToggle.cval == 'pecan'
        assert TestToggle.callbacks['Nut'] == 2

    def test_disable(self):
        x = ui.Togglebuttons(
            name='Nut',
            description="Type of nut to eat.",
            value='almond',
            options=['peanut', 'walnut', 'almond', 'pecan'],
            width='50%'
        )

        assert x.disabled is False
        x.disabled = True
        assert x.disabled is True
        x.disabled = False
        assert x.disabled is False
