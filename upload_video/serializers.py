from rest_framework import serializers
from django.urls import reverse
from .models import (top_video, maincontent,
            video_table, Footer, 
            search_bar, ads, 
            craetor, news, post)


class main_content(serializers.ModelSerializer):
    class Meta:
        model = maincontent
        fields = '__all__'



class top_video_serializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = main_video
        fields = '__all__'
    def get_slug(self, obj):
        request = self.context.get('request')
        if request:
            return request.scheme + '://' + 'address.com' + ('/' if not obj.slug.startswith('/') else '')  + obj.slug
        return None
    
    def get_video_file(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.video_file.url)
        return obj.video_file.url
        
        
class video_table_serializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    video_file = serializers.SerializerMethodField()
    
    class Meta:
        model = video_table
        fields = ['video_file', 'title', 'description', 'category', 'views', 'likes', 'creator', 'slug']
    def get_slug(self, obj):
        request = self.context.get('request')
        if requestt
           return f"{request.scheme}://address.com{Path('/', obj.slug)}"
        return None

    def get_video_file(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.video_file.url) if request else obj.video_file.url
        
class Footer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['poster', 'social_media_links']
        
class search_bar_serializer(serializers.ModelSerializer):
    class Meta:
        model = search_bar
        fields = ['title']
        
        
class ads_serializer(serializers.ModelSerializer):
    class Meta:
        model = ads
        fields = '__all__'
        
        
class creator_serializer(serializers.ModelSerializer):
    class Meta:
        model = spokesman
        fields = ['name', 'image', 'description', 'contact']


class news_serializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = ['id', 'title', 'poster', 'news_text', 'source']


class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = ['id', 'title', 'poster', 'post_text']
