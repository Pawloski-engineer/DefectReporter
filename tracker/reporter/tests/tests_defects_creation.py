from rest_framework.test import APITestCase
from rest_framework import status


class DefectCreationTestCase(APITestCase):
    def test_defects_creation(self):
        data = {"location_name": "test name", "parent_location": "abs", "location_user_group": 1, "location_admin": 1}
        # data = {"location_name": "test name", "location_user_group": 1, "location_admin": 1}
        response = self.client.get("/api/defects-detail/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

