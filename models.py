from datetime import timezone
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories')
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True)
    tags = models.ManyToManyField('Tag', related_name='products', blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    discount_percentage = models.FloatField(default=0.0)
    discount_start_date = models.DateTimeField(blank=True, null=True)
    discount_end_date = models.DateTimeField(blank=True, null=True)
    stock = models.IntegerField()
    stock_alert_threshold = models.IntegerField(default=0)
    stock_alert_email = models.EmailField(blank=True, null=True)
    stock_alert_sms = models.CharField(max_length=20, blank=True, null=True)
    stock_alert_enabled = models.BooleanField(default=False)
    stock_alert_sent = models.BooleanField(default=False)
    stock_alert_sent_date = models.DateTimeField(blank=True, null=True)
    stock_alert_sent_count = models.IntegerField(default=0)
    stock_alert_sent_method = models.CharField(max_length=50, choices=[('email', 'Email'), ('sms', 'SMS')], default='email')
    stock_alert_sent_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('sent', 'Sent'), ('failed', 'Failed')], default='pending')
    stock_alert_sent_message = models.TextField(blank=True, null=True)
    stock_alert_sent_message_date = models.DateTimeField(blank=True, null=True)
    stock_alert_sent_message_count = models.IntegerField(default=0)
    stock_alert_sent_message_method = models.CharField(max_length=50, choices=[('email', 'Email'), ('sms', 'SMS')], default='email')
    stock_alert_sent_message_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('sent', 'Sent'), ('failed', 'Failed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products_created', blank=True, null=True)
    updated_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products_updated', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products_deleted', blank=True, null=True)
    deleted_reason = models.TextField(blank=True, null=True)
    deleted_method = models.CharField(max_length=50, choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='manual')
    deleted_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('deleted', 'Deleted'), ('failed', 'Failed')], default='pending')
    archived = models.BooleanField(default=False)
    archived_at = models.DateTimeField(blank=True, null=True)   
    archived_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products_archived', blank=True, null=True)
    archived_reason = models.TextField(blank=True, null=True)
    archived_method = models.CharField(max_length=50, choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='manual')
    archived_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('archived', 'Archived'), ('failed', 'Failed')], default='pending')
    def __str__(self):
        return self.name
    
    def get_discounted_price(self):
        if self.is_discounted and self.discount_start_date <= timezone.now() <= self.discount_end_date:
            return self.price - (self.price * (self.discount_percentage / 100))
        return self.price
    def get_stock_status(self):
        if self.stock <= self.stock_alert_threshold:
            return 'Low Stock'
        return 'In Stock'
    
    def get_stock_alert_message(self):
        if self.stock_alert_enabled and self.stock <= self.stock_alert_threshold:
            if self.stock_alert_sent_method == 'email':
                return f"Low stock alert for {self.name}. Current stock: {self.stock}."
            elif self.stock_alert_sent_method == 'sms':
                return f"Low stock alert for {self.name}. Current stock: {self.stock}."
        return None
    

    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    def __str__(self):
        return f"Order of {self.product.name} on {self.order_date}"
    
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    orders = models.ManyToManyField(Order, related_name='customers', blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Review for {self.product.name} by {self.customer.first_name}"
    
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    products = models.ManyToManyField(Product, related_name='carts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Cart for {self.customer.first_name} {self.customer.last_name}"
    
    
class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='wishlists')
    products = models.ManyToManyField(Product, related_name='wishlists', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Wishlist for {self.customer.first_name} {self.customer.last_name}"
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')])
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Payment of {self.amount} for Order {self.order.id}"
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shipping_addresses')
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Shipping Address for {self.customer.first_name} {self.customer.last_name}"
    
class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.code
    
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, related_name='suppliers', blank=True)
    def __str__(self):
        return self.name
    
    
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Inventory for {self.product.name} at {self.location}"
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, related_name='tags', blank=True)
    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, related_name='brands', blank=True)
    def __str__(self):
        return self.name
    
    
class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='review_comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Comment on {self.review.product.name} by {self.customer.first_name}"
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Image for {self.product.name}"
    

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Variant of {self.product.name} - {self.name}"
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='product_reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Review for {self.product.name} by {self.customer.first_name}"
    
    
    
    def __str__(self):
        return self.name