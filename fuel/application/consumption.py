from ..infrastructure.consumption import get_generic_consumption, get_custom_consumption, update_custom_consumption, create_custom_consumption

def get_consumption(car, track, user):
    if user is not None:
        data = get_custom_consumption(car, track, user)
        if len(data) > 0:
            return data
    
    data = get_generic_consumption(car, track)
    return data

def save_consumption(car, track, fuel, user):
    existing_record = get_custom_consumption(car=car, track=track, user=user)
    if len(existing_record) == 0:
        return create_custom_consumption(car=car, track=track, user=user, fuel=fuel)
    else:

        return update_custom_consumption(id=existing_record[0].id, fuel=fuel)
