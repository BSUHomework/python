
import sys
import unittest
import importlib
import collections

from unittest import mock
from io import StringIO


# uncomment the line below and change the path specified
# sys.path.insert(0, r'path_to_solution_folder')


class InterfaceTestCase(unittest.TestCase):
    def setUp(self):
        self._stdout_mock = self._setup_stdout_mock()

    def _setup_stdout_mock(self):
        patcher = mock.patch('sys.stdout', new=StringIO())
        patcher.start()
        self.addCleanup(patcher.stop)
        return patcher.new

    def _check_stdout_empty(self, file_name):
        if self._stdout_mock is not None:
            self.assertFalse(self._stdout_mock.getvalue(),
                             'no prints to console are allowed in "%s"' % file_name)
                             
    def _load_task(self, task_idx, file_name):
        try:
            loaded_task = importlib.import_module(file_name)
        except ImportError:
            self.fail('cannot import task #%d solution - no file "%s"' % (task_idx, file_name))
        return loaded_task
                             
    def _load_function(self, task_idx, file_name, func_names):
        loaded_task = self._load_task(task_idx, file_name)

        func_names = (func_names, ) if isinstance(func_names, str) else func_names
        loaded_functions = list(filter(None, (getattr(loaded_task, func_name, None) for func_name in func_names)))

        self.assertEqual(1, len(loaded_functions),
                         'cannot import task #%d solution - only one of function(-s) "%s" must be in file "%s"'
                         % (task_idx, file_name, func_names))

        return loaded_functions[0]
        
    def test_special_sum(self):
        f = self._load_function(0, 'special_sum', 'calculate_special_sum')
        self.assertEqual(14, f(3))
        self._check_stdout_empty('special_sum')
        
    def test_compress(self):
        f = self._load_function(0, 'unique', 'compress')
        expected_sorted = [(1, 2), (2, 1)]
        actual_sorted = sorted(f([1, 2, 1]))
        self.assertSequenceEqual(expected_sorted, actual_sorted)
        self._check_stdout_empty('unique')
        
    def test_primes(self):
        f = self._load_function(0, 'primes', 'get_primes')
        self.assertSequenceEqual([2, 3, 5, 7, 11], sorted(f(11)))
        self._check_stdout_empty('primes')
        
    def test_hist(self):
        f = self._load_function(0, 'hist', 'distribute')
        self.assertSequenceEqual([2, 2], f([1.25, 1, 2, 1.75], 2))
        self._check_stdout_empty('hist')


if __name__ == '__main__':
    unittest.main()
