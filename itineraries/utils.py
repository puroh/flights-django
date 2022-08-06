def transform_result(data: list) -> dict:

    itis = []
    legs = []
    trasnformed_data = {}
    for element in data:
        itis.append(element.get("itineraries"))
        legs.append(element.get("legs"))

    trasnformed_data["itineraries"] = itis
    trasnformed_data["legs"] = legs

    return trasnformed_data
