# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class clsu_brews_and_boards(models.Model):
#     _name = 'clsu_brews_and_boards.clsu_brews_and_boards'
#     _description = 'clsu_brews_and_boards.clsu_brews_and_boards'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# brand_id = fields.Many2one('sge_scooters.brand', string='Fabricante de patinetes')
# clients_id =fields.One2many('sge_scooters.client','bike_id',string='Reservada por ')

from odoo import models, fields, api # type: ignore
class comida(models.Model):
    _name = 'clsu_brews_and_boards.comida'
    _description = 'Menú de comida'

    id = fields.Char()
    nombre = fields.Char()
    precio = fields.Float()
    tipo = fields.Selection(string='Tipo', selection=[('snacks','Picoteo'),('dish','Primer plato'),('dessert','Postre')])

    pedido = fields.Mani2one('clsu_brews_and_boards.pedido', string='Número de pedido')

class bebida(models.Model):
    _name = 'clsu_brews_and_boards.bebida'
    _description = 'Menú de bebidas'

    id = fields.Char()
    nombre = fields.Char()
    precio = fields.Float()
    tamaño = fields.Selection(string='Tamaño', selection=[('small','Pequeño'),('meidum','Mediano'),('tall','Grande')])

class pedido(models.Model):
    _name = 'clsu_brews_and_boards.pedido'
    _description = 'Pedido de comida'

    id = fields.Char()
    hora = fields.Date()

class staff(models.Model):
    _name = 'clsu_brews_and_boards.staff'
    _description = 'Trabajadores'

    id = fields.Char()
    nombre = fields.Char()
    telf = fields.Integer()
    email = fields.Char()
    rol = fields.Selection(string='Rol', selection=[('mess','Mesero'),('coff','Barista'),('mangr','Administrador')])

class jugador(models.Model):
    _name = 'clsu_brews_and_boards.jugador'
    _description = 'Cliente habitual'

    id = fields.Char()
    nombre = fields.Char()
    alias = fields.Char()

class torneo(models.Model):
    _name = 'clsu_brews_and_boards.torneo'
    _description = 'Torneo de juego'

    id = fields.Char()
    nombre = fields.Char()
    premio = fields.Char()
    fecha = fields.Date()

class mesa(models.Model):
    _name = 'clsu_brews_and_boards.mesa'
    _description = 'Mesas del local'

    num_mesa = fields.Char()
    capacidad = fields.Integer()
    tipo = fields.Boolean(string='Apto para juego', default=True)
    estado = fields.Selection(string='Estado', selection=[('free','Libre'),('stop','Ocupada'),('resr','Reservada')])

class reserva(models.Model):
    _name = 'clsu_brews_and_boards.reserva'
    _description = 'Registro de reserva'

    id = fields.Char()
    hora = fields.Date()
    jugadores = fields.Integer()
