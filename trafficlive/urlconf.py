urls = {
    "get_employees": {"method": "GET", "url": "/staff/employee"},
    "get_employee": {"method": "GET", "url": "/staff/employee/%(id)d"},
    "update_employee": {"method": "POST", "url": "/staff/employee"},
    "add_employee": {"method": "PUT", "url": "/staff/employee"},
    "get_departments": {"method": "GET", "url": "/staff/department"},
    "get_department": {"method": "GET", "url": "/staff/department/%(id)d"},
    "update_department": {"method": "POST", "url": "/staff/department"},
    "add_department": {"method": "PUT", "url": "/staff/department"},
    "get_locations": {"method": "GET", "url": "/staff/location"},
    "get_location": {"method": "GET", "url": "/staff/location/%(id)d"},
    "update_location": {"method": "POST", "url": "/staff/location"},
    "add_location": {"method": "PUT", "url": "/staff/location"},
    "get_jobs": {"method": "GET", "url": "/job"},
    "get_job": {"method": "GET", "url": "/job/%(id)d"},
    "update_job": {"method": "POST", "url": "/job"},
    "add_job": {"method": "PUT", "url": "/job"},
    "get_jobdetails": {"method": "GET", "url": "/jobdetail"},
    "get_jobdetail": {"method": "GET", "url": "/jobdetail/%(id)d"},
    "update_jobdetail": {"method": "POST", "url": "/jobdetail"},
    "add_jobdetail": {"method": "PUT", "url": "/jobdetail"},
    "get_projects": {"method": "GET", "url": "/project"},
    "get_project": {"method": "GET", "url": "/project/%(id)d"},
    "update_project": {"method": "POST", "url": "/project"},
    "add_project": {"method": "PUT", "url": "/project"},
    "get_quotes": {"method": "GET", "url": "/quote"},
    "get_quote": {"method": "GET", "url": "/quote/%(id)d"},
    "update_quote": {"method": "POST", "url": "/quote"},
    "add_quote": {"method": "PUT", "url": "/quote"},
    "get_chargebands": {"method": "GET", "url": "/chargeband"},
    "get_chargeband": {"method": "GET", "url": "/chargeband/%(id)d"},
    "update_chargeband": {"method": "POST", "url": "/chargeband"},
    "add_chargeband": {"method": "PUT", "url": "/chargeband"},
    "get_timeentries": {"method": "GET", "url": "/timeentries"},
    "get_timeentry": {"method": "GET", "url": "/timeentries/%(id)d"},
    "update_timeentry": {"method": "POST", "url": "/timeentries"},
    "update_timeentries": {"method": "POST", "url": "/timeentries/batch"},
    "add_timeentry": {"method": "PUT", "url": "/timeentries"},
    "get_clients": {"method": "GET", "url": "/crm/client"},
    "get_client": {"method": "GET", "url": "/crm/client/%(id)d"},
    "update_client": {"method": "POST", "url": "/crm/client"},
    "add_client": {"method": "PUT", "url": "/crm/client"},
    "get_suppliers": {"method": "GET", "url": "/crm/supplier"},
    "get_supplier": {"method": "GET", "url": "/crm/supplier/%(id)d"},
    "update_supplier": {"method": "POST", "url": "/crm/supplier"},
    "add_supplier": {"method": "PUT", "url": "/crm/supplier"},
    "get_others": {"method": "GET", "url": "/crm/other"},
    "get_other": {"method": "GET", "url": "/crm/other/%(id)d"},
    "update_other": {"method": "POST", "url": "/crm/other"},
    "add_other": {"method": "PUT", "url": "/crm/other"},
    "get_addresses": {"method": "GET", "url": "/crm/address"},
    "get_address": {"method": "GET", "url": "/crm/address/%(id)d"},
    "update_address": {"method": "POST", "url": "/crm/address"},
    "add_address": {"method": "PUT", "url": "/crm/address"},
    "get_crm_employees": {"method": "GET", "url": "/crm/employee"},
    "get_crm_employee": {"method": "GET", "url": "/crm/employee/%(id)d"},
    "update_crm_employee": {"method": "POST", "url": "/crm/employee"},
    "add_crm_employee": {"method": "PUT", "url": "/crm/employee"},
    "get_listitems": {"method": "GET", "url": "/listitem/%(type)s"},
    "get_listitem": {"method": "GET", "url": "/listitem/%(type)s/%(id)d"},
    "update_listitem": {"method": "POST", "url": "/listitem/%(type)s"},
    "add_listitem": {"method": "PUT", "url": "/listitem/%(type)s"},
    "delete_listitem": {"method": "DELETE", "url": "/listitem/%(type)s/%(id)d"},
    "get_taxtypes": {"method": "GET", "url": "/taxtype"},
    "get_taxtype": {"method": "GET", "url": "/taxtype/%(id)d"},
    "update_taxtype": {"method": "POST", "url": "/taxtype"},
    "add_taxtype": {"method": "PUT", "url": "/taxtype"},
    "delete_taxtype": {"method": "DELETE", "url": "/taxtype/%(id)d"},
    "get_application_countries": {"method": "GET", "url": "/application/country"},
    "get_application_country": {"method": "GET", "url": "/application/country/%(code)s"},
}
