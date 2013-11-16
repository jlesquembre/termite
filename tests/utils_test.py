import unittest
import tempfile
import os
from time import sleep

from termite.utils import Files, _as_list


def get_tuple(m=None, n=None, d=None):

    modified = set() if m is None else set(_as_list(m))
    new = set() if n is None else set(_as_list(n))
    deleted = set() if d is None else set(_as_list(d))

    return modified, new, deleted


class TestCaseWithTmp(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = self._tmp.name
        self._cwd = os.getcwd()
        os.chdir(self.tmp)

    def tearDown(self):
        self._tmp.cleanup()
        os.chdir(self._cwd)

    def modify(self, filename):
        for element in _as_list(filename):

            directory, _ = os.path.split(element)
            if directory:
                os.makedirs(directory, exist_ok=True)

            with open(element, 'w') as f:
                f.write('termite')

        sleep(0.01)


class TestFiles(TestCaseWithTmp):
    def test_simple_file_change(self):
        file_a = 'a.txt'
        self.modify(file_a)

        files = Files(file_a)

        self.assertFalse(files.changes())
        self.assertEqual(get_tuple(), files.get_changes())

        self.modify(file_a)
        self.assertTrue(files.changes())

        self.modify(file_a)
        self.assertEqual(get_tuple(m=file_a), files.get_changes())

    def test_glob_file_change(self):
        files_names = ['folder/a/a.txt', 'folder/b/b.txt', 'file.py']
        self.modify(files_names)

        files = Files('**/*.txt')

        self.modify(files_names[0])
        self.assertTrue(files.changes())

        self.modify(files_names[0])
        self.assertEqual(get_tuple(m=files_names[0]), files.get_changes())

    def test_file_deleted(self):
        files_names = ['folder/a/a.txt', 'folder/b/b.txt', 'file.py']
        self.modify(files_names)

        files = Files('**/*.txt')

        os.remove(files_names[0])
        self.assertTrue(files.changes())

        os.remove(files_names[1])
        self.assertEqual(get_tuple(d=files_names[1]), files.get_changes())

    def test_file_added(self):
        files_names = ['folder/a/a.txt', 'folder/b/b.txt', 'file.py']
        self.modify(files_names)

        files = Files('**/*.txt')

        self.modify('path/to/new/file.txt')
        self.assertTrue(files.changes())

        self.modify('a/b/c/a.txt')
        self.assertEqual(get_tuple(n='a/b/c/a.txt'), files.get_changes())

    def test_file_observer_nothing_found(self):
        files = Files('**/*.txt')
        self.assertFalse(files.changes())

    def test_file_change_but_not_watched(self):
        files_names = ['folder/a/a.txt', 'folder/b/b.txt', 'file.py']
        self.modify(files_names)

        files = Files('**/*.txt')

        self.modify(files_names[2])
        self.assertFalse(files.changes())

    def test_file_change_folder_observer(self):
        files_names = ['folder/a/a.txt', 'folder/b/b.txt', 'file.py']
        self.modify(files_names)

        files = Files('folder')

        self.modify(files_names[0])
        self.assertTrue(files.changes())

        self.modify(files_names[0])
        self.assertEqual(get_tuple(m=files_names[0]), files.get_changes())

    def test_file_added_folder_observer(self):
        files_names = ['folder/a/a.txt', 'folder/b/b.txt', 'file.py']
        self.modify(files_names)

        files = Files('folder')

        self.modify('folder/a.py')
        self.assertTrue(files.changes())

        self.modify('folder/b.py')
        self.assertEqual(get_tuple(n='folder/b.py'), files.get_changes())

    def test_file_deleted_folder_observer(self):
        files_names = ['folder/a/a.txt', 'folder/b/b.txt', 'file.py']
        self.modify(files_names)

        files = Files('folder')

        os.remove(files_names[0])
        self.assertTrue(files.changes())

        os.remove(files_names[1])
        self.assertEqual(get_tuple(d=files_names[1]), files.get_changes())

    def test_file_list_properly(self):
        files_names = {'folder/a/a.txt', 'folder/b/b.txt', 'folder/file.py',
                       'folder/v/e/r/y/d/e/e/p/f/i/l/e.txt'}
        self.modify(files_names)

        files = Files('folder')
        self.assertEqual(files_names, files.paths.keys())
