from django import template
from urllib import quote

register = template.Library()
@register.inclusion_tag('paginator.html', takes_context=True)

def paginator(context, adjacent_pages=2):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """

    if context.has_key('is_paginated'):
        page_obj=context['page_obj']
        paginator=page_obj.paginator
        page_numbers = [n for n in \
                        range(page_obj.number - adjacent_pages, page_obj.number + adjacent_pages + 1) \
                        if n > 0 and n <= paginator.num_pages]
        results_this_page = context['object_list'].count()
        range_base = ((page_obj.number - 1) * paginator.per_page)
        if len(page_numbers)<=1:
            page_numbers=[]

        r= {
                'hits': paginator.count,
                'results_per_page': paginator.per_page,
                'results_this_page': results_this_page,
                'first_this_page': range_base + 1,
                'last_this_page': range_base + results_this_page,
                'page': page_obj.number,
                'pages': paginator.num_pages,
                'page_numbers': page_numbers,
                'next': page_obj.next_page_number,
                'previous': page_obj.previous_page_number,
                'has_next': page_obj.has_next(),
                'has_previous': page_obj.has_previous(),
                'show_first': 1 not in page_numbers,
                'show_last': paginator.num_pages not in page_numbers,
                }

        if context.has_key('search_term'):
            r['search_term']=quote(context['search_term'],'')

        return r
