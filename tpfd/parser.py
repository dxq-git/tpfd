"""
parser.py
This contains the main Parser class that can be instantiated to create rules.
"""
import logging
from .rules import RuleMap

from parse import parse

class Parser(object):
    """
    Parser exposes a couple methods for reading in strings.
    Currently only parse_file is working.
    """

    def __init__(self):
        """Initalizer"""
        self.debug = False
        self._rule_map = RuleMap(list)


    def on_recognize(self, eventname):
        """Decorator for rules. Calls the associated functions when the rule is invoked via voice"""
        def eventdecorator(func):
            """Event decorator closure thing"""
            self._func_registry.add_rule(eventname, func)
            return func
        return eventdecorator


    def parse_file(self, file):
        with open(file, 'r') as f:
            for line in f:
                self._rule_map.query(line)