from rest_framework import serializers

from quote.models import Quote, Category



class QuoteSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name')
    category_list = serializers.CharField(source='category.name')
    
    class Meta:
        model = Quote
        # ('__all__')     for all fields
        fields = ['id', 'quote', 'author_name', 'category', 'category_list', 'publish_date']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
