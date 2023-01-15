# -*- coding: utf-8 -*-
# from odoo import http


# class Barrio1(http.Controller):
#     @http.route('/barrio1/barrio1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barrio1/barrio1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('barrio1.listing', {
#             'root': '/barrio1/barrio1',
#             'objects': http.request.env['barrio1.barrio1'].search([]),
#         })

#     @http.route('/barrio1/barrio1/objects/<model("barrio1.barrio1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barrio1.object', {
#             'object': obj
#         })
