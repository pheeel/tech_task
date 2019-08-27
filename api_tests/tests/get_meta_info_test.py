import requests
import pytest
from jsonschema import validate
from api_tests.schemas.meta_info import *

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
class TestGetMetaInfo:
    host = "cloud-api.yandex.net:443"
    command = "v1/disk/resources"
    url = "https://{}/{}".format(host, command)

    def test_get_of_meta_info(self):
        response = requests.get(
            self.url, params=PARAMS["Valid"], headers=HEADERS["Valid"]
        )
        assert response.status_code == SUCCESS
        validate(response.json(), VALID_PATH_SCHEMA)

    def test_get_of_meta_info_with_invalid_path(self):
        response = requests.get(
            self.url, params=PARAMS["Invalid"], headers=HEADERS["Valid"]
        )
        assert response.status_code == INVALID_PATH
        validate(response.json(), INVALID_PATH_SCHEMA)
