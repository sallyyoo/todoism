"""mission model add is_show

Revision ID: 0aae0727099a
Revises: 
Create Date: 2019-01-07 09:00:20.680050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aae0727099a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_log_timestamp', table_name='log')
    op.drop_table('log')
    op.drop_index('ix_todo_list_created_at', table_name='todo_list')
    op.drop_table('todo_list')
    op.drop_table('mission_category')
    op.drop_table('task')
    op.drop_index('ix_today_created_at', table_name='today')
    op.drop_table('today')
    op.drop_table('user')
    op.drop_table('score')
    op.add_column('mission', sa.Column('is_show', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mission', 'is_show')
    op.create_table('score',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('score_id', sa.INTEGER(), nullable=True),
    sa.Column('score', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('today',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('score', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_today_created_at', 'today', ['created_at'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.VARCHAR(length=50), nullable=True),
    sa.Column('status', sa.INTEGER(), nullable=True),
    sa.Column('todo_list_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['todo_list_id'], ['todo_list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mission_category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('todo_list',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index('ix_todo_list_created_at', 'todo_list', ['created_at'], unique=False)
    op.create_table('log',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('completed_mission', sa.INTEGER(), nullable=True),
    sa.Column('used_time', sa.FLOAT(), nullable=True),
    sa.Column('mission_log_id', sa.INTEGER(), nullable=True),
    sa.Column('mission_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['mission_id'], ['mission.id'], ),
    sa.ForeignKeyConstraint(['mission_log_id'], ['mission_log.log_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_log_timestamp', 'log', ['timestamp'], unique=False)
    # ### end Alembic commands ###
