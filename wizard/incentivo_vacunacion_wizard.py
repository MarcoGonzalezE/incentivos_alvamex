from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
import datetime

class IncentivoAlvamexWizard(models.TransientModel):
	_name = 'incentivo.alvamex.wizard'
	_description = "Reporte Inventivos"

	def lineas(self):
		incentivos_ids = []
		incentivos_totales = []
		incentivos = self.env['incentivo.alvamex.vacunacion'].browse(self.env.context.get('active_ids'))
		#incentivos_lineas = self.env['incentivo.alvamex.vacunacion.lineas'].search([['id','in', incentivos.incentivo_7d.ids],['id','in', incentivos.incentivo_3s.ids]])
		for i in incentivos:
			if i.incentivo_7d:
				for s in i.incentivo_7d:
					incentivos_ids.append([(s.empleado_id.name),(s.incentivo)])
			if i.incentivo_3s:
				for s in i.incentivo_3s:
					incentivos_ids.append([(s.empleado_id.name),(s.incentivo)])
			if i.incentivo_8s:
				for s in i.incentivo_8s:
					incentivos_ids.append([(s.empleado_id.name),(s.incentivo)])
			if i.incentivo_12s:
				for s in i.incentivo_12s:
					incentivos_ids.append([(s.empleado_id.name),(s.incentivo)])
			if i.incentivo_16s:
				for s in i.incentivo_16s:
					incentivos_ids.append([(s.empleado_id.name),(s.incentivo)])
			if i.incentivo_subcutaneo:
				for s in i.incentivo_subcutaneo:
					incentivos_ids.append([(s.empleado_id.name),(s.incentivo)])
		incentivos_ids.sort()

		#SUMA DE INCENTIVOS POR EMPLEADO
		flag = incentivos_ids[0][0]
		total = 0
		for i in incentivos_ids:
			if i[0] == flag:
				total = i[1] + total
			if i[0] != flag:
				incentivos_totales.append((0,0,{'empleado':flag,'incentivo_total':total}))
				flag = i[0]
				total = 0
		incentivos_totales.append((0, 0, {'empleado': flag, 'incentivo_total': total}))
		return incentivos_totales

	def fecha_inicial(self):
		incentivos_ids = []
		incentivos = self.env['incentivo.alvamex.vacunacion'].browse(self.env.context.get('active_ids'))
		for i in incentivos:
			incentivos_ids.append([(i.fecha)])
		incentivos_ids.sort()
		return incentivos_ids[0][0]

	def fecha_final(self):
		incentivos_ids = []
		incentivos = self.env['incentivo.alvamex.vacunacion'].browse(self.env.context.get('active_ids'))
		for i in incentivos:
			incentivos_ids.append([(i.fecha)])
		incentivos_ids.sort()
		return incentivos_ids[len(incentivos_ids)-1][0]

	fecha_inicio = fields.Date(string="Fecha Inicio", default=fecha_inicial)
	fecha_final = fields.Date(string="Fecha Final", default=fecha_final)
	responsable = fields.Char(String="Responsable")
	reporte_lineas = fields.One2many('incentivo.alvamex.wizard.lineas', 'reporte_id', String="Lineas de Reporte", default=lineas)

	@api.multi
	def imprimir(self):
		return self.env['report'].get_action(self, 'incentivos_alvamex.reporte_incentivos_vacunacion_document')

	@api.multi
	def reporte(self):
		incentivos = self.env['incentivo.alvamex.vacunacion'].browse(self.env.context.get('active_ids'))
		for r in self:
			query = """SELECT empleado_id as empleado, sum(cantidad) as incentivo
						from incentivo_alvamex_vacunacion_lineas
						where incentivo7d_id = 5
						OR incentivo3s_id = 5
						OR incentivo8s_id = 5
						OR incentivo12s_id = 5
						OR incentivo16s_id = 5
						OR incentivosub_id = 5
						group by empleado_id
						order by empleado_id asc;"""
			params = [incentivos]
			r.env.cr.execute(query, tuple(params))
			res = r.env.cr.fetchone()
			print(res)

class InventivosAlvamexWizardLineas(models.TransientModel):
	_name = 'incentivo.alvamex.wizard.lineas'
	_description = "Lineas de Reporte Vacunacion"

	reporte_id = fields.Many2one('incentivo.alvamex.wizard', string="Reporte")
	empleado = fields.Char(String="Empleado")
	# granja = fields.Char(String="Granja")
	# equipo = fields.Selection([('7dias', '7 Dias'),
	# 							('3semanas', '3 Semanas'),
	# 							('8semanas', '8 Semanas'),
	# 							('12semanas', '12 Semanas'),
	# 							('16semanas', '16 Semanas'),
	# 							('manejo_sub', 'Manejo Subcutaneo')], String="Equipo")
	# puesto = fields.Selection([('aplicador', 'Aplicador'), ('sacador', 'Sacador')], String="Puesto")
	# incentivo = fields.Float(String="Incentivo")
	incentivo_total = fields.Float(String="Incentivo Total")