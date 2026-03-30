from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class StudentCourse(models.Model):
    _name = 'student.course'
    _description = 'Course Information'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    description = fields.Text(string='Description')
