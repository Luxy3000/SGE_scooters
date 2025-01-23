# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sge_scooters(models.Model):
#     _name = 'sge_scooters.sge_scooters'
#     _description = 'sge_scooters.sge_scooters'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api # type: ignore

class brand(models.Model):
    _name = 'sge_scooters.brand'
    _description = 'Marcas'

    name = fields.Char('Marca')
    nvehicles = fields.Integer('Vehículos disponibles')
    desc = fields.Text('Descripción')
    nbikes = fields.Integer('Nº de Bicicletas')
    nscooters = fields.Integer('Nº de Scooters')

    bike_id = fields.One2many('sge_scooters.ebike', 'brand_id', string = 'Modelos de bicicletas')
    scooter_id = fields.One2many('sge_scooters.scooter', 'brand_id', string = 'Modelos de patinetes')

class ebike(models.Model):
    _name = 'sge_scooters.ebike'
    _description = 'Bicicletas eléctricas'

    name = fields.Char('Modelo')
    peso = fields.Integer('Peso')
    tipo = fields.Selection(string='Tipo', selection=[('ci', 'ciudad'), ('ca','carretera'),('pl', 'Plegable')], default='ci')
    precio = fields.Float('Precio por horas', (5,2))
    motor = fields.Boolean(string='Motor trasero', default=False)

    brand_id = fields.Many2one('sge_scooters.brand', string='Fabricante de patinetes')
    clients_id =fields.One2many('sge_scooters.client','bike_id',string='Reservada por ')

class scooter(models.Model):
    _name = 'sge_scooters.scooter'
    _description = 'Patinetes eléctricos'

    name = fields.Char('Modelo')
    peso = fields.Integer('Peso')
    precio = fields.Float('Precio por horas', (5,2))
    panel = fields.Boolean(string='Con panel', default=False)
    potencia = fields.Selection(string='Nivel', selection=[('baja', 'Menos de 250W'), ('media','De 250W a 500W'),('alta', 'Más de 500W')], default='low')

    brand_id = fields.Many2one('sge_scooters.brand', string='Fabricante de patinetes')
    clients_id =fields.One2many('sge_scooters.client','scooter_id',string='Alquilada por ')

class client(models.Model):
    _name = 'sge_scooters.client'
    _description = 'Clientes de la empresa'

    name = fields.Char('Codigo de cliente')
    dni = fields.Char('DNI')
    nombre = fields.Char('Nombre')
    apellido = fields.Char('Apellido')

    bike_id = fields.Many2one('sge_scooters.ebike', string='Bicicleta alquilada')
    scooter_id = fields.Many2one('sge_scooters.scooter', string='Patinete alquilado')
