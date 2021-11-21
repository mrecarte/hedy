import hedy
from test_level_01 import HedyTester
import hedy_translation


def check_local_lang_bool(func):
    def inner(self):
        if not hedy.local_keywords_enabled:
            return

        return func(self)

    return inner


    # tests should be ordered as follows:
    # * Translation from English to Dutch
    # * Translation from Dutch to English
    # * Translation to several languages
    # * Error handling


class TestsTranslationLevel2(HedyTester):
    level = 2

    def test_print(self):
        result = hedy_translation.translate_keywords("print Hallo welkom bij Hedy!", "nl", "en", self.level)
        expected = "print Hallo welkom bij Hedy!"

        self.assertEqual(result, expected)

    def test_print_multiple_lines(self):
        result = hedy_translation.translate_keywords("print Hallo welkom bij Hedy!\nprint veel plezier", "en", "nl", self.level)
        expected = "print Hallo welkom bij Hedy!\nprint veel plezier"

        self.assertEqual(result, expected)

    def test_print_kewords(self):
        result = hedy_translation.translate_keywords("print print ask echo", "en", "nl", self.level)
        expected = "print print ask echo"

    def test_ask_assign(self):
        result = hedy_translation.translate_keywords("mens is vraag Hallo welkom bij Hedy!", "nl", "en", self.level)
        expected = "mens is ask Hallo welkom bij Hedy!"

        self.assertEqual(result, expected)

    def test_ask_multiple_lines(self):
        result = hedy_translation.translate_keywords("welkom is ask Hallo welkom bij Hedy!\nplezier is ask veel plezier", "en", "nl", self.level)
        expected = "welkom is vraag Hallo welkom bij Hedy!\nplezier is vraag veel plezier"

        self.assertEqual(result, expected)

    def test_ask_kewords(self):
        result = hedy_translation.translate_keywords("hedy is vraag print ask echo", "en", "nl", self.level)
        expected = "hedy is vraag print ask echo"

        self.assertEqual(result, expected)

    def test_ask_print(self):
        result = hedy_translation.translate_keywords("hedy is hello\nprint hedy", "en", "nl", self.level)
        expected = "hedy is hello\nprint hedy"

        self.assertEqual(result, expected)

    def test_assign_list(self):
        result = hedy_translation.translate_keywords("mens is papa mama oma", "en", "nl", self.level)
        expected = "mens is papa mama oma"

        self.assertEqual(result, expected)

    def test_acces_list(self):
        result = hedy_translation.translate_keywords("mens is papa mama oma\nprint mens at random", "en", "nl", self.level)
        expected = "mens is papa mama oma\nprint mens opplek willekeurig"

        self.assertEqual(result, expected)

    def test_forward(self):
        result = hedy_translation.translate_keywords("forward 50", "en", "nl", self.level)
        expected = "vooruit 50"

        self.assertEqual(result, expected)

    def test_turn(self):
        result = hedy_translation.translate_keywords("turn left", "en", "nl", self.level)
        expected = "draai left"

        self.assertEqual(result, expected)

    def test_turn_value(self):
        result = hedy_translation.translate_keywords("turn 50", "en", "nl", self.level)
        expected = "draai 50"

        self.assertEqual(result, expected)

    def test_forward_assigned_value(self):
        result = hedy_translation.translate_keywords("value is 50\nforward value", "en", "nl", self.level)
        expected = "value is 50\nvooruit value"

        self.assertEqual(result, expected)

    def test_invalid(self):
        result = hedy_translation.translate_keywords("hallo", "en", "nl", self.level)
        expected = "hallo"

        self.assertEqual(result, expected)

    def test_invalid_space(self):
        result = hedy_translation.translate_keywords(" print Hedy", "en", "nl", self.level)
        expected = " print Hedy"

        self.assertEqual(result, expected)

    def no_argument_ask(self):
        result = hedy_translation.translate_keywords("ask", "en", "nl", self.level)
        expected = "vraag"

        self.assertEqual(result, expected)