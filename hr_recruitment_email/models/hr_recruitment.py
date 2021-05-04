# -*- coding: utf-8 -*--
# © Martin Reisenhofer <martin@reisenhofer.biz>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Applicant(models.Model):
    _inherit = 'hr.applicant'

    next_meeting = fields.Datetime(string='Next Meeting')

    def _track_template(self, changes):
        res = super(Applicant, self)._track_template(changes)
        applicant = self[0]
        if 'refuse_reason_id' in changes and applicant.refuse_reason_id.template_id:
            res['stage_id'] = (applicant.refuse_reason_id.template_id, {
                'auto_delete_message': True,
                'subtype_id': self.env['ir.model.data'].xmlid_to_res_id('mail.mt_note'),
                'email_layout_xmlid': 'mail.mail_notification_light'
            })
        return res


class ApplicantRefuseReason(models.Model):
    _inherit = 'hr.applicant.refuse.reason'

    template_id = fields.Many2one(
        'mail.template', "Email Template",
        help="If set, a message is posted on the applicant using the template when the applicant was refused.")

