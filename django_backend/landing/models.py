from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seller(models.Model):
    """Seller's profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(default='seller_logo/default.jpg',  
                                     upload_to='seller_logo')
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    about = models.CharField(max_length=250)
    business_phone = models.CharField(max_length=20)
    rating = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.user.username} Seller-Profile'

class ProductCategory(models.Model):
    """Product Category"""
    name = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.name}'

class BulkProduct(models.Model):
    """Bulk Product"""
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, blank=True)
    about = models.CharField(max_length=250, null=True)
    rating = models.PositiveIntegerField()

class BulkOption(models.Model):
    """Buik purchase option"""
    product = models.ForeignKey(BulkProduct, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    amount_saved = models.PositiveIntegerField()
    amount_off = models.PositiveIntegerField()
    purchases = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()


class Buyer(models.Model):
    """Buyer's profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='buyer_pic/default.jpg',  
                                     upload_to='profile_pics')
    address = models.CharField(max_length=30, null=True)
    lga = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    about = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=20)
    wallet = models.PositiveIntegerField()
    buyer_cart = models.ManyToManyField(BulkOption, blank=True, through='Cart', related_name='buyer_cart')
    buyer_pool = models.ManyToManyField(BulkOption, blank=True, through='Pool', related_name='buyer_pool')
    saved_options = models.ManyToManyField(BulkOption, blank=True, through='Saved', related_name='save_for_later')
    def __str__(self):
        return f'{self.user.username} Buyer-Profile'

class Pool(models.Model):
    """Bulk product pool"""
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    bulkoption = models.ForeignKey(BulkOption, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    class Meta:
        unique_together = ('buyer', 'bulkoption')

class SellerBackgroundPhoto(models.Model):
    """Seller's background photo"""
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    background_photo = models.ImageField(default='background_photos/default.jpg',  
                                     upload_to='background_photos')

class ProductPhoto(models.Model):
    """Product's photo"""
    product = models.ForeignKey(BulkProduct, on_delete=models.CASCADE)
    background_photo = models.ImageField(default='product_photos/default.jpg',  
                                     upload_to='product_photos')
                        
class Cart(models.Model):
    """Buyer's Cart"""
    buyer = models.ForeignKey(Buyer,  on_delete=models.PROTECT)
    bulkoption = models.ForeignKey(BulkOption, on_delete=models.PROTECT)
    added_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    class Meta:
        unique_together = ('buyer', 'bulkoption')

class Saved(models.Model):
    """Buyer's saved product options"""
    saver = models.ForeignKey(Buyer,  on_delete=models.PROTECT)
    bulkoption = models.ForeignKey(BulkOption, on_delete=models.PROTECT)
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('saver', 'bulkoption')

PURCHASE_STAGES = (('Pooling', 'Pooling'), ('Pending', 'Pending'), ('In_transit', 'In_transit'), ('delivered', 'delivered'))
class Purchase(models.Model):
    """Buyer's Purchase item"""
    buyer = models.ForeignKey(Buyer,  on_delete=models.PROTECT)
    bulkoption = models.ForeignKey(BulkOption, on_delete=models.PROTECT)
    purchase_stage = models.CharField(choices=PURCHASE_STAGES, max_length=11)
    pooled_at = models.DateTimeField(auto_now_add=True)
    pending_at = models.DateTimeField(auto_now_add=True)
    in_transit_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(auto_now_add=True)

class CustomerFeedback(models.Model):
    """Feedback from buyer to seller"""
    feedback = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)