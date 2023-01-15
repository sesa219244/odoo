# -*- coding: utf-8 -*-
{
    'name': "informacion de comercios",

    'summary': """
    Información sobre pequeños comercios o tiendas de barrio y las compañías de envío que utilizan para enviar sus pedidos""",

    'description': """
    Tarea Evaluativa del módulo Sistema de Gestión Empresarial del ciclo de Desarrollo de Aplicaciones Multiplataforma""",

    'author': "Oscar Garijo Pereda",
    'website': "http://www.birt.eus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/report_envio.xml',
        'report/report_tienda.xml',
        'report/report_seguros.xml',
        'data/data.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
