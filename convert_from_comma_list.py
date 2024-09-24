import subprocess

def copy2clip(txt):
    cmd = "echo " + txt.strip() + "|clip"
    return subprocess.check_call(cmd, shell=True)

# Given list of items
items = """
nk_sfacctid, nk_sfacctid, sk_stccustid, sk_stccustid, nk_crmacctid, nk_crmacctid, nk_dotnbr, nk_dotnbr, docketnbr, docketnbr, custnm, custnm, acctlegalnm, acctlegalnm, custtype, custtype, carriertype, carriertype, descr, descr, industry, industry, website, website, annualrev, annualrev, emplnbr, emplnbr, ownership, ownership, tickersymbol, tickersymbol, rating, rating, site, site, acctsrc, acctsrc, trucknbr, trucknbr, leadsrc, leadsrc, language, language, region, region, fuelcardnbr, fuelcardnbr, flt1cardnbr, flt1cardnbr, activefuelcardnbr, activefuelcardnbr, pt_acctid, pt_acctid, pt_supportind, pt_supportind, pt_softver, pt_softver, pt_canceldt, pt_canceldt, pt_hosted, pt_hosted, pt_impltier, pt_impltier, pt_cancelrsn, pt_cancelrsn, pt_billholddt, pt_billholddt, rtsuploadintegrationind, rtsuploadintegrationind, usingediind, usingediind, software, software, tripmgmtstartdt, tripmgmtstartdt, tripmgmtind, trimmgmtind, citrixuserind, citrixuserind, isdeleted, isdeleted, ispartner, ispartnerind, rtscs_salesrepid, rtscs_salesrepid, rtsf_salesrepid, rtsf_salesrepid, rtsi_salesrepid, rtsi_salesrepid, pt_salesrepid, pt_salesrepid, rtsrt_salesrepid, rtsrt_salesrepid, rtsf_opsacctrepid, rtsf_opsacctrepid, crmlastvieweddt, crmlastvieweddt, crmlastreferenceddt, crmlastreferenceddt, crmlastactivitydt, crmlastactivitydt, crmcreatedt, crmcreatedt, crmcreateuserid, crmcreateuserid, crmmodifieddt, crmmodifieddt, crmmodifieduserid, crmmodifieduserid, primcontactphone, primcontactphone, ooidamemberid, ooidamemberid, rtscs_competitor, rtscs_competitor, rtscs_holdind, rtscs_holdind, rtscs_dormantrsn, rtscs_dormantrsn, rtscs_crmactivecustind, rtscs_crmactivecustind, rtsf_crmactivecustind, rtsf_crmactivecustind, rtsi_crmactivecustind, rtsi_crmactivecustind, pt_crmactivecustind, pt_crmactivecustind, crosscorpmbrind, crosscorpmbrind, truckerssolutionind, truckerssolutionind, pt_softwaretier, pt_softwaretier, bundlestat, bundlestat, compliancestat, compliancestat, bundlegracepdenddt, bundlegracepdenddt
"""

# Split the items by comma and newline and strip any extra whitespace
item_list = [item.strip() for item in items.replace("\n", "").split(",")]

# Get unique items by converting the list to a set and then back to a list to maintain order
unique_items = list(set(item_list))

unique_items.sort()

# Join the items with a newline character
formatted_items = "\n".join(unique_items)

# Print the formatted items to verify the output
print(formatted_items)

# Copy to the clipboard
copy2clip(formatted_items)
