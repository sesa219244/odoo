# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Modelo tienda
class barrio1_tienda(models.Model):
    _name = 'barrio1.tienda'

    # Campos del modelo tienda
    name = fields.Text(string="Nombre",required=True,help="")
    fecha_apertura = fields.Date(string="Fecha de apertura",required=False,help="")
    tamaño = fields.Selection([('0','Pequeña'),('1','Mediana'),('2','Grande')],default='0',string="Tamaño",required=True,help="")
    calificacion = fields.Float(digits=(2,2),string="Nota media",required=False,help="")
    # Campos calculados
    aforo = fields.Text(string="Aforo",compute="_metodoAforo",store=False,help="")
    recomendacion = fields.Text(string="Recomendación",compute="_metodoRecomendacion",store=False,help="")
    # Campos relacionados
    # Una tienda puede tener muchos envios
    envios = fields.One2many("barrio1.envio","tiendas",string="Envíos")


    # _metodoAforo
    @api.depends('tamaño')
    def _metodoAforo(self):
        for record in self:
            if record.tamaño == '0':
                record.aforo = 'Entre 1 y 10 personas'
            elif record.tamaño == '1':
                record.aforo = 'Entre 10 y 30 personas'
            elif record.tamaño == '2':
                record.aforo = 'Entre 30 y 50 personas'
            else:
                record.aforo = ''

    # _metodoRecomendacion
    @api.depends('calificacion')
    def _metodoRecomendacion(self):
        for record in self:
            if record.calificacion < 5:
                record.recomendacion = 'No recomendada'
            elif record.calificacion >= 5 and record.calificacion < 7:
                record.recomendacion = 'Es una buena opción'
            elif record.calificacion >=7 and record.calificacion <= 10:
                record.recomendacion = 'Muy recomendable y valorada por sus clientes'
            else:
                record.recomendacion = 'Error, la nota media excede de la nota máxima'


# Modelo envio
class barrio1_envio(models.Model):
    _name = 'barrio1.envio'

    # Campos del modelo envio
    nombre = fields.Text(string="Nombre",required=True,help="")
    direccion = fields.Text(string="Dirección",required=False,help="")
    telefono = fields.Text(string="Teléfono",required=False,help="")
    eficiencia = fields.Char(string="Eficiencia de los envíos",size=1,required=True,help="")
    # Campo calculados
    comentarios = fields.Text(string="Comentarios",compute="_metodoComentarios",store=False,help="")
    # Campos relacionados
    # Muchos envios pueden estar en una tienda
    tiendas = fields.Many2one("barrio1.tienda",string="Tiendas")

    # _metodoComentarios
    @api.depends('eficiencia')
    def _metodoComentarios(self):
        for record in self:
            if record.eficiencia == 'A':
                record.comentarios = 'Es un envío muy eficiente'
            elif record.eficiencia == 'B':
                record.comentarios = 'Es un envío eficiente'
            elif record.eficiencia == 'C':
                record.comentarios = 'Es un envío poco eficiente'
            elif record.eficiencia == 'D':
                record.comentarios = 'Es un envío muy poco eficiente'
            else:
                record.comentarios = 'Error, la eficiencia no es correcta'
