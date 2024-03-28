class TestInput:
    def test_input_phrase(self):
        phrase = input("Введите фразу короче 15 символов: ")
        max_len = 15
        assert len(phrase) < max_len, f"Введенная фраза длинее {max_len} символов"