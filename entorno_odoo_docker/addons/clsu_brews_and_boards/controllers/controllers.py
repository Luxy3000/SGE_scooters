# -*- coding: utf-8 -*-
# from odoo import http


# class ClsuBrewsAndBoards(http.Controller):
#     @http.route('/clsu_brews_and_boards/clsu_brews_and_boards', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clsu_brews_and_boards/clsu_brews_and_boards/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clsu_brews_and_boards.listing', {
#             'root': '/clsu_brews_and_boards/clsu_brews_and_boards',
#             'objects': http.request.env['clsu_brews_and_boards.clsu_brews_and_boards'].search([]),
#         })

#     @http.route('/clsu_brews_and_boards/clsu_brews_and_boards/objects/<model("clsu_brews_and_boards.clsu_brews_and_boards"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clsu_brews_and_boards.object', {
#             'object': obj
#         })

