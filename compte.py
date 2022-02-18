from osv import osv,fields
import openerp

class compte(osv.osv):
    _name= 'gfe.compte'
    _columns={
        'name':fields.char('Nom et Numero')  ,
        'type': fields.many2one('gfe.account_type', 'Type de Compte', ondelete='cascade'),
        'credit': fields.float('Credit'),
        'debit':fields.float('Debit'),
        'balance':fields.float('Balance') ,
    }
    
compte()