from functools import wraps
from typing import Callable, Any, Optional
from datetime import datetime
import time


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования функций:
    1) Логирует начало и конец выполнения
    2) Измеряет время работы
    3) Логирует ошибки с входными параметрами
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            params = f"args: {args}, kwargs: {kwargs}"
            start_time = time.time()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            start_msg = f"[{timestamp}] {func.__name__} started. {params}\n"

            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(start_msg)
            else:
                print(start_msg, end="")

            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                success_msg = (
                    f"[{timestamp}] {func.__name__} finished in {duration:.2f}s. "
                    f"Result: {result}\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_msg)
                else:
                    print(success_msg, end="")

                return result

            except Exception as e:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                error_msg = (
                    f"[{timestamp}] {func.__name__} failed with {type(e).__name__}: "
                    f"{str(e)}. {params}\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_msg)
                else:
                    print(error_msg, end="")

                raise

        return wrapper
    return decorator
