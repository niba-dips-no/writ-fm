import unittest
from unittest.mock import patch

from mac import discogs_lookup, qr_generator


class DiscogsQrTests(unittest.TestCase):
    def test_discogs_lookup_disabled_without_credentials(self):
        with patch.object(discogs_lookup, "HAS_CREDENTIALS", False):
            self.assertIsNone(discogs_lookup.search_discogs("Track"))

    def test_discogs_lookup_expands_relative_release_url(self):
        payload = {
            "results": [{
                "id": 1,
                "title": "Artist - Title",
                "uri": "/release/1-title",
                "thumb": "https://img.example/thumb.jpg",
                "label": ["Label"],
                "format": ["LP"],
                "year": 1970,
            }]
        }
        with (
            patch.object(discogs_lookup, "HAS_CREDENTIALS", True),
            patch.object(discogs_lookup, "_request_json", return_value=payload),
        ):
            result = discogs_lookup.search_discogs("Artist - Title")

        self.assertIsNotNone(result)
        self.assertEqual(result.url, "https://www.discogs.com/release/1-title")

    def test_qr_data_url_when_qrcode_available(self):
        result = qr_generator.generate_qr_data_url("https://example.com")
        if qr_generator.HAS_QRCODE:
            self.assertTrue(result.startswith("data:image/png;base64,"))
        else:
            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
