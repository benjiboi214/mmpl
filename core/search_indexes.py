from haystack import indexes
from core.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    subtitle = indexes.CharField(model_attr='subtitle')
    body = indexes.CharField(model_attr='body')

    def get_model(self):
        return Post
