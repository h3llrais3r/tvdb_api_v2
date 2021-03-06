# coding: utf-8

# flake8: noqa

"""
    TheTVDB API v2

    API v3 targets v2 functionality with a few minor additions. The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.   How to use this API documentation ----------------   You may browse the API routes without authentication, but if you wish to send requests to the API and see response data, then you must authenticate. 1. Obtain a JWT token by `POST`ing  to the `/login` route in the `Authentication` section with your API key and credentials. 1. Paste the JWT token from the response into the \"JWT Token\" field at the top of the page and click the 'Add Token' button.   You will now be able to use the remaining routes to send requests to the API and get a response.   Language Selection ----------------   Language selection is done via the `Accept-Language` header. At the moment, you may only pass one language abbreviation in the header at a time. Valid language abbreviations can be found at the `/languages` route..   Authentication ----------------   Authentication to use the API is similar to the How-to section above. Users must `POST` to the `/login` route with their API key and credentials in the following format in order to obtain a JWT token.  `{\"apikey\":\"APIKEY\",\"username\":\"USERNAME\",\"userkey\":\"USERKEY\"}`  Note that the username and key are ONLY required for the `/user` routes. The user's key is labled `Account Identifier` in the account section of the main site. The token is then used in all subsequent requests by providing it in the `Authorization` header. The header will look like: `Authorization: Bearer <yourJWTtoken>`. Currently, the token expires after 24 hours. You can `GET` the `/refresh_token` route to extend that expiration date.   Versioning ----------------   You may request a different version of the API by including an `Accept` header in your request with the following format: `Accept:application/vnd.thetvdb.v$VERSION`. This documentation automatically uses the version seen at the top and bottom of the page.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from tvdb_api.api.authentication_api import AuthenticationApi
from tvdb_api.api.episodes_api import EpisodesApi
from tvdb_api.api.languages_api import LanguagesApi
from tvdb_api.api.movies_api import MoviesApi
from tvdb_api.api.search_api import SearchApi
from tvdb_api.api.series_api import SeriesApi
from tvdb_api.api.updates_api import UpdatesApi
from tvdb_api.api.users_api import UsersApi

# import ApiClient
from tvdb_api.api_client import ApiClient
from tvdb_api.configuration import Configuration
# import models into sdk package
from tvdb_api.models.auth import Auth
from tvdb_api.models.basic_episode import BasicEpisode
from tvdb_api.models.conflict import Conflict
from tvdb_api.models.episode import Episode
from tvdb_api.models.episode_data_query_params import EpisodeDataQueryParams
from tvdb_api.models.episode_language_info import EpisodeLanguageInfo
from tvdb_api.models.episode_record_data import EpisodeRecordData
from tvdb_api.models.filter_keys import FilterKeys
from tvdb_api.models.invalid_query_params import InvalidQueryParams
from tvdb_api.models.json_errors import JSONErrors
from tvdb_api.models.language import Language
from tvdb_api.models.language_data import LanguageData
from tvdb_api.models.links import Links
from tvdb_api.models.movie import Movie
from tvdb_api.models.movie_artwork import MovieArtwork
from tvdb_api.models.movie_genre import MovieGenre
from tvdb_api.models.movie_people import MoviePeople
from tvdb_api.models.movie_release_date import MovieReleaseDate
from tvdb_api.models.movie_remote_id import MovieRemoteId
from tvdb_api.models.movie_trailer import MovieTrailer
from tvdb_api.models.movie_translation import MovieTranslation
from tvdb_api.models.not_authorized import NotAuthorized
from tvdb_api.models.not_found import NotFound
from tvdb_api.models.series import Series
from tvdb_api.models.series_actors import SeriesActors
from tvdb_api.models.series_actors_data import SeriesActorsData
from tvdb_api.models.series_data import SeriesData
from tvdb_api.models.series_episodes import SeriesEpisodes
from tvdb_api.models.series_episodes_query import SeriesEpisodesQuery
from tvdb_api.models.series_episodes_query_params import SeriesEpisodesQueryParams
from tvdb_api.models.series_episodes_summary import SeriesEpisodesSummary
from tvdb_api.models.series_image_query_result import SeriesImageQueryResult
from tvdb_api.models.series_image_query_result_ratings_info import SeriesImageQueryResultRatingsInfo
from tvdb_api.models.series_image_query_results import SeriesImageQueryResults
from tvdb_api.models.series_images_count import SeriesImagesCount
from tvdb_api.models.series_images_counts import SeriesImagesCounts
from tvdb_api.models.series_images_query_param import SeriesImagesQueryParam
from tvdb_api.models.series_images_query_params import SeriesImagesQueryParams
from tvdb_api.models.series_search_result import SeriesSearchResult
from tvdb_api.models.series_search_results import SeriesSearchResults
from tvdb_api.models.token import Token
from tvdb_api.models.update import Update
from tvdb_api.models.update_data import UpdateData
from tvdb_api.models.update_data_query_params import UpdateDataQueryParams
from tvdb_api.models.updated_movies import UpdatedMovies
from tvdb_api.models.user import User
from tvdb_api.models.user_data import UserData
from tvdb_api.models.user_favorites import UserFavorites
from tvdb_api.models.user_favorites_data import UserFavoritesData
from tvdb_api.models.user_ratings import UserRatings
from tvdb_api.models.user_ratings_data import UserRatingsData
from tvdb_api.models.user_ratings_data_no_links import UserRatingsDataNoLinks
from tvdb_api.models.user_ratings_data_no_links_empty_array import UserRatingsDataNoLinksEmptyArray
from tvdb_api.models.user_ratings_query_params import UserRatingsQueryParams
