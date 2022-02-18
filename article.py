from osv import osv,fields
import openerp

class article(osv.osv):
    _name= 'gfe.article'

    def _get_selection(self, cursor, article_id, context=None):
        return (('study', 'Studies'),('infrastructure', 'Infrastructure'),('internat', 'Internat'))

    _columns={
        'name': fields.char('Nom'), 
        'code': fields.float('Code'),
        'category': fields.selection(_get_selection, 'Categorie'),
        'qty': fields.float('Quantity'),
        'idfacture': fields.many2one('gfe.facture_fournisseurs','Facture',ondelete='cascade')
        # department = article
        # etablissement = facture
   }

article()