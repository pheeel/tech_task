import requests
import pytest


SUCCESS = 202
INCORRECT_PARAMS = 400
INCORRECT_HEADERS = 401
HEADERS = {
    "Valid": {
        "Content-Type": "application/json",
        "Authorization": "OAuth AgAAAAAE1P7UAADLW3JYZc32oEZBhJid6U-I3rk",
    },
    "Invalid": {"Content-Type": "application/json", "Authorization": "OAuth TEST"},
}
PARAMS = {
    "Valid": {"path": "/test", "url": "https://www.w3schools.com/w3css/img_lights.jpg"},
    "Invalid": {"path": "/", "url": "TEST"},
}


@pytest.mark.api
class TestUploadFileByURL:
    host = "cloud-api.yandex.net:443"
    command = "v1/disk/resources/upload"
    url = "https://{}/{}".format(host, command)

    def test_upload_file(self):
        response = requests.post(
            self.url, params=PARAMS["Valid"], headers=HEADERS["Valid"]
        )
        assert response.status_code == SUCCESS

    def test_upload_file_with_invalid_params(self):
        response = requests.post(
            self.url, params=PARAMS["Invalid"], headers=HEADERS["Valid"]
        )
        assert response.status_code == INCORRECT_PARAMS

    def test_upload_file_with_invalid_headers(self):
        response = requests.post(
            self.url, params=PARAMS["Valid"], headers=HEADERS["Invalid"]
        )
        assert response.status_code == INCORRECT_HEADERS
