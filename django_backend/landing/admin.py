from django.contrib import admin
from .models import Buyer, Seller, BulkOption, BulkProduct, Cart, SellerBackgroundPhoto, ProductCategory, ProductPhoto
# Register your models here.

#ProductPhoto inline BulkProduct admin panel
class ProductPhotoAdmin(admin.StackedInline):
    model = ProductPhoto
#SellerBackgroundPhoto inline Seller admin panel
class SellerBgPhotoAdmin(admin.StackedInline):
    model = SellerBackgroundPhoto
#Cart item inline cart admin panel
class CartAdmin(admin.StackedInline):
    model = Cart
#Seller registration
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    inlines = [SellerBgPhotoAdmin]

    class Meta:
        model = Seller
#Bulkproduct registration
@admin.register(BulkProduct)
class BulkProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoAdmin]

    class Meta:
        model = BulkProduct
#Buyer registration
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    inlines = [CartAdmin]

    class Meta:
        model = Buyer

admin.site.register(ProductCategory)
admin.site.register(BulkOption)
admin.site.register(Cart)
admin.site.register(SellerBackgroundPhoto)
admin.site.register(ProductPhoto)