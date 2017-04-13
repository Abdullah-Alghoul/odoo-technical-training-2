{    
    "name": "OpenAcademy Managment",
    "description": """
OpenAcademy Managment
===============================
* Sessions Managment
* Course Managment
* etc...
""",
    "summary": "Sessions,Courses",
    "license": "LGPL-3",
    "version": "1.0",
    "category": "Extra Addons",
    "sequence": 0,
    "website": "https://www.odoo.com",
    "author": "Odoo, Inc",
    "depends": ["sale", "mail"],
    "data": [
        "views/openacademy_views.xml",
        "views/partner_view.xml",
    ],
    "demo": [
        "demo/openacademy_session_demo.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}