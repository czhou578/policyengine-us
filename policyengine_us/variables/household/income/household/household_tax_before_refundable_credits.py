from policyengine_us.model_api import *


class household_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "total tax before refundable credits"
    documentation = "Total tax liability before refundable credits."
    unit = USD
    definition_period = YEAR

    adds = "gov.household_tax_before_refundable_credits"
