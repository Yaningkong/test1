from haystack import indexes
from .models import Text    # 需要建立索引的数据

class TextIndex(indexes.SearchIndex, indexes.Indexable):# 这里的类名也是固定的，索引的模型名+Index,继承也是固定的
    """
    索引模型类
    """
    # text表示被查询的字段，用户搜索的是这些字段的值，具体被索引的字段写在另一个文件里。
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(model_attr="id")

    content = indexes.CharField(model_attr="content")

    def get_model(self):
        """

        :return: 返回建立索引的模型类
        """

        return Text

    def index_queryset(self, using=None):
        """

        :param using:
        :return: 返回要建立索引的数据库查询集
        """

        return self.get_model().objects.all()
