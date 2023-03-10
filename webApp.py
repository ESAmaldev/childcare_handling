from flask import Flask, render_template , request
import sqlite3

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/location.html')
def location():

    gov_region=request.args.get("gov_region")
    if(gov_region=="east_mid"): gov_region="East Midlands"
    elif(gov_region=="east_eng"): gov_region="East of England"
    elif(gov_region=="london"): gov_region="London"
    elif(gov_region=="north_east"): gov_region="North East"
    elif(gov_region=="north_west"): gov_region="North West"
    elif(gov_region=="south_east"): gov_region="South East"
    elif(gov_region=="south_west"): gov_region="South West"
    elif(gov_region=="west_mid"): gov_region="West Midlands"
    elif(gov_region=="york_humb"): gov_region="Yorkshire and The Humber"

    con = sqlite3.connect('childcare_data.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    query1="select * from location_data where GOV_REGION LIKE '%"
    query2=query1+gov_region
    q3="%'ORDER BY REG_DATE DESC"
    query4=query2+q3
    cur.execute(query4)
    rows = cur.fetchall()
    con.close()
    return render_template('location.html', rows=rows)

@app.route('/form.html')
def form():
    return render_template('form.html')

@app.route('/success.html', methods=["POST"])
def success():
    pro_type=request.args.get("pro_type")
    if(pro_type=="adopt_support"): pro_type="Adoption Support Agency"
    elif(pro_type=="boarding_school"): pro_type="Boarding School"
    elif(pro_type=="childrens_home"): pro_type="Children's Home"
    elif(pro_type=="college"): pro_type="Further Education College with Residential Accommodation"
    elif(pro_type=="indie_foster"): pro_type="Independent Fostering Agency"
    elif(pro_type=="res_fam_centre"): pro_type="Residential Family Centre"
    elif(pro_type=="res_hol_sch"): pro_type="Residential Holiday Scheme for Disabled Children"
    elif(pro_type=="res_spe_school"): pro_type="Residential Special School"
    elif(pro_type=="res_spe_school_c_h"): pro_type="Residential special school (registered as a children's home)"
    elif(pro_type=="train_centre"): pro_type="Secure Training Centre"
    elif(pro_type=="sec_child_home"): pro_type="Secure children's home"
    elif(pro_type=="Vol_adopt"): pro_type="Voluntary Adoption Agency"
    
    reg_date=request.args.get("reg_date")

    reg_status=request.args.get("reg_status")
    if(reg_status=="active"): reg_status="Active"
    elif(reg_status=="resigned"): reg_status="Resigned"
    elif(reg_status=="cancelled"): reg_status="Cancelled"

    gov_region=request.args.get("gov_region")
    if(gov_region=="east_mid"): gov_region="East Midlands"
    elif(gov_region=="east_eng"): gov_region="East of England"
    elif(gov_region=="london"): gov_region="London"
    elif(gov_region=="north_east"): gov_region="North East"
    elif(gov_region=="north_west"): gov_region="North West"
    elif(gov_region=="south_east"): gov_region="South East"
    elif(gov_region=="south_west"): gov_region="South West"
    elif(gov_region=="west_mid"): gov_region="West Midlands"
    elif(gov_region=="york_humb"): gov_region="Yorkshire and The Humber"

    loc_authority=request.args.get("loc_authority")

    sector=request.args.get("sector")

    constituency=request.args.get("constituency")

    org_owner=request.args.get("org_owner")

    

    event_type=request.args.get("event_type")
    if(event_type=="ful_insp"): event_type="Full inspection"
    elif(event_type=="interim_insp"): event_type="Interim inspection"
    elif(event_type=="monit_insp"): event_type="Monitoring inspection"
    elif(event_type=="emerg_insp"): event_type="SC Emergency inspection"

    insp_date=request.args.get("insp_date")

    publ_date=request.args.get("publ_date")

    event_num=request.args.get("event_num")

    ovrall_exp=request.args.get("ovrall_exp")
    if(ovrall_exp=="null_exp"): ovrall_exp=""
    elif(ovrall_exp=="good_exp"): ovrall_exp="Good"
    elif(ovrall_exp=="outstanding_exp"): ovrall_exp="Outstanding"
    elif(ovrall_exp=="req_imp_exp"): ovrall_exp="Requires improvement"
    elif(ovrall_exp=="inadequate_exp"): ovrall_exp="Inadequate"

    help_eff=request.args.get("help_eff")
    if(help_eff=="null_help"): help_eff=""
    elif(help_eff=="good_help"): help_eff="Good"
    elif(help_eff=="outstanding_help"): help_eff="Outstanding"
    elif(help_eff=="req_imp_help"): help_eff="Requires improvement"
    elif(help_eff=="inadequate_help"): help_eff="Inadequate"

    ovrall_eff=request.args.get("ovrall_eff")
    if(ovrall_eff=="null_eff"): ovrall_eff=""
    elif(ovrall_eff=="good_eff"): ovrall_eff="Good"
    elif(ovrall_eff=="outstanding_eff"): ovrall_eff="Outstanding"
    elif(ovrall_eff=="req_imp_eff"): ovrall_eff="Requires improvement"
    elif(ovrall_eff=="inadequate_eff"): ovrall_eff="Inadequate"

    
    con = sqlite3.connect('childcare_data.db')
    cur = con.cursor()
    try:
        query="INSERT INTO location_data (PROVISION_TYPE ,REG_DATE ,REG_STATUS ,GOV_REGION ,LOCAL_AUTHORITY ,CONSTITUENCY ,SECTOR ,ORG_OWNER ,EVENT_NUM) VALUES (?,?,?,?,?,?,?,?,?)"
        cur.execute(query,(pro_type ,reg_date ,reg_status ,gov_region ,loc_authority ,constituency ,sector ,org_owner ,event_num))
        con.commit()
        query="INSERT INTO inspection_data (EVENT_TYPE ,INSPECT_DATE ,PUBLISH_DATE ,EVENT_NUM ,OVERALL_EXP ,HELP_CARE_EFF ,ADMIN_EFF) VALUES (?,?,?,?,?,?,?)"
        cur.execute(query,(event_type ,insp_date ,publ_date ,event_num ,ovrall_exp ,help_eff ,ovrall_eff))
        con.commit()
        return render_template('success.html')
    except Exception as e:
        print(f'Error adding data to the table: {e}')
    finally:
        con.close()
    return render_template('failure.html')
    
@app.route('/inspection.html', methods=['GET'])
def inspection():

    event_num=request.args.get("event_num")

    con = sqlite3.connect('childcare_data.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    query1="SELECT ins.EVENT_TYPE,ins.INSPECT_DATE,ins.PUBLISH_DATE,ins.EVENT_NUM,ins.OVERALL_EXP,ins.HELP_CARE_EFF,ins.ADMIN_EFF,loc.PROVISION_TYPE,loc.ORG_OWNER FROM inspection_data AS ins INNER JOIN location_data AS loc ON ins.EVENT_NUM=loc.EVENT_NUM AND ins.EVENT_NUM LIKE '%"
    query2=query1+event_num
    q3="%'"
    query4=query2+q3
    print("This is for a test ",query4)
    cur.execute(query4)
    rows = cur.fetchmany(1)
    con.close()
    return render_template('inspection.html', rows=rows)