# -*- coding: utf-8 -*-
# from odoo import http


# class Infocomercio(http.Controller):
#     @http.route('/infocomercio/infocomercio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infocomercio/infocomercio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('infocomercio.listing', {
#             'root': '/infocomercio/infocomercio',
#             'objects': http.request.env['infocomercio.infocomercio'].search([]),
#         })

#     @http.route('/infocomercio/infocomercio/objects/<model("infocomercio.infocomercio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infocomercio.object', {
#             'object': obj
#         })
