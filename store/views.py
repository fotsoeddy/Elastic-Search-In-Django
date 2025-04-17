from django.shortcuts import render
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch
from .documents import BrandDocument, SupplierDocument, ProductDocument, CategoryDocument

def index(request):
    q = request.GET.get("q")
    context = {}
    
    if q:
        # Define the multi-match query
        query = MultiMatch(
            query=q,
            fields=['name', 'email', 'phone', 'description'],
            fuzziness='AUTO'
        )
        
        # Create a multi-index search
        search = Search(index=['products', 'suppliers', 'brands', 'categories']).query(query)
        
        # Execute the search
        response = search.execute()
        
        # Organize results by document type
        products = []
        suppliers = []
        brands = []
        categories = []
        
        for hit in response:
            if hit.meta.index == 'products':
                products.append(hit)
            elif hit.meta.index == 'suppliers':
                suppliers.append(hit)
            elif hit.meta.index == 'brands':
                brands.append(hit)
            elif hit.meta.index == 'categories':
                categories.append(hit)
        
        # Add results to context
        context.update({
            'products': products,
            'suppliers': suppliers,
            'brands': brands,
            'categories': categories,
            'query': q
        })
    
    return render(request, 'index.html', context)