from Workshop.Workshop8.album_requests import (
    get_album,
    get_album_tacks,
)
import unittest

ALBUM_ID = "5eA0qtE7Yu29XiMlwoby2G"

class TestSuite(unittest.TestCase):

    def test_get_album_status_code(self):
        response = get_album(ALBUM_ID)
        assert response.status_code == 200

    def test_get_album_album_type(self):
        response = get_album(ALBUM_ID)
        response_data = response.json()
        expected_album_type = "album"
        actual_album_type = response_data['album_type']
        assert actual_album_type == expected_album_type, f"Error, expected album_type {expected_album_type} , actual album type {actual_album_type}"

    def test_get_album_artist_name(self):
        response = get_album(ALBUM_ID)
        response_data = response.json()
        expected_artist_name = "Nirvana"
        actual_artist_name = response_data['artists'][0]['name']
        assert actual_artist_name == expected_artist_name, f'Error, excpected {expected_artist_name}, returned {actual_artist_name}'

    def test_get_album_album_name(self):
        response = get_album(ALBUM_ID)
        response_data = response.json()
        expected_album_name = "Nevermind (30th Anniversary Super Deluxe)"
        actual_album_name = response_data['name']
        assert actual_album_name == expected_album_name, f'Error, expected {expected_album_name}, returned {actual_album_name}'

    def test_get_album_invalid_album_id(self):
        invalid_album_id = ALBUM_ID + "x"
        response = get_album(invalid_album_id)
        assert response.status_code == 400
        response_data = response.json()
        expected_error_message = "invalid id"
        actual_error_message = response_data['error']['message']
        assert actual_error_message == expected_error_message, f'Error, expected {expected_error_message}, returned {actual_error_message}'

    def test_get_album_tracks_total_number(self):
        response = get_album_tacks(ALBUM_ID)
        response_data = response.json()
        expected_number_of_tracks = 20
        actual_tracks_number = len(response_data['items'])
        assert actual_tracks_number == expected_number_of_tracks, f'Error, expected {expected_number_of_tracks}, returned {actual_tracks_number}'

    def test_get_album_track_names(self):
        response = get_album_tacks(ALBUM_ID)
        response_data = response.json()
        expected_first_track = "Smells Like Teen Spirit - Remastered 2021"
        expected_10th_track = "Stay Away - Remastered 2021"
        expected_20th_track = "Polly - Live In Amsterdam, Netherlands/1991"
        actual_first_track = response_data['items'][0]['name']
        actual_10th_track = response_data['items'][9]['name']
        actual_20th_track = response_data['items'][19]['name']
        assert actual_first_track == expected_first_track, f'Error, expected {expected_first_track}, returned {actual_first_track}'
        assert actual_10th_track == expected_10th_track, f'Error, expected {expected_10th_track}, returned {actual_10th_track}'
        assert actual_20th_track == expected_20th_track, f'Error, expected {expected_20th_track}, returned {expected_20th_track}'