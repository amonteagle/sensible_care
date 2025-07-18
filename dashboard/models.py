from django.db import models

class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    
    client_name = models.TextField()
    gender = models.TextField()
    marital_status = models.TextField()
    age_band = models.TextField()
    case_managers = models.TextField()
    
    client_group = models.TextField()
    client_subgroup = models.TextField()
    hcp_level_name = models.TextField()
    active_flag = models.TextField()

    state_code = models.TextField()
    area = models.TextField()

    class Meta:
        managed = False  # Don't let Django try to create or modify this
        db_table = 'clients'