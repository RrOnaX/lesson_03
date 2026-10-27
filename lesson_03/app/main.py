import sys
from app.services.calculator import calculate_average, calculate_min, calculate_max
from app.utils.formatter import format_report
from rich.console import Console

def main():
    # Ожидаемый набор оценок из задания
    grades = [5, 4, 5, 3, 5]
    
    try:
        avg_score = calculate_average(grades)
        min_score = calculate_min(grades)
        max_score = calculate_max(grades)
        
        # Форматирование и вывод через Rich
        report = format_report(avg_score, min_score, max_score)
        console = Console()
        console.print(report)
        
    except ValueError as e:
        print(f"Ошибка при расчете: {e}")

if __name__ == "__main__":
    main()
