from django.db import models


class BlogTags(models.TextChoices):
    TECH = 'tech', 'Tech'
    HEALTH = 'health', 'Health'
    SPORTS = 'sports', 'Sports'
    FOOD = 'food', 'Food'
    TRAVEL = 'travel', 'Travel'
    LIFESTYLE = 'lifestyle', 'Lifestyle'
    FASHION = 'fashion', 'Fashion'
    ENTERTAINMENT = 'entertainment', 'Entertainment'
    POLITICS = 'politics', 'Politics'
    BUSINESS = 'business', 'Business'
    EDUCATION = 'education', 'Education'
    OTHERS = 'others', 'Others'
