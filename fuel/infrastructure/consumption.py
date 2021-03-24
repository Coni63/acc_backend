from ..domain.consumption import Consumption, CustomConsumption


def get_generic_consumption(car, track):
    return Consumption.objects.all().filter(track=track, car=car)

def get_custom_consumption(car, track, user):
    return CustomConsumption.objects.filter(track=track, car=car, user=user)

def create_custom_consumption(car, track, user, fuel):
    instance = CustomConsumption(car=car, track=track, user=user, fuel=fuel)
    instance.save()
    return instance

def update_custom_consumption(id, fuel):
    instance = CustomConsumption.objects.get(id=id)
    instance.fuel = fuel
    instance.save()
    return instance