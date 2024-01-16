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
    test_id = models.IntegerField(primary_key=True)  # The composite primary key (test_id, user_id) found, that is not supported. The first column is selected.
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
    user_id = models.CharField(primary_key=True, max_length=8, db_collation='Korean_Wansung_CI_AS')  # The composite primary key (user_id, test_id, question_id, choice_id) found, that is not supported. The first column is selected.
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
    test_id = models.IntegerField(primary_key=True)  # The composite primary key (test_id, user_id, question_id) found, that is not supported. The first column is selected.
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
    user_id = models.CharField(primary_key=True, max_length=10, db_collation='Korean_Wansung_CI_AS')  # The composite primary key (user_id, test_id, subject_id) found, that is not supported. The first column is selected.
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


class VBaseDept(models.Model):
    dept_cd = models.CharField(db_column='DEPT_CD', max_length=20)  # Field name made lowercase.
    dept_nm = models.CharField(db_column='DEPT_NM', max_length=100)  # Field name made lowercase.
    dept_sort = models.CharField(db_column='DEPT_SORT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parent_cd = models.CharField(db_column='PARENT_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    parent_nm = models.CharField(db_column='PARENT_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    com_cd = models.CharField(db_column='COM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'V_BASE_DEPT'


class VBaseUser(models.Model):
    user_id = models.CharField(db_column='USER_ID', max_length=20)  # Field name made lowercase.
    emp_no = models.CharField(db_column='EMP_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_nm = models.CharField(db_column='USER_NM', max_length=50)  # Field name made lowercase.
    user_e_nm = models.CharField(db_column='USER_E_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_c_nm = models.CharField(db_column='USER_C_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_nicknm = models.CharField(db_column='USER_NICKNM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ty_retire = models.CharField(db_column='TY_RETIRE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    user_sex = models.CharField(db_column='USER_SEX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_birthday_fg = models.CharField(db_column='USER_BIRTHDAY_FG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_birthday = models.CharField(db_column='USER_BIRTHDAY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    user_anniversary_fg = models.CharField(db_column='USER_ANNIVERSARY_FG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_anniversary = models.CharField(db_column='USER_ANNIVERSARY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    user_fg = models.CharField(db_column='USER_FG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wf_pwd = models.CharField(db_column='WF_PWD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    res_no = models.CharField(db_column='RES_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ex_mail = models.CharField(db_column='EX_MAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dept_cd = models.CharField(db_column='DEPT_CD', max_length=20)  # Field name made lowercase.
    dept_nm = models.CharField(db_column='DEPT_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dept_e_nm = models.CharField(db_column='DEPT_E_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dept_c_nm = models.CharField(db_column='DEPT_C_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title_cd = models.CharField(db_column='TITLE_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    title_nm = models.CharField(db_column='TITLE_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title_e_nm = models.CharField(db_column='TITLE_E_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title_c_nm = models.CharField(db_column='TITLE_C_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    degree_cd = models.CharField(db_column='DEGREE_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    degree_nm = models.CharField(db_column='DEGREE_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    degree_e_nm = models.CharField(db_column='DEGREE_E_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    degree_c_nm = models.CharField(db_column='DEGREE_C_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    job_cd = models.CharField(db_column='JOB_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    job_nm = models.CharField(db_column='JOB_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    job_e_nm = models.CharField(db_column='JOB_E_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    job_c_nm = models.CharField(db_column='JOB_C_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    duty_cd = models.CharField(db_column='DUTY_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    duty_nm = models.CharField(db_column='DUTY_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    duty_e_nm = models.CharField(db_column='DUTY_E_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    duty_c_nm = models.CharField(db_column='DUTY_C_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hobong_cd = models.CharField(db_column='HOBONG_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hobong_nm = models.CharField(db_column='HOBONG_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title_sort = models.IntegerField(db_column='TITLE_SORT', blank=True, null=True)  # Field name made lowercase.
    degree_sort = models.IntegerField(db_column='DEGREE_SORT', blank=True, null=True)  # Field name made lowercase.
    job_sort = models.IntegerField(db_column='JOB_SORT', blank=True, null=True)  # Field name made lowercase.
    duty_sort = models.IntegerField(db_column='DUTY_SORT', blank=True, null=True)  # Field name made lowercase.
    hobong_sort = models.IntegerField(db_column='HOBONG_SORT', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='SORT', blank=True, null=True)  # Field name made lowercase.
    photo_url = models.CharField(db_column='PHOTO_URL', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sign_url = models.CharField(db_column='SIGN_URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    com_cd = models.CharField(db_column='COM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    com_nm = models.CharField(db_column='COM_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    com_e_nm = models.CharField(db_column='COM_E_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comp_tel = models.CharField(db_column='COMP_TEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comp_fax = models.CharField(db_column='COMP_FAX', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comp_post = models.CharField(db_column='COMP_POST', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comp_address = models.CharField(db_column='COMP_ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comp_e_address = models.CharField(db_column='COMP_E_ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ent_date = models.DateTimeField(db_column='ENT_DATE', blank=True, null=True)  # Field name made lowercase.
    prm_date = models.DateTimeField(db_column='PRM_DATE', blank=True, null=True)  # Field name made lowercase.
    ret_date = models.DateTimeField(db_column='RET_DATE', blank=True, null=True)  # Field name made lowercase.
    yr_continue = models.CharField(db_column='YR_CONTINUE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile_addition = models.CharField(db_column='MOBILE_ADDITION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_mask = models.CharField(db_column='USER_MASK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_fg = models.CharField(db_column='AD_FG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    use_fg = models.CharField(db_column='USE_FG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hr_fg = models.CharField(db_column='HR_FG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    it_fg = models.CharField(db_column='IT_FG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ins_date = models.DateTimeField(db_column='INS_DATE', blank=True, null=True)  # Field name made lowercase.
    upd_date = models.DateTimeField(db_column='UPD_DATE', blank=True, null=True)  # Field name made lowercase.
    pass_upd_date = models.DateTimeField(db_column='PASS_UPD_DATE', blank=True, null=True)  # Field name made lowercase.
    ad_upd_date = models.DateTimeField(db_column='AD_UPD_DATE', blank=True, null=True)  # Field name made lowercase.
    contents_fg = models.CharField(db_column='CONTENTS_FG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    job_content = models.CharField(db_column='JOB_CONTENT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    skill_content = models.CharField(db_column='SKILL_CONTENT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='INTRODUCTION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    weather_region_cd = models.CharField(db_column='WEATHER_REGION_CD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    site_cd = models.CharField(db_column='SITE_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    manager_id = models.CharField(db_column='MANAGER_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    display_yn = models.CharField(db_column='DISPLAY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    msg_yn = models.CharField(db_column='MSG_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='POST', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address_addition = models.CharField(db_column='ADDRESS_ADDITION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    blog_address = models.CharField(db_column='BLOG_ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    atd_target_yn = models.CharField(db_column='ATD_TARGET_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lync_sip = models.CharField(db_column='LYNC_SIP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cd_b_level = models.CharField(db_column='CD_B_LEVEL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ds_b_level = models.CharField(db_column='DS_B_LEVEL', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cd_m_level = models.CharField(db_column='CD_M_LEVEL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ds_m_level = models.CharField(db_column='DS_M_LEVEL', max_length=60, blank=True, null=True)  # Field name made lowercase.
    level_detail = models.CharField(db_column='LEVEL_DETAIL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    o365_yn = models.CharField(db_column='O365_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prohibit_quota = models.IntegerField(db_column='PROHIBIT_QUOTA', blank=True, null=True)  # Field name made lowercase.
    autodesk_id = models.CharField(db_column='AUTODESK_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    wfh_yn = models.CharField(db_column='WFH_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    seat_txt = models.CharField(db_column='SEAT_TXT', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'V_BASE_USER'


class VFilteredUserCertification(models.Model):
    user_id = models.CharField(db_column='USER_ID', max_length=20)  # Field name made lowercase.
    emp_no = models.CharField(db_column='EMP_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_nm = models.CharField(db_column='USER_NM', max_length=50)  # Field name made lowercase.
    user_e_nm = models.CharField(db_column='USER_E_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dept_cd = models.CharField(db_column='DEPT_CD', max_length=20)  # Field name made lowercase.
    dept_nm = models.CharField(db_column='DEPT_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title_cd = models.CharField(db_column='TITLE_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    title_nm = models.CharField(db_column='TITLE_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    degree_cd = models.CharField(db_column='DEGREE_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    com_cd = models.CharField(db_column='COM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    com_nm = models.CharField(db_column='COM_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comp_tel = models.CharField(db_column='COMP_TEL', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'V_FILTERED_USER_CERTIFICATION'


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

class UploadFileModel(models.Model):
    # description = models.CharField(max_length=255)
    files = models.FileField(upload_to="", null=True)
    # upload_at = models.DateTimeField(auto_now_add=True)
    