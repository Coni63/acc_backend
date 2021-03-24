from ..domain.car import Car

def get_all_cars():
    return Car.objects.all()

def get_car_by_id(id: int):
    return Car.objects.get(pk=id)