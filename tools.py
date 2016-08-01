
def get_places(list_points):
    places = []
    for point in list_points:
        places.append(point["geopoint"]["coordinates"])
    return places


def get_traces(list_places):
    routes = []
    for place in list_places:
        local_steps = "["
        for route in place["route"]:
            local_steps.append("["+route["end_location"]["lng"]+","+route["end_location"]["lat"]+"]")
        local_steps = local_steps + "]"
        routes.append(local_steps)
    return routes


def format_response(longitude, latitude, mode, head, list_points):
    response = {}
    response["longitude"]= longitude
    response["latitude"]= latitude
    response["mode"] = mode
    response["head"] = head
    response["points"] = list_points
    response["places"] = get_places(list_points)
    response["traces"] = get_traces(list_points)
    return response
