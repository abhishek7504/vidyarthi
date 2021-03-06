from django.db import models
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager
from django.core.validators import RegexValidator
from django.urls import reverse
from django.template.defaultfilters import slugify
'''PROFILE'''
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
class Profile(models.Model):

    STATUS_CHOICES = (('student','STUDENT'),('employer','EMPLOYER'),('freelancer','FREELANCER'))
    COUNTRY_CHOICES = (('australia','AUSTRALIA'),('india','INDIA'),('united states of america','UNITED STATES OF AMERICA'),('united kingdoms','UNITED KINGDOMS'))
    
    
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    
    mother_name = models.CharField(max_length = 60, null = True , blank = True)
    fathers_name = models.CharField(max_length = 60 , null= True , blank = True)
    date_of_birth =  models.DateField(null= True ,blank = True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
     message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    state = models.CharField(max_length = 50,default='any')
    city = models.CharField(max_length = 50,default='any')
    area = models.CharField(max_length = 50,default='any')
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES ,default ='india')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='student')
    slug = models.SlugField(max_length=50, null=True, blank=True)
    

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     reverse('work:view_profile', args=[self.slug])    

class ProfileQRCode(models.Model):
    profile = models.OneToOneField(Profile, related_name='qr_code', on_delete=models.CASCADE, max_length=100,
                                         null=True, blank=True, unique=True)
    qr_code = models.ImageField(upload_to="QR_codes/", null=True, blank=True)
    
    def save(self, *args, **kwargs):
        url = "http://127.0.0.1:8000"
        # store_id = "rqojqQuzumU::" + str(self.store.pk)
        # store_id = base64.urlsafe_b64encode(store_id)
        # print(store_id)
        # self.slug = slugify(str(self.feedback_form))
        sub_url = url + reverse('work:view_profile', args=[self.profile])
        print(sub_url)
        # short_qr_code = self.short_code  = GenerateUrl().qr_shortner(sub_url)
        # print(short_qr_code)
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            box_size=20,
            border=0
        )
        qr.add_data(sub_url)
        qr.make(fit=True)
        img = qr.make_image()
        stream = BytesIO()
        img.save(stream, kind='PNG')
        self.qr_code = SimpleUploadedFile("qr_code.png", stream.getvalue())
        super(ProfileQRCode, self).save(*args, **kwargs)

        def __str__(self):
            return self.profile


'''EDUCATION'''

class Education(models.Model):

    DEGREE_CHOICES = (('10','10'),('12','12'),('diploma','DIPLOMA'),('under graduation','UNDER GRADUATION'),('post graduation','POST GRADUATION'))

    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='education')
    degree = models.CharField(max_length = 20 ,choices = DEGREE_CHOICES,default = '10', null= True , blank = True)
    branch = models.CharField(max_length = 10 ,null=True,blank = True,default = 'in any')
    roll_number = models.CharField(max_length = 15, null= True , blank = True)
    university = models.CharField(max_length = 50, null= True , blank = True)
    duration = models.CharField(max_length = 4 ,default='in years', null= True , blank = True)
    year_of_passing = models.CharField(max_length=4, null= True , blank = True)
    pencentile = models.CharField(max_length = 4 ,default='in numbers', null= True , blank = True)
    upload_marksheet = models.ImageField(upload_to='users/%y/%m/%d', null= True , blank = True)


''' ADDITIONAL COURSES AND CERTIFICATIONS'''

class Courses(models.Model):

    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='Courses')
    course_name = models.CharField(max_length = 50, null= True , blank = True)
    institute_name = models.CharField(max_length = 50, null= True , blank = True)
    duration = models.CharField(max_length = 2 ,default='in months', null= True , blank = True)
    validity_of_certification = models.CharField(max_length = 2,default='in years', null= True , blank = True)
    upload_certificate = models.ImageField(upload_to='users/%y/%m/%d', null= True , blank = True)


'''SAMPLE SIGNATURE,THUMB IMPRESSIONS,AND DOCUMENTS'''

class Other_doc(models.Model):

    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='impressions')
    document_1= models.FileField(upload_to = 'media/',null = True,verbose_name='Document 1',  blank = True)
    document_2= models.FileField(upload_to = 'media/',null = True,verbose_name='Document 2',blank = True)
    document_3= models.FileField(upload_to = 'media/',null = True,verbose_name='Document 3', blank = True)
    document_4= models.FileField(upload_to = 'media/',null = True,verbose_name='Document 4', blank = True)
    document_5= models.FileField(upload_to = 'media/',null = True,verbose_name='Document 5',  blank = True)
    signature = models.ImageField(upload_to = 'media/',null = True,verbose_name='Signature Photo',  blank = True)
    signed_photo = models.ImageField(upload_to = 'media/',null = True,verbose_name='Singed Photo',  blank = True)
    thumb_impression_photo = models.ImageField(upload_to = 'media/',null = True,verbose_name='Thumb Impression Photo',  blank = True)                          