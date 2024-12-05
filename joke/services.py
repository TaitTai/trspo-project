import json

from requests import get, Response
from typing import Optional

from settings import JOKE_API_BASE_URL


def _parse_joke_response(joke_response: Response) -> tuple[str, str]:
    joke_dict: dict = json.loads(joke_response.text)

    return joke_dict["setup"], joke_dict["delivery"]


def get_joke(category: Optional[str] = None) -> tuple[str, str]:
    try:
        joke_response: Response = get(
            f"{JOKE_API_BASE_URL}/joke/{"Any" if not category else category}"
        )
        setup, delivery = _parse_joke_response(joke_response=joke_response)

    except Exception as exc:
        setup = "Knock-knock! Knock-knock who?"
        delivery = f"Knock-knock {exc}"

    return setup, delivery