from osv import osv,fields
import openerp

class payement_method(osv.osv):
    _name= 'gfe.payement_method'
    _columns={
        'name': fields.char('Payment Method'), 
        'code': fields.float('Payment Code')
   }
    
payement_method()