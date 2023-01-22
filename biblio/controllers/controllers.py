# -*- coding: utf-8 -*-
# from odoo import http


# class Biblio(http.Controller):
#     @http.route('/biblio/biblio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biblio/biblio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('biblio.listing', {
#             'root': '/biblio/biblio',
#             'objects': http.request.env['biblio.biblio'].search([]),
#         })

#     @http.route('/biblio/biblio/objects/<model("biblio.biblio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biblio.object', {
#             'object': obj
#         })
