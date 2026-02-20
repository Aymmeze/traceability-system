from django.contrib import admin
from .models import Material, Batch

# Konfiguracja widoku Materiałów
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('sku_code', 'name', 'material_type')
    search_fields = ('name', 'sku_code')
    list_filter = ('material_type',)

# Konfiguracja widoku Partii
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('lot_number', 'material', 'status', 'expiry_date')
    list_filter = ('status', 'material')
    search_fields = ('lot_number',)

    # ... (Wcześniejszy kod zostaje) ...
from .models import Material, Batch, Movement  # <--- WAŻNE: Dopisz Movement do importu na górze!

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'source_batch', 'quantity', 'target_batch')
    list_filter = ('timestamp',)
    # Dzięki temu w adminie będziesz mógł szukać po numerach serii
    search_fields = ('source_batch__lot_number', 'target_batch__lot_number')