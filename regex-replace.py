import re

# DS4596

# Input SQL string
input_sql = """
select 'Atlanta' as regionname, count (*) 
from crm.rpl_account as ra 
where isdeleted = 0
and region__c <> 'Atlanta, GA' 
and billingstate = 'Georgia'
union
SELECT 'South Florida' as regionname, COUNT(*)
FROM crm.rpl_account AS ra
WHERE isdeleted = 0
AND region__c <> 'South Florida'
AND billingstate = 'Florida'
union
select 'Philly' as regionname, count (*) 
from crm.rpl_account as ra 
where isdeleted = 0
and region__c <> 'Philadelphia, PA' 
and billingstate = 'Pennsylvania'
union
select 'Arizona' as regionname, count (*) 
from crm.rpl_account as ra 
where isdeleted = 0
and region__c <> 'Phoenix, AZ' 
and billingstate = 'Arizona'
union
select 'Nashville' as regionname, count (*) 
from crm.rpl_account as ra 
where isdeleted = 0
and region__c <> 'Nashville, TN' 
and billingstate = 'Tennessee'
union
select 'Arizona' as regionname, count (*) 
from crm.rpl_account as ra 
where isdeleted = 0
and region__c <> 'Chicago, IL' 
and billingstate = 'Illinois'
union
SELECT 'Overland Park' as regionname, COUNT(*)
FROM crm.rpl_account AS ra
WHERE isdeleted = 0
AND region__c <> 'Overland Park, KS'
AND billingstate = 'Kansas'
"""

# Define the regex pattern to match the desired part
pattern = r"(?i)select '[^']+' as [^,]+, count \(\*\)"

# Replace the matched part with "Select *"
output_sql = re.sub(pattern, "Select *", input_sql)

# Print the modified SQL string
print(output_sql)
