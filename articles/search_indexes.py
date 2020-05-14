from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/article_text.txt')
    body = indexes.CharField(model_attr='body')
    title = indexes.CharField(model_attr='title')
    
    def get_model(self):
        return Article
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
