# Django
from django.db import models


class TypeRequest(models.TextChoices):
    share = "share"
    credit = "credit"
    installment_payment = "installment_payment"


class ApprovalStatus(models.TextChoices):
    pending = "pending"
    rejected = "rejected"
    approved = "approved"


class CreditPayType(models.TextChoices):
    advance = "advance"
    installments = "installments"


class CreditUse(models.TextChoices):
    generationIncome = "generationIncome"
    familyStrengthening = "familyStrengthening"
    consumption = "consumption"


class CreditUseDetail(models.TextChoices):
    trade = "trade"
    Smallcompany = "Smallcompany"
    HousingImprovement = "HousingImprovement"
    Education = "Education"
    HouseholdEquipment = "HouseholdEquipment"
    Health = "Health"
    Debtpayment = "Debtpayment"
    ServicesPay = "ServicesPay"
    FoodAndClothing = "FoodAndClothing"
    Transport = "Transport"
    Travels = "Travels"
    Recreation = "Recreation"
