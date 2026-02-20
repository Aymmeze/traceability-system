from django.shortcuts import render
from .models import Batch, Movement

def traceability_search(request):
    query = request.GET.get('lot')  # Pobieramy nr LOT z paska wyszukiwania
    batch = None
    ingredients = []  # Tu będą składniki (Co weszło DO środka?)
    products = []     # Tu będą produkty (Gdzie to poszło DALEJ?)

    if query:
        try:
            # 1. Szukamy partii po numerze LOT
            batch = Batch.objects.get(lot_number=query)
            
            # 2. Szukamy składników (Genealogia Wstecz - Backward)
            # Szukamy ruchów, gdzie nasza partia jest "Celem" (Target), czyli powstała z czegoś
            ingredients_movements = Movement.objects.filter(target_batch=batch)
            for m in ingredients_movements:
                ingredients.append({
                    'lot': m.source_batch.lot_number,
                    'name': m.source_batch.material.name,
                    'qty': m.quantity
                })

            # 3. Szukamy użycia (Genealogia W przód - Forward)
            # Szukamy ruchów, gdzie nasza partia jest "Źródłem" (Source), czyli została zużyta
            products_movements = Movement.objects.filter(source_batch=batch)
            for m in products_movements:
                products.append({
                    'lot': m.target_batch.lot_number,
                    'name': m.target_batch.material.name,
                    'qty': m.quantity
                })

        except Batch.DoesNotExist:
            batch = None

    return render(request, 'inventory/report.html', {
        'batch': batch,
        'query': query,
        'ingredients': ingredients,
        'products': products
    })