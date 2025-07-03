import re
from collections import Counter
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """Фильтрует список банковских операций"""
    if not search or not data:
        return []
    try:
        pattern = re.compile(re.escape(search), re.IGNORECASE)
    except re.error:
        return []
    result = []
    for operation in data:
        if isinstance(operation, dict) and 'description' in operation:
            description = operation['description']
            if isinstance(description, str) and pattern.search(description):
                result.append(operation)
    return result


def process_bank_operations(data: List[Dict], categories: List[str], case_sensitive: bool = False) -> Dict[str, int]:
    """Подсчитывает количество операций по заданным категориям, используя Counter."""
    if not data or not categories:
        return {}
    search_categories = categories if case_sensitive else [c.lower() for c in categories]
    category_counter = Counter()
    for operation in data:
        if not isinstance(operation, dict):
            continue
        description = operation.get('description')
        if not isinstance(description, str):
            continue
        search_text = description if case_sensitive else description.lower()
        for i, category in enumerate(search_categories):
            if category in search_text:
                category_counter[categories[i]] += 1
    return dict(category_counter)
