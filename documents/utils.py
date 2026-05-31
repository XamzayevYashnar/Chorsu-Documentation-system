class DataMixin:
    def get_context_user(self, cat=None, **kwargs):
        context = kwargs
        if not cat:
            context['cat_selected'] = 0
        else:
            context['cat_selected'] = cat

        return context