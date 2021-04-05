# -*- coding: utf-8 -*-
{
    'name': "Incentivos Alvamex",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Marco Gonzalez",
    'website': "http://www.grupoalvamex.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','base_grupoalvamex'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',        
        'views/incentivo_vacunacion_views.xml',
        'views/incentivo_alvamex_config_views.xml',
        'views/menus.xml',
        'data/incentivo_alvamex_config.xml',
        #'views/templates.xml',
    ],
    'installable': True,
}