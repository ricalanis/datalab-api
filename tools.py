
def get_places(list_points):
    try:
        places = []
        for point in list_points:
            places.append(point["geopoint"]["coordinates"])
    except:
        places = "NaN"
    return places


def get_traces(longitude, latitude, list_points):
    try:
        routes = []
        for place in list_points:
            i = 0
            local_steps = ""
            for route in place["route"]:
                if i > 0:
                    initial_string = ","
                else:
                    initial_string = "[[" + str(longitude) + "," + str(latitude) +"],"
                local_steps = local_steps + initial_string + "["+str(route["end_location"]["lng"])+","+str(route["end_location"]["lat"])+"]"
                i = i + 1
            local_steps = local_steps + "]"
            routes.append(local_steps)
    except:
        routes = "NaN"
    return routes

def print_points(longitude,latitude,list_points):
    list_strings = []
    for point in list_points:
        list_strings.append("[["+ str(longitude) + ","+str(latitude)+"],["+str(point[0])+","+str(point[1])+"]]")
    return list_strings

def format_response(longitude, latitude, mode, head, list_points):
    response = {}
    response["longitude"]= longitude
    response["latitude"]= latitude
    response["mode"] = mode
    response["head"] = head
    response["points"] = list_points
    response["places"] = get_places(list_points)
    if mode == "euclidean":
        response["traces"] = print_points(longitude, latitude, response["places"])
    else:
        response["traces"] = get_traces(longitude, latitude, list_points)
    return response
