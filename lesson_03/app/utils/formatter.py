from rich.text import Text

def format_report(average, min_val, max_val):
    """Форматирует отчет с использованием стилей библиотеки Rich"""
    text = Text()
    text.append("Средний результат: ", style="bold cyan")
    text.append(f"{average:.2f}\n", style="bold green")
    text.append("Минимальная оценка: ", style="bold cyan")
    text.append(f"{min_val}\n", style="bold yellow")
    text.append("Максимальная оценка: ", style="bold cyan")
    text.append(f"{max_val}", style="bold magenta")
    return text
