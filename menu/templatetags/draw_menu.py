from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    all_items = list(
        MenuItem.objects
        .filter(menu__name=menu_name)
        .select_related('parent')
    )

    active_item = next((item for item in all_items if item.get_absolute_url() == current_path), None)

    active_path_ids = set()
    if active_item:
        parent = active_item
        while parent:
            active_path_ids.add(parent.id)
            parent = parent.parent

    def build_tree(parent=None):
        branch = []
        for item in all_items:
            if item.parent_id == (parent.id if parent else None):
                is_active_branch = item.id in active_path_ids
                should_expand = is_active_branch or (parent and parent.id in active_path_ids)
                children = build_tree(item) if should_expand else []
                branch.append({
                    'item': item,
                    'children': children,
                    'is_active': item == active_item,
                    'is_open': is_active_branch,
                })
        return branch

    return {
        'menu_items': build_tree(),
        'current_path': current_path,
    }
