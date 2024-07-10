class MngDBRouter:
    # DB read
    def db_for_read(self, model, **hints) :
        if model._meta.app_label == 'bim_mng': # app명
            return 'mng_dev' # settings.py에서 설정한, 위 app에서 사용할 db명
        return 'default' # bim_mng 앱이 아닌 다른 앱은 default 사용
    
    # DB write
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'bim_mng':
            return 'mng_dev'
        return 'default'
    
    # DB model 간 relation 허용 여부 결정
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db in ('default', 'mng_dev') and obj2._state.db in ('default', 'mng_dev'):
            return True
        return None
    
    # DB migration 허용 여부 결정
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'bim_mng': # bim_mng 앱이면
            return db == 'mng_dev' # mng_dev db를 migration
        return db == 'default'     # 이외 다른 앱은 default db migration
    
    