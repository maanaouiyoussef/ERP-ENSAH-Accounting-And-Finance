from osv import osv,fields
import openerp

class recu_achat(osv.osv):
    def _draft_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'draft'})
        return True
    def _posted_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'posted'})
        return True
    
    _name= 'gfe.recu_achat'
    _columns={
        'fournisseur': fields.many2one('gfe.fournisseurs', 'Fournssseurs'),
        'compte': fields.many2one('gfe.compte', 'Compte'),
        'echeance_date': fields.date('Date de facturation'), 
        'facturation_date': fields.date('Date de facturation'), 
        'journal': fields.many2one('gfe.journal', 'Journal'),
        'nref': fields.char('Num de reference'), 
        'description': fields.char('Description'), 
        'total': fields.float('Montant'), 
        'state': fields.selection([
            ('draft','Brouillon'),
            ('posted','Posted'),
        ], 'State', readonly=True)
       # Your done for Maintenance... calculate total
   }
    
recu_achat()