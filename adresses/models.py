from django.db import models

class Address(models.Model):
    '''
        Сюда попадает адрес из формы оформления заказа и получает id.
        Этот id сразу же добавляется в Client.addresslist
    '''
    address = models.CharField(max_length=200, unique=True)

    def __str__(self):
        if len(str(self.address)) > 13:
            return '{}...'.format(self.address[:13])
        else:
            return self.address

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
