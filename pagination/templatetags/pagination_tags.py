from django import template

register = template.Library()

def format_url(base_url, page_number):
    return '{0}page/{1}/'.format(base_url, page_number)

@register.inclusion_tag('pager.tmpl.html', takes_context=True)
def show_pager(context, adjacent_links=2, base_url='/'):

    page = context['current_page']

    # prev/next links
    if page.has_previous():
        previous_link = {
            'url': format_url(base_url, page.previous_page_number()),
            'title': 'Previous'
        }
    else:
        previous_link = False

    if page.has_next():
        next_link = {
            'url': format_url(base_url, page.next_page_number()),
            'title': 'Next'
        }
    else:
        next_link = False

    # run through the page range and make links for each page
    page_links = list()
    for i in page.paginator.page_range:
        if i == page.number:
            page_links.append({
                'is_link': False,
                'title': str(i)
            })
        else:
            page_links.append({
                'is_link': True,
                'url': format_url(base_url, i),
                'title': str(i)
            })

    # remove intermediate links on either side of the center grouping if needed
    current_page_index = page.number - 1
    slice_start = max(current_page_index - adjacent_links - 2, 0)
    slice_end = min(page.number + adjacent_links + 2, page.paginator.num_pages)
    center_group = page_links[slice_start:slice_end]

    # if we don't find the first or last elements at the end of the list
    # that means we need to add them and abbreviate the list with a separator
    if center_group[0]['title'] != '1':
        center_group[0] = page_links[0]
        center_group[1] = {'is_separator': True}

    if center_group[-1]['title'] != str(page.paginator.num_pages):
        center_group[-1] = page_links[-1]
        center_group[-2] = {'is_separator': True}

    return {
        'paginate': {
            'previous': previous_link,
            'current_page_number': str(page.number),
            'next': next_link,
            'parts': center_group
        }
    }

@register.inclusion_tag('prev_next.tmpl.html', takes_context=True)
def show_prev_next(context, base_url='/'):

    def get_item_url(item):
        if item:
            return '{0}{1}/'.format(base_url, item.slug)
        else:
            return False

    next_url = get_item_url(context['next_item'])
    previous_url = get_item_url(context['previous_item'])
    
    return {
        'previous_url': previous_url,
        'next_url': next_url,
        'verbose_name': context['verbose_name']
    }
    
