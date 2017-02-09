# -*- coding: utf-8 -*-
{
    'name': "Classification de sirop",

    'summary': """
		Opération de classification de sirop d'érable
		""",
    'description': """
        Classification et entrée des caractéristiques du sirop d'érable.
    """,

    'author': "Global Technologie",
    'website': "http://www.globaltechnologie.ca",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['maplereception'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
		'views/reports.xml',
#        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
 #       'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
