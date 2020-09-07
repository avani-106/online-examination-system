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
	
class Exam(models.Model):
	e_id=models.IntegerField()
	exam_name=models.CharField(max_length=255)
	exam_status=models.IntegerField()
	exam_date=models.DateField()
	exam_time=models.TimeField()
	exam_duration=models.CharField(max_length=255)
	neg_marks_status=models.IntegerField()
	negative_marks=models.IntegerField()
	time_reduction=models.IntegerField()
	passing_percentage=models.IntegerField()
	re_exam_day=models.IntegerField()
	terms_condition=models.TextField()
	result_show_on_mail=models.IntegerField()
	show_question=models.CharField(max_length=255)
	sort_order=models.CharField(max_length=255)
	categoryid=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="exam1")
	subcategoryid=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="exam2")
	subjectid=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="exam3")
	centerid=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="exam4")
	
class Practice_exam(models.Model):
	p_e_id=models.IntegerField()
	passing_percentage=models.IntegerField()
	re_exam_day=models.IntegerField()
	exam_name=models.CharField(max_length=255)
	exam_status=models.IntegerField()
	exam_duration=models.CharField(max_length=255)
	neg_mark_status=models.IntegerField()
	negative_marks=models.IntegerField()
	terms_condition=models.TextField()
	category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="pexam1")
	subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="pexam2")
	center=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="pexam3")
	subjects=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="pexam4")
	
	
class Student(models.Model):
	student_id=models.IntegerField()
	student_name=models.CharField(max_length=250)
	student_father=models.CharField(max_length=255)
	student_mother=models.CharField(max_length=255)
	student_dob=models.CharField(max_length=255)
	student_address=models.TextField()
	student_phone=models.CharField(max_length=255)
	student_email=models.CharField(max_length=255)
	user_name=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	student_status=models.IntegerField()
	categorys=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="student1")
	subcategorys=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="student2")
	centers=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="student3")
	batch=models.ForeignKey(Batch,on_delete=models.CASCADE,related_name="student4")
	
class Practice_exam_status(models.Model):
	pid=models.IntegerField()
	exam_date=models.DateField()
	status=models.IntegerField()
	starttime=models.CharField(max_length=255)
	endtime=models.CharField(max_length=255)
	noofattempts=models.IntegerField(max_length=255)
	pass_or_fail=models.CharField(max_length=255)
	students=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="practice")
	exams=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name="practice2")
	
	

				     





