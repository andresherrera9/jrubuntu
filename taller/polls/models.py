from django.db import models

class Quizros(models.Model):
    nombre = models.CharField(max_length=120)
    num_preguntas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"




class Cuest(models.Model):
    
    UNA = 'UNA'
    MULTIPLE = 'MULTIPLE'
    ABIERTA = 'ABIERTA'
    tiposPregunta = [
        (UNA,'UNA'),
        (MULTIPLE,'MULTIPLE'),
        (ABIERTA,'ABIERTA'),
    ]

    question = models.CharField(max_length=250, unique=True)
    quizros = models.ForeignKey(Quizros, on_delete=models.CASCADE)
    tipoPregunta = models.CharField(max_length=20,choices=tiposPregunta,default=UNA)
    correcta_n = models.IntegerField(default=1)
    #option = models.CharField(max_length=100)
    #correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question}-{self.quizros}"

    #def get_question(self):
    #    return self.question()

    class Meta:
        unique_together = [
            ("question","quizros")
        ]
    

class answ(models.Model):

    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question= models.ForeignKey(Cuest, on_delete=models.CASCADE)
    quizros = models.ForeignKey(Quizros, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        unique_together = [
            ("question","text")
        ]


