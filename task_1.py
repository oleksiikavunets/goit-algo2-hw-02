import heapq
from collections import defaultdict
from copy import deepcopy
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

    def __lt__(self, other):
        return self.priority < other.priority and self.volume > other.volume


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


# Програма групує моделі для одночасного друку, не перевищуючи обмеження (10 б).
# Завдання з вищим пріоритетом виконуються раніше (10 б).
# Час друку групи моделей розраховується як максимальний час серед моделей у групі (10 б).
# Програма обробляє всі тестові сценарії (10 б):
# завдання однакового пріоритету,
# завдання різних пріоритетів,
# перевищення обмежень принтера.
# Код використовує dataclass для структур даних (10 б).

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """
    # Тут повинен бути ваш код
    print_order = []
    total_time = 0

    jobs = [PrintJob(**j) for j in print_jobs]
    printer_constraints = PrinterConstraints(**constraints)

    heapq.heapify(jobs)

    order_group = []

    def push_group():
        nonlocal total_time

        total_time += max(i.print_time for i in order_group)
        print_order.extend(i.id for i in order_group)
        order_group.clear()

    while len(jobs) > 0:
        job = heapq.heappop(jobs)

        if (len(order_group) >= printer_constraints.max_items or
                sum(i.volume for i in order_group) + job.volume > printer_constraints.max_volume):
            push_group()

        order_group.append(job)

    else:
        push_group()

    return {
        "print_order": print_order,
        "total_time": total_time
    }


# Тестування
def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # лабораторна
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # дипломна
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")

    print("\\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")

    print("\\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")


if __name__ == "__main__":
    test_printing_optimization()
