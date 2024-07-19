string = """211460-Next Generation eCommerce COLO-Production
213197-MyNetWorkingPortal-PRD
213051-Order Capture Layer-PRD
213049-CORONA-PRD
213032-Internet Pricing and Configurator Service-PRD-OCC
213032-Internet Pricing and Configurator Service-PRD-OCC
211240-ADDISON-Production-pricing
211240-ADDISON-Production-inventory
213503-Global Tax Engine-Integration
211240-ADDISON-Production-inventory
213503-Global Tax Engine-Integration
211240-ADDISON-Production-inventory
211240-ADDISON-Production-service-delivery
213032-Internet Pricing and Configurator Service-PRD-OCC
211240-ADDISON-Production
213032-Internet Pricing and Configurator Service-PRD-OCC
211240-ADDISON-Production-pricing
211240-ADDISON-Production-inventory
211240-ADDISON-Production-service-delivery
211289-emdm-production
211240-ADDISON-Production
213051-Order Capture Layer-PRD
210135-Partner Ready Portal (PRP)-Production"""

l = list(set(string.split('\n')))
for x in l:
    print(x)