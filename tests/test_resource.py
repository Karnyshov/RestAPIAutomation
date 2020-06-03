from src.template import Template


class TestResource(Template):
    def test_resource(self):
        response = self.api.get(self.api.RESOURCE_URL)

        assert 200 == response.status_code

        assert 1 == response.json()['page']
        assert 6 == response.json()['per_page']
        assert 12 == response.json()['total']
        assert 2 == response.json()['total_pages']

        assert [] != response.json()['data']
        # TODO: assert that dictionaries are not empty

    def test_specific_resource(self):
        response = self.api.get(self.api.RESOURCE_URL + '/2')

        assert 200 == response.status_code

        assert 2 == response.json()['data']['id']
        assert 'fuchsia rose' == response.json()['data']['name']
        assert 2001 == response.json()['data']['year']
        assert '#C74375' == response.json()['data']['color']
        assert '17-2031' == response.json()['data']['pantone_value']

    def test_resource_absent(self):
        response = self.api.get(self.api.RESOURCE_URL + '/0')

        assert 404 == response.status_code

        assert {} == response.json()
