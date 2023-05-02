from rest_framework import mixins

class CreateOnlyMixin(mixins.CreateModelMixin):
    http_method_names = ['post']

class ListOnlyMixin(mixins.ListModelMixin):
    http_method_names = ['get']