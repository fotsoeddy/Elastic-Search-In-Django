from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch
from .documents import BrandDocument, SupplierDocument, ProductDocument, CategoryDocument

def index(request):
    context = {}
    return render(request, 'index.html', context)

class SearchJsonView(View):
    def get(self, request):
        q = request.GET.get("q", "")
        results = {"products": [], "suppliers": [], "brands": [], "categories": [], "query": q}
        
        if q:
            query = MultiMatch(
                query=q,
                fields=['name', 'email', 'phone', 'description'],
                fuzziness='AUTO'
            )
            search = Search(index=['products', 'suppliers', 'brands', 'categories']).query(query)
            response = search.execute()
            
            for hit in response:
                item = {
                    "name": getattr(hit, "name", ""),
                    "description": getattr(hit, "description", ""),
                    "email": getattr(hit, "email", ""),
                    "phone": getattr(hit, "phone", ""),
                }
                if hit.meta.index == 'products':
                    results["products"].append(item)
                elif hit.meta.index == 'suppliers':
                    results["suppliers"].append(item)
                elif hit.meta.index == 'brands':
                    results["brands"].append(item)
                elif hit.meta.index == 'categories':
                    results["categories"].append(item)
        
        return JsonResponse(results)