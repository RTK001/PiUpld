from django.db import models

class BulkQueryMixin(object):
    def delete(self):
        for obj in self.all():
            obj.delete()

class BulkQuerySet(BulkQueryMixin, models.query.QuerySet):
    pass

class BulkQueryManager(BulkQueryMixin, models.Manager):
    def get_query_set(self):
        return BulkQuerySet(self.model, using=self._db)
