from django.db import models

# --- HABITACION ---
class Habitacion(models.Model):
    TIPOS = [
        ('simple', 'Simple'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
    ]
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('reservada', 'Reservada'),
        ('mantenimiento', 'En Mantenimiento'),
    ]
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    precio_por_noche = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='disponible')
    activo = models.BooleanField(default=True)  # False = dada de baja permanente

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo} - {self.estado}"


# --- HUESPED ---
class Huesped(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)  # False = dado de baja

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# --- RESERVA ---
class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('activa', 'Activa'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]
    huesped = models.ForeignKey(Huesped, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.huesped} - Hab {self.habitacion.numero}"


# --- HOUSEKEEPING ---
class Housekeeping(models.Model):
    ESTADOS = [
        ('limpia', 'Limpia'),
        ('sucia', 'Sucia'),
        ('en_mantenimiento', 'En Mantenimiento'),
    ]
    habitacion = models.OneToOneField(Habitacion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='limpia')
    ultima_limpieza = models.DateTimeField(auto_now=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Housekeeping - Hab {self.habitacion.numero} - {self.estado}"


# --- MANTENIMIENTO ---
class Mantenimiento(models.Model):
    TIPOS = [
        ('pintura', 'Pintura'),
        ('muebles', 'Cambio de Muebles'),
        ('iluminacion', 'Iluminación'),
        ('remodelaje', 'Remodelaje General'),
        ('reparacion', 'Reparación'),
        ('otro', 'Otro'),
    ]
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
    ]
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin_estimada = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    habitacion_disponible = models.BooleanField(default=False)

    def __str__(self):
        return f"Mantenimiento {self.tipo} - Hab {self.habitacion.numero}"
