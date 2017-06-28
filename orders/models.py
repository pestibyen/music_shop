from django.db import models
from products.models import Product
from profiles.models import Profile

class Order(models.Model):
    user = models.ForeignKey(Profile)
    orderstartdate = models.DateTimeField(auto_now_add=True)
    orderenddate = models.DateTimeField(auto_now=True)

    ORDER_OPEN = 'Open'
    ORDER_DONE = 'Done'
    ORDER_CANCELED = 'Canceled'

    options = (
        (ORDER_OPEN, 'Open'),
        (ORDER_DONE, 'Done'),
        (ORDER_CANCELED, 'Canceled'),
    )
    status = models.CharField(max_length=14, choices=options,
                              default=ORDER_OPEN)

    # При изменении Order.status на Done или Canceled автоматически
    # расчитывается сумма всего заказа и сохраняется в ordercost.
    # Реализовано с помощь Trigger Function SAVECOST() в БД.
    ordercost = models.DecimalField(max_digits=8, decimal_places=2,
                                    default=0, editable=False)

    def __str__(self):
        if self.status == 'Open':
            return '{0.id}: {0.status}'.format(self)
        else:
            return '{0.id}: {0.status} = {0.ordercost}'.format(self)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{0.id}: {1.name} x {2.quantity}'.format(self.order, self.product, self)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
