import csv
from datetime import datetime
from django.http.response import JsonResponse
from django.views import View


class PurchaseOderView(View):

    def filter_by_year(self, data, year):
        results = []
        if not year:
            return results
        try:
            year = int(year)
        except Exception:
            return results
        if not (1111 <= year <= 9999):
            return results
        for product in data:
            product_date = product["date"]
            product_date_obj = datetime.strptime(product_date, "%Y-%m-%d")
            if product_date_obj.year == year:
                results.append(product)
        return results

    def filter_by_product(self, data, name):
        results = []
        if not name:
            return results
        for product_obj in data:
            product_name = product_obj["product"]
            if product_name == name:
                results.append(product_obj)
        return results

    def filter_by_supplier(self, data, name):
        results = []
        if not name:
            return results
        for product_obj in data:
            supplier_name = product_obj["supplier"]
            if supplier_name == name:
                results.append(product_obj)
        return results

    def fetch_data(self, action="list"):
        products = []
        with open('assignment/purchase-orders.csv', mode='r') as purchase_orders_file:
            reader = csv.DictReader(purchase_orders_file)
            for row in reader:
                product = {
                    "date": row["Date"],
                    "supplier": row["Supplier"],
                    "orderNumber": row["Order number"],
                    "product": row["Product"],
                }
                price_per_100_grams = float(row.get("Price per 100 grams", 0.0))
                price_per_1_kg = price_per_100_grams * 10
                price_per_tonne = price_per_1_kg * 1000
                quantity_in_kg = float(row.get("Quantity in kg", 0.0))
                quantity_in_tonne = float(quantity_in_kg / 1000)
                product['pricePerTonne'] = round(price_per_tonne, 3)
                products.append(product)
        product_averages_details = {}
        if action == "average-product-price-per-year":
            for product in products:
                name = product["product"]
                year = datetime.strptime(product['date'], "%Y-%m-%d").year
                key = f"{name}_{year}"
                price_per_tonne = product['pricePerTonne']
                if key not in product_averages_details:
                    product_averages_details[key] = [price_per_tonne]
                else:
                    product_averages_details[key].append(price_per_tonne)

            for product in products:
                name = product["product"]
                year = datetime.strptime(product['date'], "%Y-%m-%d").year
                key = f"{name}_{year}"
                total_list = product_averages_details.get(key)
                product["averagePricePerTonne"] = round(sum(total_list) / len(total_list), 3)

        return products

    def get(self, request, *args, **kwargs):
        action = request.GET.get('action')
        year = request.GET.get('year')
        product = request.GET.get('product')
        supplier = request.GET.get('supplier')

        data = self.fetch_data(action=action)
        if year is not None:
            data = self.filter_by_year(data, year)
        if product is not None:
            data = self.filter_by_product(data, product)
        if supplier is not None:
            data = self.filter_by_supplier(data, supplier)

        sorted_data = sorted(data, key=lambda i: (i["date"], i["product"]), reverse=True)
        response = {"data": sorted_data}
        return JsonResponse(data=response, status=200)




