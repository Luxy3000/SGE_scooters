# -*- coding: utf-8 -*-
{
    'name': "Brew and Boards",

    'summary': "Gestión de cafetería de juegos de mesa",

    'description': "Modulo de gestión de locales de ocio con servicio de cafetería y ludoteca con juegos de mesa",

    'author': "Cielo Lucia Sosa Urviola",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/brews_and_boards_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/brews_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'icon': '/clsu_brews_and_boards/static/description/icon.jpg',
    # Se indica que es una aplicación
    'application': True,
}

