# tests/test_task_manager.py
import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()

    def test_add_task(self):
        self.tm.add_task("Buy groceries")
        self.assertEqual(len(self.tm.tasks), 1)
        self.assertEqual(self.tm.tasks[0]['title'], "Buy groceries")

    def test_complete_task(self):
        self.tm.add_task("Read book")
        self.tm.complete_task(0)
        self.assertTrue(self.tm.tasks[0]['completed'])

    def test_delete_task(self):
        self.tm.add_task("Walk dog")
        self.tm.delete_task(0)
        self.assertEqual(len(self.tm.tasks), 0)

if __name__ == '__main__':
    unittest.main()