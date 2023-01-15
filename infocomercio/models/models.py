# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Modelo tienda
class infocomercio_tienda(models.Model):
    _name = 'infocomercio.tienda'

    # Campos del modelo tienda
    name = fields.Text(string="Nombre",required=True,help="Introduce el nombre de la tienda")
    fecha_apertura = fields.Date(string="Fecha de apertura",required=True,help="Introduce la fecha de apertura de la tienda")
    size = fields.Selection([('0','Pequeña'),('1','Mediana'),('2','Grande')],string="Tamaño",default='1',help="Introduce el tamaño de la tienda")
    nota_media = fields.Float(digits=(2,2),string="Valoración",help="Introduce la nota media de la tienda")
    # Campos calculados
    aforo = fields.Text(string="Aforo",compute="_metodoAforo",store=True)
    recomendacion = fields.Text(string="Recomendación",compute="_metodoRecomendacion",store=False)
    # Campo relacionado "MUCHAS tiendas pueden estar en UNA UNICA compañía de transporte"
    compania_envios = fields.Many2one("infocomercio.envio",string="Compañía de transporte")
    # Campo relacionado "MUCHAS tiendas pueden estar en MUCHAS compañías de seguros"
    compania_seguros = fields.Many2many("infocomercio.seguros",string="Registro de seguros")
    
    # _metodoAforo
    @api.depends('size')
    def _metodoAforo(self):
        for r in self:
            if r.size == '0':
                r.aforo = 'Entre 1 y 10 personas'
            elif r.size == '1':
                r.aforo = 'Entre 10 y 30 personas'
            elif r.size == '2':
                r.aforo = 'Mas de 30 personas'
            else:
                r.aforo = ''
    
    # _metodoRecomendacion
    @api.depends('nota_media')
    def _metodoRecomendacion(self):
        for r in self:
            if r.nota_media < 5:
                r.recomendacion = 'No recomendada'
            elif r.nota_media >= 5 and r.nota_media <= 7:
                r.recomendacion = 'Es una buena opción'
            elif r.nota_media  > 7 and r.nota_media <= 10:
                r.recomendacion = 'Muy recomendada y valorada por sus clientes'
            else:
                r.recomendacion = 'Error, la nota media excede la nota máxima'

# Modelo envio
class infocomercio_envio(models.Model):
    _name = 'infocomercio.envio'

    # Campos del modelo envio
    name = fields.Text(string="Nombre",required=True,help="Introduce el nombre de la compañía de tranporte")
    direccion = fields.Text(string="Dirección",help="Introduce la dirección de la compañía de tranporte")
    telefono = fields.Text(string="Teléfono",help="Introduce el teléfono de la compañía de tranporte")
    eficiencia_envios = fields.Char(string="Eficiencia de envios",size=1,help="Introduce el título del libro")
    # Campo relacionado "UNA UNICA compañía de transportes puede tener MUCHAS tiendas"
    lista_tiendas = fields.One2many("infocomercio.tienda","compania_envios",string="Registro de tiendas")
    # Campo relacionado "MUCHAS compañías de transportes pueden tener UN único seguro"
    compania_seguros = fields.Many2one("infocomercio.seguros",string="Compañía de seguros")

# Modelo seguros
class infocomercio_seguros(models.Model):
    _name = 'infocomercio.seguros'

    # Campos del modelo seguro
    name = fields.Text(string="Nombre",required=True,help="Introduce el nombre de la compañía de seguros")
    direccion = fields.Text(string="Dirección",help="Introduce la dirección de la compañía de seguros")
    telefono = fields.Text(string="Teléfono",help="Introduce el teléfono de la compñía de seguros")
    cobertura = fields.Selection([('A','Todo riesgo'),('B','Todo riesgo franquicia baja'),('C','Todo riesgo franquicia media'),('D','Todo riesgo franquicia alta'),('E','Seguro básico')],string="Cobertura de Seguro",default='E',help="Introduce el tipo de cobertura de seguro")
    # Campo calculado
    tipo = fields.Text(string="Tipo",compute="_metodoCobertura",store=False)
    # Campo relacionado "UN Seguro puede tener MUCHAS tiendas"
    lista_tiendas = fields.Many2many("infocomercio.tienda",string="Registro de tiendas")
    # Campo relacionado "UN Seguro puede tener MUCHOS empresas de envios"
    lista_envios = fields.One2many("infocomercio.envio","compania_seguros",string="Registro de Transportistas")
    
    # _metodoCobertura
    @api.depends('cobertura')
    def _metodoCobertura(self):
        for r in self:
            if r.cobertura == 'A':
                r.tipo = 'A'
            elif r.cobertura == 'B':
                r.tipo = 'B'
            elif r.cobertura == 'C':
                r.tipo = 'C'
            elif r.cobertura == 'D':
                r.tipo = 'D'
            elif r.cobertura == 'E':
                r.tipo = 'E'
            else:
                r.tipo = ''
