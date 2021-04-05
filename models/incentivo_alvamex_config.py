from odoo import api, fields, models

class IncentivosAlvamexConfiguracion(models.Model):
	_name = "incentivo.alvamex.configuracion"

	#CONFIGURACION DE EQUIPOS DE VACUNACION
	incentivo_7d = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo7d_id', String="7 Dias")
	incentivo_3s = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo3s_id', String="3 Semanas")
	incentivo_8s = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo8s_id', String="8 Semanas")
	incentivo_12s = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo12s_id', String="12 Semanas")
	incentivo_16s = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo16s_id', String="16 Semanas")
	incentivo_subcutaneo = fields.One2many('incentivo.vacunacion.configuracion', 'incentivosub_id', String="SubCutaneo")
	#CONFIGURACION DE INCENTIVOS DE VACUNACION
	incentivo_personal_7d = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo7d_personal_id', String="7 Dias")
	incentivo_personal_3s = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo3s_personal_id', String="3 Semanas")
	incentivo_personal_8s = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo8s_personal_id', String="8 Semanas")
	incentivo_personal_12s = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo12s_personal_id', String="12 Semanas")
	incentivo_personal_16s = fields.One2many('incentivo.vacunacion.configuracion', 'incentivo16s_personal_id', String="16 Semanas")
	incentivo_personal_subcutaneo = fields.One2many('incentivo.vacunacion.configuracion', 'incentivosub_personal_id', String="SubCutaneo")

	def save(self):
		return True

class IncentivosVacunacionConfiguracion(models.Model):
	_name = "incentivo.vacunacion.configuracion"

	empleado_id = fields.Many2one('gp.partner', String="Empleado")
	puesto = fields.Selection([('aplicador','Aplicador'),('sacador','Sacador')], String="Puesto")
	tipo_incentivo = fields.Char(String="Tipo Incentivo")
	incentivo = fields.Float(String="Incentivo")
	cantidad = fields.Integer(String="Cantidad")
	incentivo7d_id = fields.Many2one('incentivo.alvamex.configuracion', String="Incentivo")
	incentivo3s_id = fields.Many2one('incentivo.alvamex.configuracion', String="Incentivo")
	incentivo8s_id = fields.Many2one('incentivo.alvamex.configuracion', String="Incentivo")
	incentivo12s_id = fields.Many2one('incentivo.alvamex.configuracion', String="Incentivo")
	incentivo16s_id = fields.Many2one('incentivo.alvamex.configuracion', String="Incentivo")
	incentivosub_id = fields.Many2one('incentivo.alvamex.configuracion', String="Incentivo")

	incentivo7d_personal_id = fields.Many2one('incentivo.alvamex.configuracion', String="Equipos")
	incentivo3s_personal_id = fields.Many2one('incentivo.alvamex.configuracion', String="Equipos")
	incentivo8s_personal_id = fields.Many2one('incentivo.alvamex.configuracion', String="Equipos")
	incentivo12s_personal_id = fields.Many2one('incentivo.alvamex.configuracion', String="Equipos")
	incentivo16s_personal_id = fields.Many2one('incentivo.alvamex.configuracion', String="Equipos")
	incentivosub_personal_id = fields.Many2one('incentivo.alvamex.configuracion', String="Equipos")

	# @api.multi
	# def _empleado(self):
	# 	for r in self: