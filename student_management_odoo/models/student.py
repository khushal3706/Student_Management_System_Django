from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    enrollment_no = fields.Char(string='Enrollment No', required=True)
    email = fields.Char(string='Email')
    course_id = fields.Many2one('student.course', string='Course')

    def demo_orm_operations(self):
        """
        Demonstrates the use of ORM methods: create, write, search, unlink
        """
        _logger.info("--- Starting ORM Demo ---")
        
        # 1. CREATE
        new_student = self.env['student.student'].create({
            'name': 'Demo User',
            'enrollment_no': 'DEMO001',
            'email': 'demo@example.com'
        })
        _logger.info(f"Created student: {new_student.name} with ID {new_student.id}")
        
        # 2. SEARCH
        found_student = self.env['student.student'].search([('enrollment_no', '=', 'DEMO001')], limit=1)
        _logger.info(f"Searched for DEMO001, found: {found_student.name}")
        
        # 3. WRITE
        if found_student:
            found_student.write({'name': 'Demo User Updated'})
            _logger.info(f"Updated student name to: {found_student.name}")
            
        # 4. UNLINK (Delete)
        if found_student:
            found_student.unlink()
            _logger.info("Deleted the demo student.")
            
        _logger.info("--- Finished ORM Demo ---")
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'ORM Demo Complete',
                'message': 'Check the Odoo server logs for the output of create, read, write, and unlink operations.',
                'type': 'success',
                'sticky': False,
            }
        }
