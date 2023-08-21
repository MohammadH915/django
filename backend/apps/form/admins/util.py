from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget


class InputFilter(admin.SimpleListFilter):
    template = 'input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

class CustomAdminDateWidget(AdminDateWidget):
    def __init__(self, attrs=None, format=None):
        if attrs is None:
            attrs = {}
        attrs.update({'autocomplete': 'off', 'class': 'vDateField'})
        super().__init__(attrs=attrs, format=format)

