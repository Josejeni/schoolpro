"""empty message

Revision ID: 0079d65cf6f0
Revises: 96d5c8f97265
Create Date: 2022-09-27 14:26:59.717889

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0079d65cf6f0'
down_revision = '96d5c8f97265'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schoolprofile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('sname', sa.String(), nullable=True),
    sa.Column('post', sa.String(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('pno', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('pcode', sa.Integer(), nullable=True),
    sa.Column('slocation', sa.String(), nullable=True),
    sa.Column('need', sa.String(), nullable=True),
    sa.Column('ayear', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('slevel', sa.String(), nullable=True),
    sa.Column('medium', sa.String(), nullable=True),
    sa.Column('nature', sa.String(), nullable=True),
    sa.Column('tstaff', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('girls', sa.Integer(), nullable=True),
    sa.Column('boys', sa.Integer(), nullable=True),
    sa.Column('students', sa.Integer(), nullable=True),
    sa.Column('nstaff', sa.Integer(), nullable=True),
    sa.Column('cname', sa.String(), nullable=True),
    sa.Column('cpno', sa.Integer(), nullable=True),
    sa.Column('pname', sa.String(), nullable=True),
    sa.Column('pemail', sa.String(), nullable=True),
    sa.Column('ppno', sa.Integer(), nullable=True),
    sa.Column('opno', sa.Integer(), nullable=True),
    sa.Column('institute_govt', sa.String(), nullable=True),
    sa.Column('board_affiliated', sa.String(), nullable=True),
    sa.Column('affiliation_no', sa.Integer(), nullable=True),
    sa.Column('affiliation_year', sa.Integer(), nullable=True),
    sa.Column('affiliation_condition', sa.String(), nullable=True),
    sa.Column('affiliation_cons', sa.Integer(), nullable=True),
    sa.Column('status_certificate', sa.String(), nullable=True),
    sa.Column('hindhu', sa.Integer(), nullable=True),
    sa.Column('cristian', sa.Integer(), nullable=True),
    sa.Column('islam', sa.Integer(), nullable=True),
    sa.Column('others', sa.Integer(), nullable=True),
    sa.Column('non_believers', sa.Integer(), nullable=True),
    sa.Column('fire_certificate', sa.String(), nullable=True),
    sa.Column('sanitation_certificate', sa.String(), nullable=True),
    sa.Column('building_certificate', sa.String(), nullable=True),
    sa.Column('school_owned', sa.String(), nullable=True),
    sa.Column('name_trust', sa.String(), nullable=True),
    sa.Column('registered', sa.String(), nullable=True),
    sa.Column('under_act', sa.String(), nullable=True),
    sa.Column('registration_year', sa.Integer(), nullable=True),
    sa.Column('registration_no', sa.Integer(), nullable=True),
    sa.Column('period_validity', sa.Integer(), nullable=True),
    sa.Column('name_chairman', sa.String(), nullable=True),
    sa.Column('designation', sa.String(), nullable=True),
    sa.Column('address_chairman', sa.String(), nullable=True),
    sa.Column('pno_chairman', sa.String(), nullable=True),
    sa.Column('email_chairman', sa.String(), nullable=True),
    sa.Column('governing', sa.String(), nullable=True),
    sa.Column('members', sa.Integer(), nullable=True),
    sa.Column('tenure', sa.Integer(), nullable=True),
    sa.Column('epcc', sa.String(), nullable=True),
    sa.Column('members_epcc', sa.Integer(), nullable=True),
    sa.Column('epcc_tenure', sa.Integer(), nullable=True),
    sa.Column('pt_executive', sa.String(), nullable=True),
    sa.Column('pt_members', sa.Integer(), nullable=True),
    sa.Column('pt_tenure', sa.Integer(), nullable=True),
    sa.Column('st_councill', sa.String(), nullable=True),
    sa.Column('st_members', sa.Integer(), nullable=True),
    sa.Column('st_tenure', sa.Integer(), nullable=True),
    sa.Column('general_grievance', sa.String(), nullable=True),
    sa.Column('sm_committee', sa.String(), nullable=True),
    sa.Column('cm_committee', sa.String(), nullable=True),
    sa.Column('cm_members', sa.Integer(), nullable=True),
    sa.Column('cm_tenure', sa.Integer(), nullable=True),
    sa.Column('school_building', sa.String(), nullable=True),
    sa.Column('built_area', sa.String(), nullable=True),
    sa.Column('play_area', sa.String(), nullable=True),
    sa.Column('no_building', sa.Integer(), nullable=True),
    sa.Column('provision', sa.String(), nullable=True),
    sa.Column('no_staircases', sa.Integer(), nullable=True),
    sa.Column('no_lift', sa.Integer(), nullable=True),
    sa.Column('class_rooms', sa.Integer(), nullable=True),
    sa.Column('srooms', sa.Integer(), nullable=True),
    sa.Column('plab', sa.Integer(), nullable=True),
    sa.Column('clab', sa.Integer(), nullable=True),
    sa.Column('blab', sa.Integer(), nullable=True),
    sa.Column('mlab', sa.Integer(), nullable=True),
    sa.Column('comlab', sa.Integer(), nullable=True),
    sa.Column('llab', sa.Integer(), nullable=True),
    sa.Column('hslab', sa.Integer(), nullable=True),
    sa.Column('library', sa.Integer(), nullable=True),
    sa.Column('auditorium', sa.Integer(), nullable=True),
    sa.Column('counroom', sa.Integer(), nullable=True),
    sa.Column('parlor', sa.Integer(), nullable=True),
    sa.Column('proom', sa.Integer(), nullable=True),
    sa.Column('sick_room', sa.Integer(), nullable=True),
    sa.Column('canteen', sa.Integer(), nullable=True),
    sa.Column('secroom', sa.Integer(), nullable=True),
    sa.Column('oroom', sa.Integer(), nullable=True),
    sa.Column('stoilet', sa.Integer(), nullable=True),
    sa.Column('std_toilet', sa.Integer(), nullable=True),
    sa.Column('rooms', sa.Integer(), nullable=True),
    sa.Column('spcl_stud', sa.String(), nullable=True),
    sa.Column('wall', sa.String(), nullable=True),
    sa.Column('if_wall', sa.String(), nullable=True),
    sa.Column('cctv', sa.String(), nullable=True),
    sa.Column('ds', sa.String(), nullable=True),
    sa.Column('no_camera', sa.Integer(), nullable=True),
    sa.Column('guard', sa.String(), nullable=True),
    sa.Column('no_guard', sa.Integer(), nullable=True),
    sa.Column('fguard', sa.String(), nullable=True),
    sa.Column('no_fguard', sa.Integer(), nullable=True),
    sa.Column('water', sa.String(), nullable=True),
    sa.Column('drainage', sa.String(), nullable=True),
    sa.Column('mmeals', sa.String(), nullable=True),
    sa.Column('no_buses', sa.Integer(), nullable=True),
    sa.Column('gps', sa.Integer(), nullable=True),
    sa.Column('nola', sa.Integer(), nullable=True),
    sa.Column('first_aid', sa.Integer(), nullable=True),
    sa.Column('no_water', sa.Integer(), nullable=True),
    sa.Column('no_sbus', sa.Integer(), nullable=True),
    sa.Column('free_tran', sa.String(), nullable=True),
    sa.Column('cam_area', sa.String(), nullable=True),
    sa.Column('pas', sa.String(), nullable=True),
    sa.Column('prin_permale', sa.Integer(), nullable=True),
    sa.Column('prin_perfemale', sa.Integer(), nullable=True),
    sa.Column('prin_temmale', sa.Integer(), nullable=True),
    sa.Column('prin_temfemale', sa.Integer(), nullable=True),
    sa.Column('vp_permale', sa.Integer(), nullable=True),
    sa.Column('vp_perfemale', sa.Integer(), nullable=True),
    sa.Column('vp_temmale', sa.Integer(), nullable=True),
    sa.Column('vp_temfemale', sa.Integer(), nullable=True),
    sa.Column('pg_permale', sa.Integer(), nullable=True),
    sa.Column('pg_perfemale', sa.Integer(), nullable=True),
    sa.Column('pg_temmale', sa.Integer(), nullable=True),
    sa.Column('pg_temfemale', sa.Integer(), nullable=True),
    sa.Column('tg_permale', sa.Integer(), nullable=True),
    sa.Column('tg_perfemale', sa.Integer(), nullable=True),
    sa.Column('tg_temmale', sa.Integer(), nullable=True),
    sa.Column('tg_temfemale', sa.Integer(), nullable=True),
    sa.Column('prt_permale', sa.Integer(), nullable=True),
    sa.Column('prt_perfemale', sa.Integer(), nullable=True),
    sa.Column('prt_temmale', sa.Integer(), nullable=True),
    sa.Column('prt_temfemale', sa.Integer(), nullable=True),
    sa.Column('nt_permale', sa.Integer(), nullable=True),
    sa.Column('nt_perfemale', sa.Integer(), nullable=True),
    sa.Column('nt_temmale', sa.Integer(), nullable=True),
    sa.Column('nt_temfemale', sa.Integer(), nullable=True),
    sa.Column('lib_permale', sa.Integer(), nullable=True),
    sa.Column('lib_perfemale', sa.Integer(), nullable=True),
    sa.Column('lib_temmale', sa.Integer(), nullable=True),
    sa.Column('lib_temfemale', sa.Integer(), nullable=True),
    sa.Column('art_permale', sa.Integer(), nullable=True),
    sa.Column('art_perfemale', sa.Integer(), nullable=True),
    sa.Column('art_temmale', sa.Integer(), nullable=True),
    sa.Column('art_temfemale', sa.Integer(), nullable=True),
    sa.Column('coun_permale', sa.Integer(), nullable=True),
    sa.Column('coun_perfemale', sa.Integer(), nullable=True),
    sa.Column('coun_temmale', sa.Integer(), nullable=True),
    sa.Column('coun_temfemale', sa.Integer(), nullable=True),
    sa.Column('comlit_permale', sa.Integer(), nullable=True),
    sa.Column('comlit_perfemale', sa.Integer(), nullable=True),
    sa.Column('comlit_temmale', sa.Integer(), nullable=True),
    sa.Column('comlit_temfemale', sa.Integer(), nullable=True),
    sa.Column('faithmin_permale', sa.Integer(), nullable=True),
    sa.Column('faithmin_perfemale', sa.Integer(), nullable=True),
    sa.Column('faithmin_temmale', sa.Integer(), nullable=True),
    sa.Column('faithmin_temfemale', sa.Integer(), nullable=True),
    sa.Column('nurse_permale', sa.Integer(), nullable=True),
    sa.Column('nurse_perfemale', sa.Integer(), nullable=True),
    sa.Column('nurse_temmale', sa.Integer(), nullable=True),
    sa.Column('nurse_temfemale', sa.Integer(), nullable=True),
    sa.Column('pt_permale', sa.Integer(), nullable=True),
    sa.Column('pt_perfemale', sa.Integer(), nullable=True),
    sa.Column('pt_temmale', sa.Integer(), nullable=True),
    sa.Column('pt_temfemale', sa.Integer(), nullable=True),
    sa.Column('om_per', sa.Integer(), nullable=True),
    sa.Column('om_tem', sa.Integer(), nullable=True),
    sa.Column('om_part', sa.Integer(), nullable=True),
    sa.Column('oa_per', sa.Integer(), nullable=True),
    sa.Column('oa_tem', sa.Integer(), nullable=True),
    sa.Column('oa_part', sa.Integer(), nullable=True),
    sa.Column('clerk_per', sa.Integer(), nullable=True),
    sa.Column('clerk_tem', sa.Integer(), nullable=True),
    sa.Column('clerk_part', sa.Integer(), nullable=True),
    sa.Column('lab_per', sa.Integer(), nullable=True),
    sa.Column('lab_tem', sa.Integer(), nullable=True),
    sa.Column('lab_part', sa.Integer(), nullable=True),
    sa.Column('acc_per', sa.Integer(), nullable=True),
    sa.Column('acc_tem', sa.Integer(), nullable=True),
    sa.Column('acc_part', sa.Integer(), nullable=True),
    sa.Column('peon_per', sa.Integer(), nullable=True),
    sa.Column('peon_tem', sa.Integer(), nullable=True),
    sa.Column('peon_part', sa.Integer(), nullable=True),
    sa.Column('other_per', sa.Integer(), nullable=True),
    sa.Column('other_tem', sa.Integer(), nullable=True),
    sa.Column('other_part', sa.Integer(), nullable=True),
    sa.Column('ut_permale', sa.Integer(), nullable=True),
    sa.Column('ut_perfemale', sa.Integer(), nullable=True),
    sa.Column('ut_temmale', sa.Integer(), nullable=True),
    sa.Column('ut_temfemale', sa.Integer(), nullable=True),
    sa.Column('no_curricular_carried', sa.Integer(), nullable=True),
    sa.Column('no_groups', sa.Integer(), nullable=True),
    sa.Column('no_community', sa.Integer(), nullable=True),
    sa.Column('last_school', sa.Integer(), nullable=True),
    sa.Column('last_zonal', sa.Integer(), nullable=True),
    sa.Column('last_district', sa.Integer(), nullable=True),
    sa.Column('last_state', sa.Integer(), nullable=True),
    sa.Column('last_national', sa.Integer(), nullable=True),
    sa.Column('last_international', sa.Integer(), nullable=True),
    sa.Column('com_school', sa.Integer(), nullable=True),
    sa.Column('com_zonal', sa.Integer(), nullable=True),
    sa.Column('com_district', sa.Integer(), nullable=True),
    sa.Column('com_state', sa.Integer(), nullable=True),
    sa.Column('com_national', sa.Integer(), nullable=True),
    sa.Column('com_international', sa.Integer(), nullable=True),
    sa.Column('sclpro_school', sa.Integer(), nullable=True),
    sa.Column('sclpro_zonal', sa.Integer(), nullable=True),
    sa.Column('sclpro_district', sa.Integer(), nullable=True),
    sa.Column('sclpro_state', sa.Integer(), nullable=True),
    sa.Column('sclpro_national', sa.Integer(), nullable=True),
    sa.Column('sclpro_international', sa.Integer(), nullable=True),
    sa.Column('year_begin', sa.String(), nullable=True),
    sa.Column('year_end', sa.String(), nullable=True),
    sa.Column('workday_21_22', sa.Integer(), nullable=True),
    sa.Column('workday_20_21', sa.Integer(), nullable=True),
    sa.Column('workday_19_20', sa.Integer(), nullable=True),
    sa.Column('hours_21_22', sa.Integer(), nullable=True),
    sa.Column('hours_20_21', sa.Integer(), nullable=True),
    sa.Column('hours_19_20', sa.Integer(), nullable=True),
    sa.Column('instructional_hours_21_22', sa.Integer(), nullable=True),
    sa.Column('instructional_hours_20_21', sa.Integer(), nullable=True),
    sa.Column('instructional_hours_19_20', sa.Integer(), nullable=True),
    sa.Column('non_instructional_hours_21_22', sa.Integer(), nullable=True),
    sa.Column('non_instructional_hours_20_21', sa.Integer(), nullable=True),
    sa.Column('non_instructional_hours_19_20', sa.Integer(), nullable=True),
    sa.Column('holidays_21_22', sa.Integer(), nullable=True),
    sa.Column('holidays_20_21', sa.Integer(), nullable=True),
    sa.Column('holidays_19_20', sa.Integer(), nullable=True),
    sa.Column('sub_week', sa.Integer(), nullable=True),
    sa.Column('moral_week', sa.Integer(), nullable=True),
    sa.Column('duration_teaching', sa.Integer(), nullable=True),
    sa.Column('no_clubs', sa.Integer(), nullable=True),
    sa.Column('summer_from', sa.Time(), nullable=True),
    sa.Column('summer_to', sa.Time(), nullable=True),
    sa.Column('winter_from', sa.Time(), nullable=True),
    sa.Column('winter_to', sa.Time(), nullable=True),
    sa.Column('shifts', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['user_name'], ['register.user_name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('general_info')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('general_info',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('sname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('post', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('district', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pno', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pcode', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('slocation', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('need', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ayear', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('slevel', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('medium', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('nature', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tstaff', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('girls', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('boys', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('students', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nstaff', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cpno', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pemail', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ppno', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('opno', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('institute_govt', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('board_affiliated', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('affiliation_no', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('affiliation_year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('affiliation_condition', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('affiliation_cons', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status_certificate', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('hindhu', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cristian', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('islam', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('others', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('non_believers', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('fire_certificate', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('sanitation_certificate', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('building_certificate', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('school_owned', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('name_trust', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('registered', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('under_act', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('registration_year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('registration_no', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('period_validity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name_chairman', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('designation', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('address_chairman', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pno_chairman', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email_chairman', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('governing', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('members', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tenure', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('epcc', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('members_epcc', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('epcc_tenure', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pt_executive', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pt_members', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pt_tenure', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('st_councill', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('st_members', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('st_tenure', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('general_grievance', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('sm_committee', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cm_committee', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cm_members', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cm_tenure', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('school_building', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('built_area', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('play_area', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('no_building', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('provision', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('no_staircases', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('no_lift', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('class_rooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('plab', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('clab', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('blab', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('mlab', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comlab', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('llab', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hslab', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('library', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('auditorium', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('counroom', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('parlor', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('proom', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sick_room', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('canteen', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('secroom', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('oroom', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('stoilet', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('std_toilet', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('spcl_stud', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('wall', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('if_wall', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cctv', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ds', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('no_camera', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('guard', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('no_guard', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('fguard', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('no_fguard', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('water', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('drainage', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('mmeals', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('no_buses', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gps', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nola', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('first_aid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('no_water', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('no_sbus', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('free_tran', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cam_area', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pas', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('prin_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('prin_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('prin_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('prin_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vp_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vp_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vp_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vp_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pg_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pg_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pg_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pg_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tg_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tg_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tg_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tg_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('prt_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('prt_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('prt_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('prt_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nt_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nt_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nt_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nt_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lib_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lib_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lib_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lib_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('art_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('art_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('art_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('art_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('coun_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('coun_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('coun_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('coun_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comlit_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comlit_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comlit_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comlit_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('faithmin_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('faithmin_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('faithmin_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('faithmin_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nurse_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nurse_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nurse_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nurse_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pt_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pt_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pt_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pt_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('om_per', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('om_tem', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('om_part', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('oa_per', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('oa_tem', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('oa_part', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('clerk_per', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('clerk_tem', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('clerk_part', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lab_per', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lab_tem', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lab_part', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('acc_per', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('acc_tem', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('acc_part', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('peon_per', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('peon_tem', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('peon_part', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('other_per', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('other_tem', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('other_part', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ut_permale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ut_perfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ut_temmale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ut_temfemale', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('no_curricular_carried', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('no_groups', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('no_community', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_school', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_zonal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_district', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_state', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_national', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_international', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('com_school', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('com_zonal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('com_district', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('com_state', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('com_national', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('com_international', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sclpro_school', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sclpro_zonal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sclpro_district', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sclpro_state', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sclpro_national', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sclpro_international', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('year_begin', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('year_end', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('workday_21_22', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('workday_20_21', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('workday_19_20', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hours_21_22', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hours_20_21', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hours_19_20', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('instructional_hours_21_22', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('instructional_hours_20_21', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('instructional_hours_19_20', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('non_instructional_hours_21_22', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('non_instructional_hours_20_21', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('non_instructional_hours_19_20', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('holidays_21_22', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('holidays_20_21', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('holidays_19_20', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sub_week', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('moral_week', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('duration_teaching', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('no_clubs', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('summer_from', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('summer_to', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('winter_from', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('winter_to', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('shifts', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_name'], ['register.user_name'], name='general_info_user_name_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='general_info_pkey')
    )
    op.drop_table('schoolprofile')
    # ### end Alembic commands ###
