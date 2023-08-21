""" address-to-coordinate """
import os


import googlemaps


def query_coordinate_from_address(
        client, 
        address: str,
):
    """Query the coordinate from the address.
    GOOGLE_API_KEY is required because it uses googlemap's geocoding API
    see: https://developers.google.com/maps/documentation/geocoding/overview
    """

    location = client.geocode(address)[0]["geometry"]["location"]
    print(f'{location["lat"]}\t{location["lng"]}')


def main():
    """Main."""

    assert os.environ.get("GOOGLE_API_KEY"), "Set your GOOGLE_API_KEY."
    googleapikey = os.environ["GOOGLE_API_KEY"]
    gmaps = googlemaps.Client(key=googleapikey)

    while True:
        line = input()
        query_coordinate_from_address(gmaps, line)



if __name__ == "__main__":
    main()
