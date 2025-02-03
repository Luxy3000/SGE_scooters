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
# pedido = fields.Many2many('clsu_brews_and_boards.pedido', 'tu_tabla_relacion', 'columna_id_actual', 'columna_id_pedido', string='Número de pedido')

from odoo import models, fields, api # type: ignore
class comida(models.Model):
    _name = 'clsu_brews_and_boards.comida'
    _description = 'Menú de comida'

    name = fields.Char('Comida')
    nombre = fields.Char('Nombre de la comida')
    precio = fields.Float('Precio')
    tipo = fields.Selection(
        string='Tipo', 
        selection=[
            ('snacks','Picoteo'),
            ('dish','Primer plato'),
            ('dessert','Postre')
        ]
    )

    pedido_id = fields.Many2many(
        'clsu_brews_and_boards.pedido', #Modelo relacionado
        'pedido_comida',                #Nombre de la tabla intermedia
        'comida_id',                    #Referencia a este modelo
        'pedido_id',                    #Referencia al otro modelo
        string='Pertenece a pedido:'
    )

class bebida(models.Model):
    _name = 'clsu_brews_and_boards.bebida'
    _description = 'Menú de bebidas'

    name = fields.Char('Bebida')
    nombre = fields.Char('Nombre de la bebida')
    precio = fields.Float('Precio')
    tamanio = fields.Selection(
        string='Tamaño', 
        selection=[
            ('small','Pequeño'),
            ('medium','Mediano'),
            ('tall','Grande')
        ]
    )

    pedido_id = fields.Many2many(
        'clsu_brews_and_boards.pedido', #Modelo relacionado
        'pedido_bebida',                #Nombre de la tabla intermedia
        'bebida_id',                    #Referencia a este modelo
        'pedido_id',                    #Referencia al otro modelo
        string='Pertenece a pedido: '
    )

class pedido(models.Model):
    _name = 'clsu_brews_and_boards.pedido'
    _description = 'Pedido de comida'

    name = fields.Char('Pedido')
    hora = fields.Datetime('Hora del pedido')

    comida_id = fields.Many2many(
        'clsu_brews_and_boards.comida',
        'pedido_comida',
        'pedido_id',
        'comida_id',
        string='Comida en el pedido'
    )
    bebida_id = fields.Many2many(
        'clsu_brews_and_boards.bebida',
        'pedido_bebida',
        'pedido_id',
        'bebida_id',
        string='Bebida en el pedido'
    )
    staff_id=fields.Many2one(
        'clsu_brews_and_boards.staff', 
        string="Encargado del pedido"
    )
    jugador_id=fields.Many2one(
        'clsu_brews_and_boards.jugador', 
        string="Pedido para "
    )

class staff(models.Model):
    _name = 'clsu_brews_and_boards.staff'
    _description = 'Trabajadores'

    name = fields.Char('Staff')
    nombre = fields.Char('Nombre: ')
    telf = fields.Integer('Telefono: ')
    email = fields.Char('Email: ')
    rol = fields.Selection(
        string='Rol', 
        selection=[
            ('mess','Mesero'),
            ('coff','Barista'),
            ('mangr','Administrador')
        ]
    )

    pedido_id=fields.One2many(
        'clsu_brews_and_boards.pedido', 
        'staff_id', 
        string='Pedidos realizados'
    )

class jugador(models.Model):
    _name = 'clsu_brews_and_boards.jugador'
    _description = 'Cliente habitual'

    name = fields.Char('Jugadores')
    nombre = fields.Char('Nombre completo: ')
    alias = fields.Char('Alias: ')
    telf = fields.Char("Nº teléfono: ")
    email = fields.Chat("Email: ")

    pedido_id=fields.One2many(
        'clsu_brews_and_boards.pedido', 
        'jugador_id', 
        string='Pedidos realizados'
    )
    torneo_id = fields.Many2many(
        'clsu_brews_and_boards.torneo',
        'torneo_jugador',
        'torneo_id',
        'jugador_id',
        string='Participa en '
    )
    reserva_id=fields.One2many(
        'clsu_brews_and_boards.reserva', 
        'jugador_id', 
        string='Pedidos realizados'
    )

class torneo(models.Model):
    _name = 'clsu_brews_and_boards.torneo'
    _description = 'Torneo de juego'

    name = fields.Char('Torneos')
    nombre = fields.Char('Titulo del torneo: ')
    premio = fields.Char('Premio del torneo: ')
    fecha_inicio = fields.Date('Fecha establecida de inicio: ')
    fecha_final = fields.Date('Fecha establecida de fin:')

    jugador_id = fields.Many2many(
        'clsu_brews_and_boards.jugador',
        'torneo_jugador',
        'jugador_id',
        'torneo_id',
        string='Participa '
    )
    juego_id=fields.Many2one(
        'clsu_brews_and_boards.juego', 
        string="Pedido para "
    )

class juego(models.Model):
    _name = 'clsu_brews_and_boards.juego'
    _description = 'Torneo de juego'

    name = fields.Char('Juegos de mesa')
    nombre = fields.Char('Nombre del juego: ')
    genero = fields.Selection(
        string='Género del juego', 
        selection=[
            ('fam','Familiar'),
            ('party','Fiesta'),
            ('strategy','Estrategia'),
            ('coop','Cooperativos'),
            ('skill','Destreza y habilidad'),
            ('abstract','Abstractos'),
            ('deduc','Deduccion y faroleo')
        ]
    )
    num_jugadores = fields.Integer('Numero de jugadores recomendados')
    duracion = fields.Integer('Duracion media de partida')

    torneo_id=fields.One2many(
        'clsu_brews_and_boards.torneo', 
        'juego_id', 
        string='Se juega en el torneo '
    )
    reserva_id=fields.One2many(
        'clsu_brews_and_boards.reserva',
        'juego_id',
        string='Reservado a '
    )

class mesa(models.Model):
    _name = 'clsu_brews_and_boards.mesa'
    _description = 'Mesas del local'

    name = fields.Char('Mesas disponibles')
    num_mesa = fields.Char('Codigo')
    capacidad = fields.Integer('Cupo de sillas: ')
    tipo = fields.Boolean(string='Apto para juego', default=True)
    estado = fields.Selection(
        string='Estado', 
        selection=[
            ('free','Libre'),
            ('stop','Ocupada'),
            ('resr','Reservada')
        ]
    )

    reserva_id=fields.Many2one(
        'clsu_brews_and_boards.reserva',
        string='Mesa reservada: '
    )

class reserva(models.Model):
    _name = 'clsu_brews_and_boards.reserva'
    _description = 'Registro de reserva'

    name = fields.Char('Reservas')
    hora = fields.Datetime('Hora de la reserva: ')
    jugadores = fields.Integer('Número de personas para la reserva: ')

    jugador_id=fields.Many2one(
        'clsu_brews_and_boards.jugador', 
        string="Reservado para: "
    )
    juego_id=fields.Many2one(
        'clsu_brews_and_boards.juego',
        string='Juego reservado '
    )
    mesa_id=fields.One2many(
        'clsu_brews_and_boards.mesa',
        'reserva_id',
        string='Reservado a '
    )
