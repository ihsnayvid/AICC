from django.contrib import admin
from .models import Profile,ProfileSummary
from django.db.models.functions import Trunc
from django.db.models import DateTimeField
# Register your models here.
admin.site.register(Profile)


@admin.register(ProfileSummary)

class ProfileSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/profile_summary_change_list.html'
    #date_hierarchy = 'created'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        metrics = {
           # 'total': Count('id'),
           # ‘total_sales’: Sum(‘price’),
        }
        response.context_data['summary'] = list(
            qs
            #.values('profile__category__name')
            .annotate(**metrics)
            #.order_by('-total_profile')
        )
        list_filter = (
        'user',
    )

        '''summary_over_time = qs.annotate(
            period=Trunc(
                'created',
                'day',
                output_field=DateTimeField(),
            ),
        ).values('period')
        .annotate(total=Sum('price'))
        .order_by('period')
        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)
        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': \
               ((x['total'] or 0) - low) / (high - low) * 100 
               if high > low else 0,
        } for x in summary_over_time]'''
        return response
