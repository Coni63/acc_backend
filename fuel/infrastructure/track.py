from ..domain.track import Track

def get_all_tracks():
    return Track.objects.all()

def get_track_by_id(id: int):
    return Track.objects.get(pk=id)