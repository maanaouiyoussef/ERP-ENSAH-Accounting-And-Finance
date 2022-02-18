from osv import osv,fields
import openerp

class payement_frn(osv.osv):
    _name= 'gfe.payement_frn'
    _columns={
        'name': fields.many2one('gfe.fournisseurs','Fournisseur',ondelete='cascade'),
        'total':fields.float('Total')  ,
        'payment_method':fields.many2one('gfe.payement_method','Method de paiement')  ,
        'date':fields.date('Date de paiement') ,
        'compte': fields.many2one('gfe.compte','Compte',ondelete='cascade')
   }
    
payement_frn()