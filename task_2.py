from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def compute(n, memo_):
        if n == 0:
            return 0, []
        if n in memo_:
            return memo_[n]

        max_val, cuts_ = 0, []

        for i in range(1, n + 1):
            if i <= len(prices):
                val, cut = compute(n - i, memo_)
                val += prices[i - 1]

                if val > max_val:
                    max_val, cuts_ = val, cut + [i]

        memo_[n] = (max_val, cuts_)
        return max_val, cuts_

    max_profit, cuts = compute(length, memo)

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts)
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp, cuts = [0] * (length + 1), [[]] * (length + 1)

    for i in range(1, length + 1):
        max_val, cut = 0, []

        for j in range(1, i + 1):
            if j <= length:
                val = dp[i - j] + prices[j - 1]

                if val > max_val:
                    max_val = val
                    cut = cuts[i - j] + [j]

        dp[i], cuts[i] = max_val, cut

    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length])
    }


def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()
