import logging

from sqlalchemy.util import OrderedDict

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)


class Custom_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets, inherit=True)

    def update_config(self, config_):
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'custom_theme')
        toolkit.add_template_directory(config_, 'templates')

    # Discipline
    # package_type is 'dataset' for Dataset menu option
    def dataset_facets(self, facets_dict, package_type):
        if package_type != 'harvest':
            return OrderedDict([('tags', 'Disciplines'),
                                ('groups', 'Keywords'),
                                ('Collections', toolkit._('Collections')),
                                ('license_id', 'Data access')])
        else:
            return facets_dict

    # this only works this way. I.e. not like dataset_facets!
    # Why? I have no idea, but this is documented that way as well
    def group_facets(self, facets_dict, group_type, package_type):
        # strip away the unwanted standard facets
        facets_dict.pop('organization')
        facets_dict.pop('license_id')
        facets_dict.pop('tags')
        facets_dict.pop('res_format')
        facets_dict['tags'] = 'Disciplines'
        facets_dict['groups'] = 'Keywords'
        #facets_dict['collection'] = 'Collection'
        facets_dict['license_id'] = 'Data access'

        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        # strip away the unwanted standard facets
        facets_dict.pop('organization')
        facets_dict.pop('license_id')
        facets_dict.pop('tags')
        facets_dict.pop('res_format')
        facets_dict['tags'] = 'Disciplines'
        facets_dict['groups'] = 'Keywords'
        facets_dict['Collections'] = 'Collections'
        facets_dict['license_id'] = 'Data access'

        return facets_dict
