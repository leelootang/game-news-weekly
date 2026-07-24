from pathlib import Path
import sys
import unittest
from unittest.mock import patch


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from feishu_common import FeishuClient


class FeishuPermissionTests(unittest.TestCase):
    def test_public_permission_defaults_to_external_link_reading(self) -> None:
        client = FeishuClient("app-id", "app-secret")

        with patch.object(client, "_request", return_value={"code": 0}) as request:
            client.set_doc_public_permission("doc-token")

        request.assert_called_once_with(
            "PATCH",
            "/drive/v2/permissions/doc-token/public",
            {
                "external_access": True,
                "link_share_entity": "anyone_readable",
            },
            query={"type": "docx"},
        )


if __name__ == "__main__":
    unittest.main()
