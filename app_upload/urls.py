from django.urls import path, include
from . import views

urlpatterns = [ 
    
    path ('upload_ozon_categories', views.upload_ozon_categories, name='upload_ozon_categories'),
    path ('upload_all', views.upload_all, name='upload_all'),
    path ('upload_brands', views.upload_brands, name='upload_brands'),
    path ('upload_type', views.upload_type, name='upload_type'),
    path ('upload_hard_drive', views.upload_hard_drive, name='upload_hard_drive'),
    path ('upload_country_of_manufacture', views.upload_country_of_manufacture, name='upload_country_of_manufacture'),
    path ('upload_matrix_type', views.upload_matrix_type, name='upload_matrix_type'),
    path ('upload_card_type', views.upload_card_type, name='upload_card_type'),
    path ('upload_bluetooth_type', views.upload_bluetooth_type, name='upload_bluetooth_type'),
    path ('upload_navigation_type', views.upload_navigation_type, name='upload_navigation_type'),
    path ('upload_sensor', views.upload_sensor, name='upload_sensor'),
    path ('upload_sim_type', views.upload_sim_type, name='upload_sim_type'),
    path ('upload_sim_qnty', views.upload_sim_qnty, name='upload_sim_qnty'),
    path ('upload_wifi_type', views.upload_wifi_type, name='upload_wifi_type'),
    path ('upload_video_processor_brand', views.upload_video_processor_brand, name='upload_video_processor_brand'),
    path ('upload_screen_resolution', views.upload_screen_resolution, name='upload_screen_resolution'),
    path ('upload_gadget_model', views.upload_gadget_model, name='upload_gadget_model'),
    path ('upload_protection_grade', views.upload_protection_grade, name='upload_protection_grade'),
    path ('upload_gadget_series', views.upload_gadget_series, name='upload_gadget_series'),
    path ('upload_camera_functions', views.upload_camera_functions, name='upload_camera_functions'),
    path ('upload_hazard_grade', views.upload_hazard_grade, name='upload_hazard_grade'),
    path ('upload_colour', views.upload_colour, name='upload_colour'),
    path ('upload_qnty_of_basic_cameras', views.upload_qnty_of_basic_cameras, name='upload_qnty_of_basic_cameras'),
    path ('upload_processor', views.upload_processor, name='upload_processor'),
    path ('upload_video_processor', views.upload_video_processor, name='upload_video_processor'),
    path ('upload_processor_brands', views.upload_processor_brands, name='upload_processor_brands'),
    path ('upload_processor_core_qnty', views.upload_processor_core_qnty, name='upload_processor_core_qnty'),
    path ('upload_processor_model', views.upload_processor_model, name='upload_processor_model'),
    path ('upload_wireless_interfaces', views.upload_wireless_interfaces, name='upload_wireless_interfaces'),
    path ('upload_case_material', views.upload_case_material, name='upload_case_material'),
    path ('upload_operation_systems', views.upload_operation_systems, name='upload_operation_systems'),
    path ('upload_android_versions', views.upload_android_versions, name='upload_android_versions'),
    path ('upload_interfaces', views.upload_interfaces, name='upload_interfaces'),
    path ('upload_communication_standards', views.upload_communication_standards, name='upload_communication_standards'),
    path ('upload_microsd_slots', views.upload_microsd_slots, name='upload_microsd_slots'),
    path ('upload_special_features', views.upload_special_features, name='upload_special_features'),
    path ('upload_special_features_smartphone', views.upload_special_features_smartphone, name='upload_special_features_smartphone'),
    path ('upload_charging_functions', views.upload_charging_functions, name='upload_charging_functions'),
    path ('upload_stabilization', views.upload_stabilization, name='upload_stabilization'),
    path ('upload_authentication', views.upload_authentication, name='upload_authentication'),
    path ('upload_case_forms', views.upload_case_forms, name='upload_case_forms'),
    path ('upload_ios_versions', views.upload_ios_versions, name='upload_ios_versions'),
    path ('upload_euroasian_codes', views.upload_euroasian_codes, name='upload_euroasian_codes'),
    path ('upload_esim_support', views.upload_esim_support, name='upload_esim_support'),
    path ('upload_ram', views.upload_ram, name='upload_ram'),
    path ('upload_publishing_year', views.upload_publishing_year, name='upload_publishing_year'),
    path ('upload_smartphone_versions', views.upload_smartphone_versions, name='upload_smartphone_versions'),
    path ('upload_video_quality', views.upload_video_quality, name='upload_video_quality'),
    path ('upload_json', views.upload_json, name='upload_json'),

    path ('upload_notebook', views.upload_notebook, name='upload_notebook'),
    path ('upload_tv', views.upload_tv, name='upload_tv'),
    path ('upload_videocard', views.upload_videocard, name='upload_videocard'),

    #path ('upload_type_nb', views.upload_type_nb, name='upload_type_nb'),


    #path ('change_tables', views.change_tables, name='change_tables'),
    path ('delete_tables', views.delete_tables, name='delete_tables'),

    
    #path ('upload_smartphone_model', views.upload_smartphone_model, name='upload_smartphone_model')

    #==================================monitor section===========================================
    path ('upload_monitor', views.upload_monitor, name='upload_monitor'),
   


]