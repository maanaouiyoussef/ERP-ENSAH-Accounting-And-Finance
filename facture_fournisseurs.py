from osv import osv,fields
import openerp

class facture_fournisseurs(osv.osv):
    def _draft_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'draft'})
        return True
    def _open_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'open'})
        return True
    def _payed_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'payed'})
        return True

    _name= 'gfe.facture_fournisseurs'
    _columns={
        'code':fields.integer('Code',size=64)  ,
        'frn_id': fields.many2one('gfe.fournisseurs','Fournisseur',ondelete='cascade'),
        'compte-id': fields.many2one('gfe.compte','Compte',ondelete='cascade'),
        'dateDeFacture':fields.date('Date De Facturation')  ,
        'total': fields.float('Total'),
        'state': fields.selection([
            ('draft','Brouillon'),
            ('open','Open'),
            ('payed','Payed')
        ], 'State', readonly=True),
        'article_ids': fields.one2many('gfe.article','idfacture',string='Article'),

        # department = article
        # etablissement = facture
    }
    
facture_fournisseurs()