from django.db import models


# =====================================================
# USERS TABLE
# =====================================================

class User(models.Model):

    user_id = models.AutoField(primary_key=True)

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    password_hash = models.CharField(max_length=255)

    role = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField()

    class Meta:

        db_table = 'users'

        managed = False

    def __str__(self):

        return self.full_name



# =====================================================
# DOCTORS TABLE
# =====================================================

class Doctor(models.Model):

    doctor_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        db_column='user_id'
    )

    specialization = models.CharField(max_length=100)

    qualification = models.CharField(max_length=200)

    experience_years = models.IntegerField()

    registration_number = models.CharField(max_length=50)

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    avg_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2
    )

    is_approved = models.BooleanField()

    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:

        db_table = 'doctors'

        managed = False

    def __str__(self):

        return self.specialization



# =====================================================
# PATIENTS TABLE
# =====================================================

class Patient(models.Model):

    patient_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        db_column='user_id'
    )

    date_of_birth = models.DateField()

    gender = models.CharField(max_length=20)

    blood_group = models.CharField(max_length=5)

    address = models.TextField()

    class Meta:

        db_table = 'patients'

        managed = False

    def __str__(self):

        return str(self.patient_id)



# =====================================================
# SCHEDULES TABLE
# =====================================================

class Schedule(models.Model):

    schedule_id = models.AutoField(primary_key=True)

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.DO_NOTHING,
        db_column='doctor_id'
    )

    available_day = models.CharField(max_length=20)

    start_time = models.TimeField()

    end_time = models.TimeField()

    slot_duration_min = models.IntegerField()

    is_active = models.BooleanField(default=True)

    class Meta:

        db_table = 'schedules'

        managed = False

    def __str__(self):

        return self.available_day



# =====================================================
# SLOTS TABLE
# =====================================================

class Slot(models.Model):

    slot_id = models.AutoField(primary_key=True)

    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.DO_NOTHING,
        db_column='schedule_id'
    )

    slot_start_time = models.TimeField()

    slot_end_time = models.TimeField()

    is_available = models.BooleanField(default=True)

    class Meta:

        db_table = 'slots'

        managed = False

    def __str__(self):

        return str(self.slot_id)



# =====================================================
# APPOINTMENTS TABLE
# =====================================================

class Appointment(models.Model):

    appointment_id = models.AutoField(primary_key=True)

    patient = models.ForeignKey(
        Patient,
        on_delete=models.DO_NOTHING,
        db_column='patient_id'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.DO_NOTHING,
        db_column='doctor_id'
    )

    slot = models.ForeignKey(
        Slot,
        on_delete=models.DO_NOTHING,
        db_column='slot_id'
    )

    appointment_date = models.DateField()

    status = models.CharField(max_length=20)

    reason_for_visit = models.CharField(max_length=300)

    notes = models.TextField()

    created_at = models.DateTimeField()

    class Meta:

        db_table = 'appointments'

        managed = False

    def __str__(self):

        return str(self.appointment_id)



# =====================================================
# REVIEWS TABLE
# =====================================================

class Review(models.Model):

    review_id = models.AutoField(primary_key=True)

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.DO_NOTHING,
        db_column='appointment_id'
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.DO_NOTHING,
        db_column='patient_id'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.DO_NOTHING,
        db_column='doctor_id'
    )

    rating = models.IntegerField()

    review_text = models.TextField()

    created_at = models.DateTimeField()

    class Meta:

        db_table = 'reviews'

        managed = False

    def __str__(self):

        return str(self.rating)



# =====================================================
# NOTIFICATIONS TABLE
# =====================================================

class Notification(models.Model):

    notification_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        db_column='user_id'
    )

    title = models.CharField(max_length=150)

    message = models.TextField()

    notification_type = models.CharField(max_length=50)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField()

    class Meta:

        db_table = 'notifications'

        managed = False

    def __str__(self):

        return self.title