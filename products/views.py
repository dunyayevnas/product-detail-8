from django.views.generic import ListView, DetailView

from products.models import ProductModel, ProductCategoryModel, ProductManufacture, ProductColor, ProductTagModel, \
    ProductSizeModel


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        qs = ProductModel.objects.all().order_by('-pk')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        man = self.request.GET.get('man')
        col = self.request.GET.get('col')

        if cat:
            qs = qs.filter(categories__in=cat)
        if tag:
            qs = qs.filter(tags__in=tag)
        if man:
            qs = qs.filter(manufacture__in=man)
        if col:
            qs = qs.filter(color__in=col)

        return qs



    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['categories'] = ProductCategoryModel.objects.all()
        content['manufacture'] = ProductManufacture.objects.all()
        content['color'] = ProductColor.objects.all()
        content['tags'] = ProductTagModel.objects.all()

        return content


class ProductDetailView(DetailView):
    template_name = 'products/products-detail.html'
    model = ProductModel
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['product'] = ProductModel.objects.all()
        content['tags'] = ProductTagModel.objects.all()
        content['categories'] = ProductCategoryModel.objects.all()
        content['color'] = ProductColor.objects.all()
        content['manufacture'] = ProductManufacture.objects.all()

        return content
