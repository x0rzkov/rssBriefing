"""initial db migration, including Users table

Revision ID: 1d268c5532f9
Revises: 
Create Date: 2020-01-20 16:23:49.132483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d268c5532f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=2048), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('link', sa.String(length=2048), nullable=True),
    sa.Column('href', sa.String(length=2048), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feed_title'), 'feed', ['title'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('briefing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=2048), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('link', sa.String(length=2048), nullable=False),
    sa.Column('reference', sa.String(length=2048), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('briefing_created', sa.DateTime(), nullable=True),
    sa.Column('guid', sa.String(length=255), nullable=True),
    sa.Column('feed_title', sa.String(length=2048), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['feed_title'], ['feed.title'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_briefing_briefing_created'), 'briefing', ['briefing_created'], unique=False)
    op.create_index(op.f('ix_briefing_title'), 'briefing', ['title'], unique=False)
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=2048), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('link', sa.String(length=2048), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('guid', sa.String(length=255), nullable=True),
    sa.Column('feed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['feed_id'], ['feed.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_created'), 'item', ['created'], unique=False)
    op.create_index(op.f('ix_item_title'), 'item', ['title'], unique=False)
    op.create_table('user_feed',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('feed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['feed_id'], ['feed.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'feed_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_feed')
    op.drop_index(op.f('ix_item_title'), table_name='item')
    op.drop_index(op.f('ix_item_created'), table_name='item')
    op.drop_table('item')
    op.drop_index(op.f('ix_briefing_title'), table_name='briefing')
    op.drop_index(op.f('ix_briefing_briefing_created'), table_name='briefing')
    op.drop_table('briefing')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_feed_title'), table_name='feed')
    op.drop_table('feed')
    # ### end Alembic commands ###
