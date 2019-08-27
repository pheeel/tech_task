VALID_PATH_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "antivirus_status": {
      "type": "string"
    },
    "size": {
      "type": "integer"
    },
    "comment_ids": {
      "type": "object",
      "properties": {
        "private_resource": {
          "type": "string"
        },
        "public_resource": {
          "type": "string"
        }
      },
      "required": [
        "private_resource",
        "public_resource"
      ]
    },
    "name": {
      "type": "string"
    },
    "exif": {
      "type": "object"
    },
    "created": {
      "type": "string"
    },
    "resource_id": {
      "type": "string"
    },
    "modified": {
      "type": "string"
    },
    "mime_type": {
      "type": "string"
    },
    "file": {
      "type": "string"
    },
    "media_type": {
      "type": "string"
    },
    "preview": {
      "type": "string"
    },
    "path": {
      "type": "string"
    },
    "sha256": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "md5": {
      "type": "string"
    },
    "revision": {
      "type": "integer"
    }
  },
  "required": [
    "antivirus_status",
    "size",
    "comment_ids",
    "name",
    "exif",
    "created",
    "resource_id",
    "modified",
    "mime_type",
    "file",
    "media_type",
    "preview",
    "path",
    "sha256",
    "type",
    "md5",
    "revision"
  ]
}

INVALID_PATH_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "error": {
      "type": "string"
    }
  },
  "required": [
    "message",
    "description",
    "error"
  ]
}