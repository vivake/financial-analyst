import unittest
from databases.vector_db.connect_to_vector_db import VectorDBConnection

# Tests for database interactions

#Unit tests for the VectorDBConnection class
class TestVectorDBConnection(unittest.TestCase):

    def setUp(self):
        self.db = VectorDBConnection()
        self.db.connect()

    def tearDown(self):
        self.db.disconnect()

    def test_connection(self):
        self.assertTrue(self.db.is_connected())

    def test_insert_data(self):
        data = {"id": 1, "value": "test"}
        self.db.insert(data)
        result = self.db.query({"id": 1})
        self.assertEqual(result, data)

    def test_query_data(self):
        data = {"id": 2, "value": "query_test"}
        self.db.insert(data)
        result = self.db.query({"id": 2})
        self.assertEqual(result, data)

    def test_update_data(self):
        data = {"id": 3, "value": "update_test"}
        self.db.insert(data)
        updated_data = {"id": 3, "value": "updated_value"}
        self.db.update(updated_data)
        result = self.db.query({"id": 3})
        self.assertEqual(result, updated_data)

    def test_delete_data(self):
        data = {"id": 4, "value": "delete_test"}
        self.db.insert(data)
        self.db.delete({"id": 4})
        result = self.db.query({"id": 4})
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
    # The following code runs the unit tests when the script is executed directly.
    # It calls unittest.main() which discovers and runs all the test cases defined in the script.

