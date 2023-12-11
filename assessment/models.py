# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbBimCertificationComm(models.Model):
    code = models.CharField(primary_key=True, max_length=10, db_collation='Korean_Wansung_CI_AS')
    name = models.CharField(max_length=50, db_collation='Korean_Wansung_CI_AS')
    value = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS')
    p_code = models.CharField(max_length=10, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    sort_no = models.IntegerField()
    note = models.CharField(max_length=500, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_COMM'


class TbBimCertificationLearnMedia(models.Model):
    seq = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    group_name = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    item_name = models.CharField(max_length=200, db_collation='Korean_Wansung_CI_AS')
    ref_files = models.CharField(max_length=2000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    media_name = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS')
    order_by = models.IntegerField()
    descriptions = models.CharField(max_length=2000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    category_icon_src = models.CharField(max_length=200, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_LEARN_MEDIA'


class TbBimCertificationManager(models.Model):
    user_id = models.CharField(primary_key=True, max_length=8, db_collation='Korean_Wansung_CI_AS')
    user_name = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    dept_cd = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    dept_name = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    is_executive = models.BooleanField()
    is_used = models.BooleanField()
    description = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    is_bim_team = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_MANAGER'


class TbBimCertificationQuestion(models.Model):
    seq = models.AutoField(primary_key=True)
    subject_id = models.IntegerField()
    test_group = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    category = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    subcategory = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    content = models.CharField(max_length=2000, db_collation='Korean_Wansung_CI_AS')
    related_function = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    document_link = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    video_link = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    created_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS')
    remark = models.CharField(max_length=2000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    issue_on = models.DateTimeField()
    modified_on = models.DateTimeField(blank=True, null=True)
    is_used = models.BooleanField()
    modified_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    question_group = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    current_choice_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_QUESTION'


class TbBimCertificationQuestionChoiceItem(models.Model):
    seq = models.AutoField(primary_key=True)
    question_id = models.IntegerField()
    content = models.CharField(max_length=2000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    is_correct = models.BooleanField()
    created_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS')
    created_on = models.DateTimeField(blank=True, null=True)
    is_used = models.BooleanField()
    order_by = models.IntegerField(blank=True, null=True)
    choice_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_QUESTION_CHOICE_ITEM'


class TbBimCertificationQuestionMedia(models.Model):
    seq = models.AutoField(primary_key=True)
    question_id = models.IntegerField()
    name = models.CharField(max_length=200, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    media_type = models.CharField(max_length=10, db_collation='Korean_Wansung_CI_AS')
    file_id = models.IntegerField()
    created_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    order_by = models.IntegerField()
    is_used = models.BooleanField()
    created_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_QUESTION_MEDIA'


class TbBimCertificationQuestionWeight(models.Model):
    question_id = models.IntegerField(primary_key=True)
    correct_answer_rate = models.FloatField(blank=True, null=True)
    incorrect_answer_rate = models.FloatField(blank=True, null=True)
    average_solution_time = models.FloatField(blank=True, null=True)
    weighted_coefficient = models.FloatField(blank=True, null=True)
    adjusted_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_QUESTION_WEIGHT'


class TbBimCertificationResultVerification(models.Model):
    seq = models.AutoField(primary_key=True)
    subject_id = models.IntegerField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS')
    result_type = models.CharField(max_length=4, db_collation='Korean_Wansung_CI_AS')
    verification_key = models.CharField(max_length=128, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    created_on = models.DateTimeField()
    verification_expires_on = models.DateTimeField()
    is_canceled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_RESULT_VERIFICATION'


class TbBimCertificationSubject(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    test_minutes = models.IntegerField()
    question_count = models.IntegerField()
    reference_file = models.IntegerField(blank=True, null=True)
    is_used = models.BooleanField()
    created_on = models.DateTimeField()
    created_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS')
    modified_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_SUBJECT'


class TbBimCertificationSubjectNote(models.Model):
    seq = models.AutoField(primary_key=True)
    subject_id = models.IntegerField()
    note = models.CharField(max_length=2000, db_collation='Korean_Wansung_CI_AS')
    order_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_SUBJECT_NOTE'


class TbBimCertificationSubjectQuestionCount(models.Model):
    seq = models.AutoField(primary_key=True)
    subject_id = models.IntegerField()
    category = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    question_group = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    question_count = models.IntegerField()
    order_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_SUBJECT_QUESTION_COUNT'


class TbBimCertificationTest(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    test_type = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    subject_id = models.IntegerField()
    test_datetime = models.DateTimeField()
    max_participants = models.IntegerField()
    registration_start_date = models.DateField()
    registration_end_date = models.DateField()
    is_opened = models.BooleanField()
    is_generated_question = models.BooleanField()
    result_open_on = models.DateTimeField()
    created_on = models.DateTimeField()
    created_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS')
    is_used = models.BooleanField()
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    is_result_open = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_TEST'


class TbBimCertificationTestUser(models.Model):
    test_id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS')
    registration_datetime = models.DateTimeField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    period_second = models.IntegerField()
    is_submitted = models.BooleanField()
    submitted_on = models.DateTimeField(blank=True, null=True)
    registration_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    verification_key = models.CharField(max_length=128, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    start_count = models.IntegerField()
    submit_count = models.IntegerField()
    is_observer = models.BooleanField()
    is_canceled = models.BooleanField(blank=True, null=True)
    is_exception = models.BooleanField()
    is_exclude_analysis = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_TEST_USER'
        unique_together = (('test_id', 'user_id'),)


class TbBimCertificationTestUserChoose(models.Model):
    user_id = models.CharField(primary_key=True, max_length=8, db_collation='Korean_Wansung_CI_AS')
    test_id = models.IntegerField()
    question_id = models.IntegerField()
    choice_id = models.IntegerField()
    choose_datetime = models.DateTimeField()
    choose_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_TEST_USER_CHOOSE'
        unique_together = (('user_id', 'test_id', 'question_id', 'choice_id'),)


class TbBimCertificationTestUserQuestion(models.Model):
    test_id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS')
    question_id = models.IntegerField()
    category = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    content = models.CharField(max_length=2000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    question_group = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    order_by = models.IntegerField(blank=True, null=True)
    choice_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_TEST_USER_QUESTION'
        unique_together = (('test_id', 'user_id', 'question_id'),)


class TbBimCertificationTestUserSummary(models.Model):
    user_id = models.CharField(primary_key=True, max_length=10, db_collation='Korean_Wansung_CI_AS')
    test_id = models.IntegerField()
    subject_id = models.IntegerField()
    period_sec = models.IntegerField()
    org_total_score = models.FloatField()
    weighted_total_score = models.FloatField(blank=True, null=True)
    org_grade = models.CharField(max_length=50, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    mod_grade = models.CharField(max_length=50, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    analysis_item = models.TextField(db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    is_used = models.BooleanField(blank=True, null=True)
    is_exclude_counting = models.BooleanField(blank=True, null=True)
    avg_weighted_coefficient = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BIM_CERTIFICATION_TEST_USER_SUMMARY'
        unique_together = (('user_id', 'test_id', 'subject_id'),)


class TbFile(models.Model):
    seq = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=500, db_collation='Korean_Wansung_CI_AS')
    file_guid = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    file_hash = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    file_path = models.CharField(max_length=4000, db_collation='Korean_Wansung_CI_AS')
    file_version = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    file_size = models.FloatField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    file_relative_url = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    is_directory = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_FILE'


class TbFileLog(models.Model):
    seq = models.AutoField(primary_key=True)
    file_id = models.IntegerField()
    user_id = models.CharField(max_length=20, db_collation='Korean_Wansung_CI_AS')
    event_type = models.CharField(max_length=10, db_collation='Korean_Wansung_CI_AS')
    access_on = models.DateTimeField()
    message = models.CharField(max_length=500, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_FILE_LOG'


class TbImageFile(models.Model):
    seq = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=500, db_collation='Korean_Wansung_CI_AS')
    file_guid = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    file_path = models.CharField(max_length=4000, db_collation='Korean_Wansung_CI_AS')
    file_size = models.FloatField(blank=True, null=True)
    image_size = models.CharField(max_length=20, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    image_relative_url = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS')
    image72_relative_url = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    image150_relative_url = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    image500_relative_url = models.CharField(max_length=1000, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    created_on = models.DateTimeField()
    created_by = models.CharField(max_length=8, db_collation='Korean_Wansung_CI_AS')

    class Meta:
        managed = False
        db_table = 'TB_IMAGE_FILE'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Korean_Wansung_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Korean_Wansung_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Korean_Wansung_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Korean_Wansung_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Korean_Wansung_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Korean_Wansung_CI_AS')
    email = models.CharField(max_length=254, db_collation='Korean_Wansung_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Korean_Wansung_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Korean_Wansung_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Korean_Wansung_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    model = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Korean_Wansung_CI_AS')
    name = models.CharField(max_length=255, db_collation='Korean_Wansung_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Korean_Wansung_CI_AS')
    session_data = models.TextField(db_collation='Korean_Wansung_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
