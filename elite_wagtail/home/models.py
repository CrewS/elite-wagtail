from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class CourseBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock()
    description = blocks.CharBlock()
    link = blocks.URLBlock()

    class Meta:
        template = 'home/blocks/course.html'
        icon = 'user'


class CategoriesListBlock(blocks.StructBlock):
    categorieslist = blocks.ListBlock(blocks.StructBlock([
        ('categories_name', blocks.CharBlock(required=True, label=_('分类名称'))),
        ('categories_link', blocks.URLBlock(required=True, label=_('分类链接'))),
    ]), label=_('课程分类'))

    class Meta:
        template = 'home/blocks/categorieslist.html'
        label = "课程分类"
        icon = 'grip'


class StoryBlock(blocks.StructBlock):
    title = blocks.CharBlock(label=_('模块标题'))
    propaganda_image = ImageChooserBlock(label=_('宣传图片'))

    story = blocks.ListBlock(blocks.StructBlock([
        ('story_photo', blocks.ListBlock(ImageChooserBlock(required=False), label=_('故事图片'))),
        ('story_title', blocks.CharBlock(required=False, label=_('故事标题'))),
        ('story_content', blocks.CharBlock(required=False, label=_('故事内容'))),
        ('photo_location', blocks.ChoiceBlock(choices=[
            ('left', 'left'),
            ('center', 'center'),
        ], icon='cup', label=_('图片位置'))),
        ('story_link', blocks.URLBlock(label=_('故事链接'))),
    ]), label=_('用户故事'))

    propaganda_link = blocks.URLBlock(label=_('宣传链接'))

    class Meta:
        label = "故事模块"
        icon = 'user'
        template = 'home/blocks/story.html'


class ProfessorBlock(blocks.StructBlock):
    title = blocks.CharBlock(label=_('模块标题'))
    professor_image = ImageChooserBlock(label=_('宣传图片'))

    professor = blocks.ListBlock(blocks.StructBlock([
        ('name', blocks.CharBlock(required=False, label=_('教授名称'))),
        ('professor_pic', ImageChooserBlock(required=False, label=_('教授头像'))),
        ('professor_link', blocks.URLBlock(required=False, label=_('链接'))),
        ('professor_degree', blocks.ListBlock(blocks.TextBlock(required=False), label=_('教授学历'))),
        ('content', blocks.CharBlock(required=False, label=_('内容'))),
    ]), label=_('教授'))

    professor_link = blocks.URLBlock(label=_('宣传链接'))

    class Meta:
        label = "教授模块"
        icon = 'user'
        template = 'home/blocks/professor.html'


class VipBlock(blocks.StructBlock):
    background_image = ImageChooserBlock(label=_('背景图片'))
    background_cotent = blocks.CharBlock(required=False, label=_('背景内容'))
    title = blocks.CharBlock(label=_('标题'))
    background_link = blocks.URLBlock(label=_('链接'))

    class Meta:
        label = "加入会员"
        icon = 'user'
        template = 'home/blocks/vip.html'


class SeriesProcessBlock(blocks.StructBlock):
    title = blocks.CharBlock(label=_('模块标题'))
    has_update_or_nor = blocks.BooleanBlock(label=_('是否有敬请期待'),required=False)
    series = blocks.ListBlock(blocks.StructBlock([
        ('course_photo', ImageChooserBlock(required=True, label=_('课程图片'))),
        ('title', blocks.CharBlock(required=True, label=_('课程标题'))),
        ('description', blocks.CharBlock(required=True, label=_('课程描述'))),
        ('link', blocks.URLBlock(required=True, label=_('课程链接'))),
    ]), label=_('课程路径'))

    class Meta:
        icon = 'user'
        label = "系列课程流程列表"
        template = 'home/blocks/series_process_list.html'


class SeriesBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock()
    description = blocks.CharBlock()
    link = blocks.URLBlock()

    class Meta:
        icon = 'user'


class HomePage(Page):
    body = StreamField([
        ('Paragraph', blocks.RichTextBlock()),
        ('Image', ImageChooserBlock()),
        ('Text', blocks.TextBlock()),
        ('Heading', blocks.CharBlock()),
        ('BlockQuote', blocks.BlockQuoteBlock()),
        ('Email', blocks.EmailBlock()),
        ('URL', blocks.URLBlock()),
        ('Boolean', blocks.BooleanBlock()),
        ('Integer', blocks.IntegerBlock()),
        ('Float', blocks.FloatBlock()),
        ('Decimal', blocks.DecimalBlock()),
        ('Date', blocks.DateBlock()),
        ('Time', blocks.TimeBlock()),
        ('DateTime', blocks.DateTimeBlock()),
        ('RawHTML', blocks.RawHTMLBlock()),

        ('Choice', blocks.ChoiceBlock()),
        ('PageChooser', blocks.PageChooserBlock()),
        ('DocumentChooser', DocumentChooserBlock()),

        ('Embed', EmbedBlock()),
        ('RecommendCourse', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('courses', blocks.ListBlock(CourseBlock()))
        ], template='home/blocks/recommend_courses.html')),
        ('SeriesCourse', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('series', blocks.ListBlock(SeriesBlock()))
        ], template='home/blocks/series_list.html')),
        ('StoryBlock', StoryBlock()),
        ('ProfessorBlock', ProfessorBlock()),
        ('CategoriesListBlock', CategoriesListBlock()),
        ('VipBlock', VipBlock()),
        ('SeriesProcessBlock', SeriesProcessBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
