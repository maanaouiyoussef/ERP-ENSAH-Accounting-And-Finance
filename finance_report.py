from osv import osv,fields
import openerp

class finance_report(osv.osv):
    _name= 'gfe.finance_report'
    _columns={
        'name': fields.char('Nom du rapport'), 
        'parent': fields.many2one('gfe.finance_report', 'Parent',ondelete='cascade'),
        'type': fields.many2one('gfe.account_type', 'Type du compte',ondelete='cascade')
   }

finance_report()