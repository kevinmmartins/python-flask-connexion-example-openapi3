# coding: utf-8

from basic import init_api

def test_get_alive():
    conn_app = init_api()
    with conn_app.test_client() as tc:
        response = tc.get("/v1/basic/ping")
        assert 200 == response.status_code
