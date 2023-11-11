"""empty message

Revision ID: 3051d11b5732
Revises: 
Create Date: 2023-11-06 20:37:20.311978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3051d11b5732'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cell',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('block_number', sa.Integer(), nullable=False),
    sa.Column('max_capacity', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crime_name', sa.String(length=45), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prisoner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=False),
    sa.Column('last_name', sa.String(length=45), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('prisonercrime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prisoner_id', sa.Integer(), nullable=True),
    sa.Column('crime_id', sa.Integer(), nullable=True),
    sa.Column('cell_id', sa.Integer(), nullable=True),
    sa.Column('date_committed', sa.Date(), nullable=False),
    sa.Column('date_incarcerated', sa.Date(), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['cell_id'], ['cell.id'], ),
    sa.ForeignKeyConstraint(['crime_id'], ['crime.id'], ),
    sa.ForeignKeyConstraint(['prisoner_id'], ['prisoner.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prisonercrime')
    op.drop_table('user')
    op.drop_table('prisoner')
    op.drop_table('crime')
    op.drop_table('cell')
    # ### end Alembic commands ###
