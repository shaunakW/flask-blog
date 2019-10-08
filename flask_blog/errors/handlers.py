from flask import Blueprint, render_template

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@bp.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(405)
def error_405(error):
    return error_404(error)[0], 405

@bp.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500