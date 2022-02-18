{
    'name':'Comptabilite Financiere ENSAH',
    'version':'1.0',
    'author':'Maanaoui Youssef',
    'category':'ENSAH ERP',
    'sequence':1,
    'description': """
         Module test de gestion des factures des l'ensah
         *Gestion des factures clients
         *Gestion des factures fournisseurs
    
    """,
    'website':'http://www.hh.ma',
    'img':['./images/ensah.png'],
    'depends':['base'],
    'data':['gfe_fournisseurs_view.xml',
            'facture_fournisseurs_view.xml',
            'compte_view.xml',
            'journal_view.xml',
            'payment_method_view.xml',
            'account_type_view.xml',
            'finance_report_view.xml',
            'article.xml',
            'recu_achat_view.xml',
            'payement_frn_view.xml',
            'recu_achat_workflow_view.xml',
            'facture_fournisseurs_workflow_view.xml',
            ],
    'init_xml' : [],
    'update_xml' : [],
    'js':[],
    'qweb':[],
    'css':[],
    'demo':[],
    'test':[],
    "installable": True,
    "auto_install": False
}