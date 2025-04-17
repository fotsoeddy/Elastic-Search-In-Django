from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product, Category, Brand, Supplier

# Optional: define the index name
product_index = Index('products')
product_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
class ProductDocument(Document):
    category = fields.ObjectField(properties={
        'name': fields.TextField(),
    })
    brand = fields.ObjectField(properties={
        'name': fields.TextField(),
    })
    supplier = fields.ObjectField(properties={
        'name': fields.TextField(),
        'email': fields.TextField(),
        'phone': fields.TextField(),
    })

    class Index:
        name = 'products'  # The name of the Elasticsearch index

    class Django:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'stock',
            'created_at',
        ]

@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'categories'

    class Django:
        model = Category
        fields = [
            'name',
        ]

@registry.register_document
class BrandDocument(Document):
    class Index:
        name = 'brands'

    class Django:
        model = Brand
        fields = [
            'name',
            'logo',
        ]


@registry.register_document
class SupplierDocument(Document):
    class Index:
        name = 'suppliers'

    class Django:
        model = Supplier
        fields = [
            'name',
            'email',
            'phone',
        ]
