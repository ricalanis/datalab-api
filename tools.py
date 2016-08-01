
def get_places(list_points):
    try:
        places = []
        for point in list_points:
            places.append(point["geopoint"]["coordinates"])
    except:
        places = "NaN"
    return places


def get_traces(list_places):
    try:
        routes = []
        for place in list_places:
            local_steps = "["
            i = 0
            for route in place["route"]:
                if i > 0:
                    initial_string = ","
                else:
                    initial_string = ""
                local_steps.append(initial_string + "["+route["end_location"]["lng"]+","+route["end_location"]["lat"]+"]")
            local_steps = local_steps + "]"
            routes.append(local_steps)
    except:
        routes = "NaN"
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
