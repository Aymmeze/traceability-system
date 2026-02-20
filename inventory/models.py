from django.db import models

# --- MODEL 1: MATERIAŁ (Katalog) ---
class Material(models.Model):
    TYPE_CHOICES = [
        ('RAW', 'Surowiec'),
        ('PACK', 'Opakowanie'),
        ('PRODUCT', 'Wyrób Gotowy'),
    ]

    name = models.CharField(max_length=200, verbose_name="Nazwa Materiału")
    sku_code = models.CharField(max_length=50, unique=True, verbose_name="Kod SKU")
    material_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Typ")
    description = models.TextField(blank=True, verbose_name="Opis")
    
    def __str__(self):
        return f"[{self.sku_code}] {self.name}"

    class Meta:
        verbose_name = "Materiał"
        verbose_name_plural = "Materiały"


# --- MODEL 2: PARTIA (Konkretna seria) ---
class Batch(models.Model):
    STATUS_CHOICES = [
        ('QUARANTINE', 'Kwarantanna'),
        ('RELEASED', 'Zwolniony'),
        ('REJECTED', 'Odrzucony'),
    ]

    # To pole łączy Partię z Materiałem (Klucz Obcy)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Materiał")
    
    lot_number = models.CharField(max_length=50, unique=True, verbose_name="Numer Serii (LOT)")
    manufacturing_date = models.DateField(verbose_name="Data Produkcji")
    expiry_date = models.DateField(verbose_name="Data Ważności")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='QUARANTINE', verbose_name="Status Jakościowy")

    def __str__(self):
        return f"{self.lot_number} ({self.material.name})"

    class Meta:
        verbose_name = "Partia"
        verbose_name_plural = "Partie"

        # ... (Twój wcześniejszy kod Material i Batch zostaje bez zmian) ...

class Movement(models.Model):
    # Logika Traceability: Łączymy "Rodzica" z "Dzieckiem"
    
    # Z jakiej partii pobraliśmy? (np. Cukier)
    source_batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='used_in', verbose_name="Z Partii (Składnik)")
    
    # Do jakiej partii to trafiło? (np. Syrop)
    target_batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='consists_of', verbose_name="Do Partii (Produkt)")
    
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Zużyta Ilość")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Data Operacji")

    def __str__(self):
        return f"{self.source_batch.lot_number} -> {self.target_batch.lot_number}"

    class Meta:
        verbose_name = "Ruch / Zużycie"
        verbose_name_plural = "Traceability (Genealogia)"