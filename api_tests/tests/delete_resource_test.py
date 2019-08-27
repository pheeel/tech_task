import requests
import pytest
import time

SUCCESS = 204
SUCCESS_ASYNC = 202
INVALID_PATH = 404
HEADERS = {
    "Valid": {
        "Content-Type": "application/json",
        "Authorization": "OAuth AgAAAAAE1P7UAADLW3JYZc32oEZBhJid6U-I3rk",
    },
    "Invalid": {"Content-Type": "application/json", "Authorization": "OAuth TEST"},
}
PARAMS_TO_UPLOAD = {
    "path": "/file_to_delete",
    "url": "https://www.w3schools.com/w3css/img_lights.jpg",
}
PARAMS_TO_DELETE = {
    "Valid": {"path": "/file_to_delete"},
    "Invalid": {"path": "/invalid_path"},
}
PARAMS_TO_DELETE_ASYNCHRONOUSLY = {"path": "/file_to_delete", "force_async": True}


@pytest.mark.api
class TestDeleteResource:
    host = "cloud-api.yandex.net:443"
    command = "v1/disk/resources"
    url = "https://{}/{}".format(host, command)

    @pytest.fixture(scope="function", autouse=True)
    def create_a_file_for_removal(self):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        requests.post(url, params=PARAMS_TO_UPLOAD, headers=HEADERS["Valid"])
        # Need to wait until the file is created, otherwise the deletion will refer to a non-existing file.
        time.sleep(3)

    def test_delete_resource(self):
        response = requests.delete(
            self.url, params=PARAMS_TO_DELETE["Valid"], headers=HEADERS["Valid"]
        )
        assert response.status_code == SUCCESS

    def test_delete_resource_async(self):
        response = requests.delete(
            self.url, params=PARAMS_TO_DELETE_ASYNCHRONOUSLY, headers=HEADERS["Valid"]
        )
        assert response.status_code == SUCCESS_ASYNC


class TestDeleteResourceWithInvalidPath:
    host = "cloud-api.yandex.net:443"
    command = "v1/disk/resources"
    url = "https://{}/{}".format(host, command)

    def test_resource_deletion_with_invalid_path(self):
        response = requests.delete(
            self.url, params=PARAMS_TO_DELETE["Invalid"], headers=HEADERS["Valid"]
        )
        assert response.status_code == INVALID_PATH
