from rest_framework.test import APITestCase
from rest_framework import status


class DefectCreationTestCase(APITestCase):
    def test_location_creation(self):
        data = {"defect_name": "test name", "defect_description": "test description", "defect_status": 0, "defect_location": 1, "defect_respondent": 1, "reporter": 1}
        response = self.client.get("/api/defects-detail/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

