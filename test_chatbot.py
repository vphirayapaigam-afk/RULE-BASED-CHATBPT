import unittest

from chatbot import FALLBACK, RESPONSES, get_reply, sanitize


class ChatbotTests(unittest.TestCase):
    def test_sanitize_handles_case_space_punctuation(self):
        self.assertEqual(sanitize("  HeLLo!!  "), "hello")
        self.assertEqual(sanitize("How   are you?"), "how are you")

    def test_known_intent(self):
        self.assertEqual(get_reply("hello"), RESPONSES["hello"])

    def test_fallback(self):
        self.assertEqual(get_reply("blah blah"), FALLBACK)

    def test_has_five_plus_intents(self):
        self.assertGreaterEqual(len(RESPONSES), 5)


if __name__ == "__main__":
    unittest.main()
