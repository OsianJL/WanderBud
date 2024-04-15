"""empty message

<<<<<<<< HEAD:migrations/versions/f649462a100b_.py
Revision ID: f649462a100b
Revises: 
Create Date: 2024-04-13 17:42:54.362217
========
Revision ID: 046ab127c55b
Revises: 
Create Date: 2024-04-13 12:48:48.357808
>>>>>>>> a638f4ab608777217e58bda363ad2d1b2ba113fc:migrations/versions/046ab127c55b_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/f649462a100b_.py
revision = 'f649462a100b'
========
revision = '046ab127c55b'
>>>>>>>> a638f4ab608777217e58bda363ad2d1b2ba113fc:migrations/versions/046ab127c55b_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('location', sa.String(length=250), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('Planned', 'Completed', 'Canceled', 'In Progress', name='status'), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('budget_per_person', sa.Float(), nullable=True),
    sa.Column('event_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_type_id'], ['event_type.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user__profile',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('ubication', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('event__chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event__member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('petition__chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_petition', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['id_petition'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('petition__chat')
    op.drop_table('event__member')
    op.drop_table('event__chat')
    op.drop_table('user__profile')
    op.drop_table('event')
    op.drop_table('user')
    op.drop_table('event_type')
    # ### end Alembic commands ###
