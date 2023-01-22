# -*- coding: utf-8 -*-

from odoo import models, fields, api

class biblio_libreria(models.Model):
    _name = 'biblio.libreria'

    titulo = fields.Text(string="Título",required=True,help="")
    autor = fields.Text(string="Autor",required=True,help="")
    isbn = fields.Text(string="ISBN",required=True,help="")
    referencia = fields.Char(string="Referencia",required=True,size=5)
    tematica = fields.Selection(
        [('1','Novela Histórica'),
        ('2','Fantasia'),
        ('3','Terror'),
        ('4','Drama'),
        ('5','Novela narrativa')],
        default='5',string="Temática",required=True)
    valoracion = fields.Float(digits=(2,2),string="Valoración",required=True)
    recomendacion = fields.Text(string="Recomendación",compute="_metodoRecomendacion",store=False)
    editorial = fields.Many2one("biblio.editoriales",string="Editorial")

    @api.depends('valoracion')
    def _metodoRecomendacion(self):
        for record in self:
            if record.valoracion <= 2:
                record.recomendacion = 'El libro no es nada recomendable'
            elif record.valoracion > 2 and record.valoracion < 5:
                record.recomendacion = 'El libro no es recomendable'
            elif record.valoracion >= 5 and record.valoracion < 7:
                record.recomendacion = 'El libro es algo recomendable'
            elif record.valoracion >= 7 and record.valoracion < 9:
                record.recomendacion = 'El libro es recomendable'
            else:
                record.recomendacion = 'El libro es muy recomendable'


class biblio_editoriales(models.Model):
    _name = 'biblio.editoriales'

    name = fields.Text(string="Nombre",required=True)
    facturacion = fields.Selection(
        [('1','Menos de 1 millón de euros'),
        ('2','Entre 1 y 5 millones de euros'),
        ('3','Entre 5 y 10 millones de euros'),
        ('4','Mas de 10 millones de euros')],
        default='1',string="Facturación",required=True)
    observacion = fields.Text(string="Observación",compute="_metodoObservacion",store=False)
    libros = fields.One2many("biblio.libreria","editorial",string="Libros")

    @api.depends('facturacion')
    def _metodoObservacion(self):
        for record in self:
            if record.facturacion == '1':
                record.observacion = 'Empresa pequeña'
            elif record.facturacion == '2':
                record.observacion = 'Empresa pequeña con progresión'
            elif record.facturacion == '3':
                record.observacion = 'Empresa media'
            else:
                record.observacion = 'Empresa grande'