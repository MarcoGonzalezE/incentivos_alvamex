# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class IncentivoAlvamexVacunacion(models.Model):
    _name = 'incentivo.alvamex.vacunacion'
    _rec_name = "fecha"

    @api.model
    def default_7d(self):
        e7d_ids = []
        equipos = self.env['incentivo.alvamex.configuracion'].search([])
        for e in equipos.incentivo_personal_7d:
            e7d_ids.append((0, 0, {'empleado_id': e.empleado_id.id}))
        return e7d_ids

    @api.model
    def default_3s(self):
        e3s_ids = []
        equipos = self.env['incentivo.alvamex.configuracion'].search([])
        for e in equipos.incentivo_personal_3s:
            e3s_ids.append((0, 0, {'empleado_id': e.empleado_id.id, 'puesto': e.puesto}))
        return e3s_ids

    @api.model
    def default_8s(self):
        e8s_ids = []
        equipos = self.env['incentivo.alvamex.configuracion'].search([])
        for e in equipos.incentivo_personal_8s:
            e8s_ids.append((0, 0, {'empleado_id': e.empleado_id.id, 'puesto': e.puesto}))
        return e8s_ids

    @api.model
    def default_12s(self):
        e12s_ids = []
        equipos = self.env['incentivo.alvamex.configuracion'].search([])
        for e in equipos.incentivo_personal_12s:
            e12s_ids.append((0, 0, {'empleado_id': e.empleado_id.id, 'puesto': e.puesto}))
        return e12s_ids

    @api.model
    def default_16s(self):
        e16s_ids = []
        equipos = self.env['incentivo.alvamex.configuracion'].search([])
        for e in equipos.incentivo_personal_16s:
            e16s_ids.append((0, 0, {'empleado_id': e.empleado_id.id, 'puesto': e.puesto}))
        return e16s_ids

    @api.model
    def default_sub(self):
        esub_ids = []
        equipos = self.env['incentivo.alvamex.configuracion'].search([])
        for e in equipos.incentivo_personal_subcutaneo:
            esub_ids.append((0, 0, {'empleado_id': e.empleado_id.id, 'puesto': e.puesto}))
        return esub_ids

    fecha = fields.Date(default=fields.Date.context_today, string="Fecha")
    responsable = fields.Char(String="Responsable")
    incentivo_7d = fields.One2many('incentivo.alvamex.vacunacion.lineas', 'incentivo7d_id', String="7 Dias", default=default_7d)
    incentivo_3s = fields.One2many('incentivo.alvamex.vacunacion.lineas', 'incentivo3s_id', String="3 Semanas", default=default_3s)
    incentivo_8s = fields.One2many('incentivo.alvamex.vacunacion.lineas', 'incentivo8s_id', String="8 Semanas", default=default_8s)
    incentivo_12s = fields.One2many('incentivo.alvamex.vacunacion.lineas', 'incentivo12s_id', String="12 Semanas", default=default_12s)
    incentivo_16s = fields.One2many('incentivo.alvamex.vacunacion.lineas', 'incentivo16s_id', String="16 Semanas", default=default_16s)
    incentivo_subcutaneo = fields.One2many('incentivo.alvamex.vacunacion.lineas', 'incentivosub_id', String="SubCutaneo", default=default_sub)

class IncentivoAlvamexVacunacionLineas(models.Model):
    _name = 'incentivo.alvamex.vacunacion.lineas'

    empleado_id = fields.Many2one('gp.partner', String="Empleado")
    puesto = fields.Selection([('aplicador', 'Aplicador'), ('sacador', 'Sacador')], String="Puesto")
    cantidad = fields.Integer(String="Cantidad")
    granja_id = fields.Many2one('gp.farm', String="Granja")
    incentivo = fields.Float(String="Incentivo", compute="incentivos_cantidad")
    incentivo7d_id = fields.Many2one('incentivo.alvamex.vacunacion', String="Incentivo")
    incentivo3s_id = fields.Many2one('incentivo.alvamex.vacunacion', String="Incentivo")
    incentivo8s_id = fields.Many2one('incentivo.alvamex.vacunacion', String="Incentivo")
    incentivo12s_id = fields.Many2one('incentivo.alvamex.vacunacion', String="Incentivo")
    incentivo16s_id = fields.Many2one('incentivo.alvamex.vacunacion', String="Incentivo")
    incentivosub_id = fields.Many2one('incentivo.alvamex.vacunacion', String="Incentivo")

    @api.onchange('granja_id','cantidad')
    def incentivos_cantidad(self):       
        for r in self:
            valor = self.env['incentivo.alvamex.configuracion'].search([])
            flag = False
            if r.incentivo7d_id:
                for x in valor.incentivo_7d:
                    if r.cantidad >= x.cantidad:
                        r.incentivo = x.incentivo
                        flag = True
            if r.incentivo3s_id:
                for x in valor.incentivo_3s:
                    if r.cantidad >= x.cantidad:
                        r.incentivo = x.incentivo
                        flag = True
            if r.incentivo8s_id:
                for x in valor.incentivo_8s:
                    if r.cantidad >= x.cantidad:
                        r.incentivo = x.incentivo
                        flag = True
            if r.incentivo12s_id:
                for x in valor.incentivo_12s:
                    if r.cantidad >= x.cantidad:
                        r.incentivo = x.incentivo
                        flag = True
            if r.incentivo16s_id:
                for x in valor.incentivo_16s:
                    if r.cantidad >= x.cantidad:
                        r.incentivo = x.incentivo
                        flag = True
            if r.incentivosub_id:
                for x in valor.incentivo_subcutaneo:
                    if r.cantidad >= x.cantidad:
                        for g in x.granja_ids:
                            if r.granja_id.name == g.name:
                                r.incentivo = x.incentivo
                        flag = True
            if flag == False:
                r.incentivo = 0