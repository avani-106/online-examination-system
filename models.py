class Batch(models.Model):
	b_id=models.IntegerField()
	batch_name=models.CharField(max_length=255)
	batch_time=models.Timefield()
	batch_status=models.IntegerField()

class Center(models.Model):
	center_id=models.IntegerField()
	center_name=models.CharField(max_length=255)
	center_address=models.CharField(max_length=300)
	center_code=models.CharField(max_length=255)
	center_logo=models.CharField(max_length=255)
	location=models.CharField(max_length=255)
	phoneno=models.CharField(max_length=10)
	email=models.CharField(max_length=255)
	username=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	password_md5=models.CharField(max_length=255)
	theme_id=models.CharField(max_length=255)
	center_status=models.IntegerField()
	about_center=models.CharField(max_length=255)

class Category(models.Model):
	category_id=models.IntegerField()
	category_name=models.CharField(max_length=225)
	category_status=models.IntegerField()

class Subcategory(models.Model):
	subcategory_id=models.IntegerField()
	subcategory_name=models.CharField(max_length=255)
	subcategory_status=models.IntegerField()
	category1=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategory")

class Subject(models.Model):
	subject_id=models.IntegerField()
	subject_name=models.CharField(max_length=255)
	subject_status=models.IntegerField()
	category2=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subject1")
	subcategory1=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="subject2")





