class TestExample:
    def test_chek_math(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a + b == expected_sum, f"Сумма переменных А и В не равна {expected_sum}"

    def test_chek_math2(self):
        a = 5
        b = 11
        expected_sum = 14
        assert a+b == expected_sum, f"Сумма переменных А и В не равна {expected_sum}"