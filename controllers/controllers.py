# -*- coding: utf-8 -*-
from odoo import http

# class ComisionesAlvamex(http.Controller):
#     @http.route('/comisiones_alvamex/comisiones_alvamex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comisiones_alvamex/comisiones_alvamex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('comisiones_alvamex.listing', {
#             'root': '/comisiones_alvamex/comisiones_alvamex',
#             'objects': http.request.env['comisiones_alvamex.comisiones_alvamex'].search([]),
#         })

#     @http.route('/comisiones_alvamex/comisiones_alvamex/objects/<model("comisiones_alvamex.comisiones_alvamex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comisiones_alvamex.object', {
#             'object': obj
#         })