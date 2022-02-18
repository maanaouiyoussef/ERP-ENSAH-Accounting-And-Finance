from osv import osv,fields
import openerp

class journal(osv.osv):
    _name= 'gfe.journal'
    _columns={
        'name':fields.char('Nom du journal')  ,
        'code':fields.char('Code',size=64)  ,
        'type':fields.many2one('gfe.account_type','Type de compte', ondelete='cascade') ,
        'default_debit': fields.many2one('gfe.compte','Compte debit par default',ondelete='cascade'),
        'default_credit': fields.many2one('gfe.compte','Compte credit par default',ondelete='cascade'),
   }
    
journal()