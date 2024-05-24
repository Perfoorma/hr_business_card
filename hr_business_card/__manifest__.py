# -*- coding: utf-8 -*-
{
    'name': "Business Card",
    'version': '17.0.0.0',
    'depends': [
        'hr',
        'website'
        ],
    'author': "Perfoorma, Michele Dario Scalia, Sherpya",
    'category': 'Human Resources',
    'summary':"""
             Your business card can reduce paper waste!""",
    'description': """
        Display business card on public website to reduce paper waste   
    """,
    'data': [
        'views/business_card.xml',
    ],
    'website': 'https://perfoorma.com',
    'license': 'LGPL-3',
    'images': ['static/description/assets/fabien_pinckaers.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'external_dependencies': {
        'python': ['qrcode'],
    },

}
