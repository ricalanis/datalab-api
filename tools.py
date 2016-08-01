
def get_places(list_points):
    places = []
    for point in list_points:
        places.append(point["geopoint"]["coordinates"])
    return places


def get_traces(list_places):
    traces = []
    for place in list_places:
        local_trace = []
        for traces in place["legs"]:
            for step in traces["steps"]:
                local_trace.append([step["longitude"], step["latitude"]])
        traces.append(local_trace)
    return traces


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
