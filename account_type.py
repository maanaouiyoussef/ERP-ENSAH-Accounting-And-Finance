from osv import osv,fields
import openerp

class account_type(osv.osv):
    _name= 'gfe.account_type'
    _columns={
        'name': fields.char('Type de compte'), 
        'code': fields.float('Code')
   }
    
account_type()