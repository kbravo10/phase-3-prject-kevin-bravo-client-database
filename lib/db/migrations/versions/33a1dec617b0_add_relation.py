"""add relation

Revision ID: 33a1dec617b0
Revises: 3bc3b5b5336d
Create Date: 2023-08-15 17:52:02.310625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33a1dec617b0'
down_revision: Union[str, None] = '3bc3b5b5336d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clent_medication',
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('medication_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['medication_id'], ['medications.id'], ),
    sa.PrimaryKeyConstraint('client_id', 'medication_id')
    )
    op.create_table('med_times',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_slot', sa.String(), nullable=True),
    sa.Column('dose', sa.String(), nullable=True),
    sa.Column('signed_off', sa.DateTime(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('medication_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['medication_id'], ['medications.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('doctors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('email', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('phone_number', sa.String(), nullable=True))

    with op.batch_alter_table('medications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('medication_use', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('med_type', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medications', schema=None) as batch_op:
        batch_op.drop_column('med_type')
        batch_op.drop_column('medication_use')
        batch_op.drop_column('name')

    with op.batch_alter_table('doctors', schema=None) as batch_op:
        batch_op.drop_column('phone_number')
        batch_op.drop_column('email')
        batch_op.drop_column('name')

    op.drop_table('med_times')
    op.drop_table('clent_medication')
    # ### end Alembic commands ###