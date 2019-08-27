import requests
import pytest

SUCCESS = 200
INVALID_PATH = 404

HEADERS = {
    "Valid": {
        "Content-Type": "application/json",
        "Authorization": "OAuth AgAAAAAE1P7UAADLW3JYZc32oEZBhJid6U-I3rk",
    },
    "Invalid": {"Content-Type": "application/json", "Authorization": "OAuth TEST"},
}

PARAMS = {"Valid": {"path": "/valid_path"}, "Invalid": {"path": "/invalid_path"}}


@pytest.mark.api
class TestResourcePublish:
    host = "cloud-api.yandex.net:443"
    command = "v1/disk/resources/publish"
    url = "https://{}/{}".format(host, command)

    def test_resource_publish(self):
        response = requests.put(
            self.url, params=PARAMS["Valid"], headers=HEADERS["Valid"]
        )
        assert response.status_code == SUCCESS

    def test_resource_publish_with_invalid_path(self):
        response = requests.put(
            self.url, params=PARAMS["Invalid"], headers=HEADERS["Valid"]
        )
        assert response.status_code == INVALID_PATH
