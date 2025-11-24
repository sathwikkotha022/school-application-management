<%!
    import re

    # fmt: off
    NAMESPACE = "alembic.runtime.migration"
    REVISION_SCRIPT_TOKEN = "revision"
    DOWN_REVISION_SCRIPT_TOKEN = "down_revision"
    BRANCH_LABEL_SCRIPT_TOKEN = "branch_labels"
    DEPENDS_ON_SCRIPT_TOKEN = "depends_on"
    CREATE_DATE_SCRIPT_TOKEN = "create_date"
    REVISION_SCRIPT_TEMPLATE = f"""
\"""{{message}}

Revision ID: {{revision}}
Revises: {{up_revision}}
Create Date: {{create_date}}

\"""


def upgrade() -> None:
    {{upgrades if upgrades else "pass"}}


def downgrade() -> None:
    {{downgrades if downgrades else "pass"}}
"""

    # fmt: on
%>
<%!
    from alembic.util import sqla_compat
%>
<%!
    def process_revision_directives(context, revision, directives):
        if getattr(directives[0], 'upgrade_ops', None) is not None:
            script = directives[0].upgrade_ops
            if script.modifies_autoincrement_columns or script.modifies_nullable_columns:
                context.config.set_section_option(
                    context.config.config_ini_section,
                    "sqlalchemy.warn_20",
                    "true"
                )
        super_process_revision_directives(context, revision, directives)
%>
<%!
    def render_item(obj, autogen_context):
        """Apply rendering functions to a particular object."""
        if isinstance(obj, str):
            return obj
        else:
            return render._render_item(obj, autogen_context)
%>
<%!
    def render_as_batch(context, directives):
        if not directives:
            return
        directive = directives[0]
        if directive.upgrade_ops.is_empty:
            return
        if not directive.upgrade_ops.batch:
            return
        return render_as_batch._render_as_batch(directive.upgrade_ops, autogen_context)
%>
<%!
    def render_column(type_, col, autogen_context):
        return render._render_column(type_, col, autogen_context)
%>
<%!
    def render_constraint(constraint, autogen_context):
        return render._render_constraint(constraint, autogen_context)
%>
<%!
    def render_index(index, autogen_context):
        return render._render_index(index, autogen_context)
%>
<%!
    def render_table(table, autogen_context):
        return render._render_table(table, autogen_context)
%>
<%!
    def render_type(type_, col, autogen_context):
        return render._render_type(type_, col, autogen_context)
%>
${REVISION_SCRIPT_TEMPLATE}
