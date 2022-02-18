from osv import osv,fields
import openerp

class gfe_fournisseurs(osv.osv):
    _name= 'gfe.fournisseurs'
    _columns={
        'name':fields.char('Nom',size=255) ,
        'code':fields.char('Code',size=64)  ,
        'adresse':fields.char('Adresse')  ,
        'telephone': fields.char('Telephone') ,
        'website': fields.char('Website') ,
        'capacity': fields.float('Capacity') ,
    }

gfe_fournisseurs()