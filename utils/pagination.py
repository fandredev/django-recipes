import math

from typing import Sequence
from django.http import HttpRequest
from django.core.paginator import Paginator

# Generate SECRET_KEY VARIABLE (use this command in terminal inside environment and and i'm together)

# python -c
# "import string as s;from random import SystemRandom as sr;print(''.join(sr().choices(s.ascii_letters + s.punctuation, k=64)))"


def make_pagination_range(
    page_range: Sequence[int],
    qty_pages: int,
    current_page,
):
    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range > total_pages:
        start_range = start_range - abs(stop_range - total_pages)

    pagination = page_range[start_range:stop_range]

    return {
        "pagination": pagination,
        "page_range": page_range,
        "qty_pages": qty_pages,
        "current_page": current_page,
        "total_pages": total_pages,
        "start_range": start_range,
        "stop_range": stop_range,
        "first_page_out_of_range": current_page > middle_range,
        "last_page_out_of_range": stop_range < total_pages,
    }


def make_pagination(
    request: HttpRequest,
    queryset,
    quantity_per_page: int,
    quantity_pages: int = 4,
):
    try:
        current_page = int(request.GET.get("page", 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(queryset, quantity_per_page)
    page_object = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=paginator.page_range,
        qty_pages=quantity_pages,
        current_page=current_page,
    )

    return page_object, pagination_range
