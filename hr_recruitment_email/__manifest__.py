{
    'name': 'Recruitment E-Mail Extensions',
    'version': '14.0.1.0.0',
    'summary': 'E-Mails extensions, like date for first meet and email on refuse',
    'category': 'Human Resources/Recruitment',
    'author': 'Martin Reisenhofer',    
    'website': 'https://github.com/oerp-at',
    'license': 'LGPL-3',    
    'depends': [
        'hr_recruitment',
    ],    
    'data': [
        'views/hr_refuse_reason_view.xml',
        'views/hr_applicant_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
