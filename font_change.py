import requests


def transform_text(text: str, slug: str = "monospace", update_stats: bool = True) -> str:
    url = "https://fancytextdecorator.com/api.php"

    data = {
        "action": "generate",
        "slug": slug,
        "text": text,
        "update_stats": str(update_stats).lower()
    }

    response = requests.post(url, data=data, timeout=10)
    response.raise_for_status()

    result = response.json()

    if not result.get("success"):
        raise Exception("Text transformation failed")

    return result["output"]


# # Example
# text = "Hello World"
# fancy_text = transform_text(text, "aesthetic")

# print(fancy_text)