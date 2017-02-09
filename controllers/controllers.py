# -*- coding: utf-8 -*-
from openerp import http

# class Maplerating(http.Controller):
#     @http.route('/maplerating/maplerating/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maplerating/maplerating/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('maplerating.listing', {
#             'root': '/maplerating/maplerating',
#             'objects': http.request.env['maplerating.maplerating'].search([]),
#         })

#     @http.route('/maplerating/maplerating/objects/<model("maplerating.maplerating"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maplerating.object', {
#             'object': obj
#         })