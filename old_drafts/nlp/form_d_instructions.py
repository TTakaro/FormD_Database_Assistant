form_d_prompt = """
1         Overview

The Form D data provides information extracted from Form D XML submissions in a flattened data format to assist users in more easily consuming the data for analysis. These data includes any amendments to those submissions. The data has been taken directly from submissions created by the registrants and provided as-filed. The data will be published quarterly. Data contained in documents filed after 5:30pm EST on the last business day of the quarter will be included in the next quarterly posting.

DISCLAIMER: The Form D Data contains information derived from structured data filed with the Commission by individual registrants as well as Commission-generated filing identifiers. Because the data is derived from information provided by individual registrants, we cannot guarantee the accuracy of the data. In addition, it is possible inaccuracies or other errors were introduced into the data during the process of extracting the data and compiling. Finally, the data does not reflect all available information, including certain metadata associated with Commission filings. The data is intended to assist the public in analyzing data contained in Commission filings; however, it is not a substitute for such filings. Investors should review the full Commission filings before making any investment decision.

The data extracted from the Form D XML submissions is organized into six tab-delimited TXT format files as follows:

·         FORMDSUBMISSION

·         ISSUERS

·         OFFERING

·         RECIPIENTS

·         RELATEDPERSONS

·         SIGNATURES
2         Scope

The Form D Data consists of XML data submitted from Jan 2008 through current period.

The Form D Data publishing files do not include data from attachments or other optional information that may have been included in a submission.

Note:  The EDGAR Form D XML Technical Specification provides additional information regarding the Form D submissions.
3         Organization

Note that the data includes Form D information "as filed" in EDGAR document submissions including amendments of prior submissions.  Data in this submitted form may contain redundancies, inconsistencies, and discrepancies relative to prior submissions and other publication formats.  There are six data files.  Each quarterly data is accompanied by a metadata file conforming to the W3C specification for tabular data (https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/ ) that encodes the following information about the data files and their relationships to each other.

1.    FORMDSUBMISSION identifies the Form D EDGAR XML submissions, with each row having the primary key ACCESSIONNUMBER.

2.    ISSUERS data is the issuer information for each submission, with each row having the primary key ACCESSIONNUMBER and ISSUER_SEQ_KEY.

3.    OFFERING data is the offering information, with each row having the primary key ACCESSIONNUMBER.

4.    RECIPIENTS data contains recipients’ information related to the submissions, with each row having the primary key ACCESSIONNUMBER and RECIPIENT_SEQ_KEY.

5.    RELATEDPERSONS data contains information of related persons in a submission, with each row having the primary key ACCESSIONNUMBER and RELATEDPERSON_SEQ_KEY.

6.    SIGNATURES data provides the data from the person signatures, with each row having the primary key ACCESSIONNUMBER and SIGNATURE_SEQ_KEY.

ACCESSIONNUMBER can be used to retrieve information about a submission in the data files.  ACCESSIONNUMBER and XXX_SEQ_KEY can be used to obtain data reported on multiple lines in the submission.
4         File Formats

Each of the six data files provide text format, tab delimited, utf-8 encoding.
5         File Header Definitions

The fields in the figures below (figures 1 - 6) provide the following information: field name, description, data format, maximum field size, an indication of whether or not the field may be NULL (yes or no), and key. 

The Key field indicates whether the field is part of a unique index on the data.  There are two possible values for this field:

·         "*"   Indicates the field is part of the unique key for the row.

·         Empty (nothing in field)   the field is not part of the unique compound key.
5.1       FORMDSUBMISSION

The FORMDSUBMISSION data file contains summary information about the submission and filer.

Figure 1. Fields in the FORMDSUBMISSION data file

Field Name
	

Field Description
	

Format
	

Max Size
	

May be NULL
	

Key

ACCESSIONNUMBER
	

The 20-character string formed from the 18-digit number assigned by the Commission to each EDGAR submission.
	

ALPHANUMERIC (nnnnnnnnnn-nn-nnnnnn)
	

20
	

No
	

*

FILE_NUM
	

File Number provided by Commission for the submission. The File Number is sourced from EDGAR.
	

ALPHANUMERIC
	

30
	

Yes
	

 

FILING_DATE
	

Date filed with the Commission. The Filing Date is sourced from EDGAR.
	

DATE (DD-MMM-YY)
	

8
	

Yes
	

 

SIC_CODE
	

Standard Industrial Classification Codes. These codes are also used as a basis for assigning review responsibility for the company's filings.
	

ALPHANUMERIC
	

4
	

Yes
	

 

SUBMISSIONTYPE
	

Submission type
	

ALPHANUMERIC
	

255
	

No
	

 

OVER100PERSONSFLAG
	

Yes, if over 100 persons.
	

ALPHANUMERIC
	

5
	

Yes
	

 

OVER100ISSUERFLAG
	

Yes, if over 100 issuers.
	

ALPHANUMERIC
	

5
	

Yes
	

 

 

Note: To access the complete submission files for a given filing, please see the Commission EDGAR website.  The Commission website folder https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/ will always contain all the data sets for a given submission. To assemble the folder address to any filing referenced in the FORMDSUBMISSION data set, simply substitute {cik} with the CIK (see ISSUERS) field and replace {accession} with the ACCESSIONNUMBER field (after removing the dash character).

 
5.2       ISSUERS

The ISSUERS data file contains specified information for the issuer provided in the submission.

Figure 2. Fields in the ISSUERS data file

Field Name
	

Field Description
	

Format
	

Max Size
	

May be NULL
	

Key

ACCESSIONNUMBER
	

The 20-character string formed from the 18-digit number assigned by the Commission to each EDGAR submission.
	

ALPHANUMERIC (nnnnnnnnnn-nn-nnnnnn)
	

20
	

No
	

*

IS_PRIMARYISSUER_FLAG
	

Yes, if primary issuer; No if not
	

ALPHANUMERIC
	

3
	

No
	

ISSUER_SEQ_KEY
	

Issuer index key.
	

NUMERIC
	

38
	

No
	

*

CIK
	

Central index key (CIK) of issuer submitting the filing.
	

ALPHANUMERIC
	

10
	

No
	

ENTITYNAME
	

Name of Issuer
	

ALPHANUMERIC
	

150
	

Yes
	

STREET1
	

Street Address 1
	

ALPHANUMERIC
	

40
	

No
	

STREET2
	

Street Address 2
	

ALPHANUMERIC
	

40
	

Yes
	

CITY
	

City
	

ALPHANUMERIC
	

30
	

No
	

STATEORCOUNTRY
	

State/Province/Country
	

ALPHANUMERIC
	

255
	

No
	

STATEORCOUNTRYDESCRIPTION
	

Full name of the country or state
	

ALPHANUMERIC
	

50
	

Yes
	

ZIPCODE
	

Zip/Postal Code
	

ALPHANUMERIC
	

10
	

No
	

ISSUERPHONENUMBER
	

Phone No. of Issuer
	

ALPHANUMERIC
	

20
	

No
	

JURISDICTIONOFINC
	

Jurisdiction of Incorporation/Organization
	

ALPHANUMERIC
	

50
	

Yes
	

ISSUER_PREVIOUSNAME_1
	

Issuer Previous Name 1
	

ALPHANUMERIC
	

150
	

Yes
	

ISSUER_PREVIOUSNAME_2
	

Issuer Previous Name 2
	

ALPHANUMERIC
	

150
	

Yes
	

ISSUER_PREVIOUSNAME_3
	

Issuer Previous Name 3
	

ALPHANUMERIC
	

150
	

Yes
	

EDGAR_PREVIOUSNAME_1
	

EDGAR  Previous Name 1
	

ALPHANUMERIC
	

150
	

Yes
	

EDGAR_PREVIOUSNAME_2
	

EDGAR  Previous Name 2
	

ALPHANUMERIC
	

150
	

Yes
	

EDGAR_PREVIOUSNAME_3
	

EDGAR  Previous Name 3
	

ALPHANUMERIC
	

150
	

Yes
	

ENTITYTYPE
	

Entity type
	

ALPHANUMERIC
	

255
	

No
	

ENTITYTYPEOTHERDESC
	

Description of Entity Type when indicated as 'Other' in Entity Type
	

ALPHANUMERIC
	

255
	

Yes
	

YEAROFINC_TIMESPAN_CHOICE
	

Year of Incorporation/Organization (Specify Year) Within Last Five Years (Specify Year)
	

ALPHANUMERIC
	

150
	

No
	

YEAROFINC_VALUE_ENTERED
	

Year of Incorporation value entered
	

ALPHANUMERIC
	

4
	

Yes
	

 
5.3       OFFERING

The OFFERING data file contains information regarding the offering requirements.

Figure 3. Fields in the OFFERING data file

Field Name
	

Field Description
	

Format
	

Max Size
	

May be NULL
	

Key

ACCESSIONNUMBER
	

The 20-character string formed from the 18-digit number assigned by the Commission to each EDGAR submission.
	

ALPHANUMERIC (nnnnnnnnnn-nn-nnnnnn)
	

20
	

No
	

*

INDUSTRYGROUPTYPE
	

Type of Industry
	

ALPHANUMERIC
	

255
	

No
	

INVESTMENTFUNDTYPE
	

Type of Securities Offered
	

ALPHANUMERIC
	

255
	

Yes
	

IS40ACT
	

Flag to indicate whether the issuer registered as an investment

company under the Investment Company

Act of 1940
	

ALPHANUMERIC
	

5
	

Yes
	

REVENUERANGE
	

Revenue Range
	

ALPHANUMERIC
	

255
	

Yes
	

AGGREGATENETASSETVALUERANGE
	

Aggregate Net Asset Value Range
	

ALPHANUMERIC
	

255
	

Yes
	

FEDERALEXEMPTIONS_ITEMS_LIST
	

List of exemptions under Securities Act
	

ALPHANUMERIC
	

1000
	

Yes
	

ISAMENDMENT
	

New Notice /Amendment
	

ALPHANUMERIC
	

5
	

No
	

PREVIOUSACCESSIONNUMBER
	

Previous Accession Number; The 20-character string formed from the 18-digit number assigned by the Commission to each EDGAR submission.
	

ALPHANUMERIC
	

20
	

Yes
	

SALE_DATE
	

Sale Date
	

ALPHANUMERIC
	

255
	

Yes
	

YETTOOCCUR
	

First Sale Yet to Occur
	

ALPHANUMERIC
	

5
	

Yes
	

MORETHANONEYEAR
	

Duration of offering more than one year
	

ALPHANUMERIC
	

5
	

No
	

ISEQUITYTYPE
	

Equity
	

ALPHANUMERIC
	

5
	

Yes
	

ISDEBTTYPE
	

Debt
	

ALPHANUMERIC
	

5
	

Yes
	

ISOPTIONTOACQUIRETYPE
	

Option, Warrant or Other Right to Acquire Another Security
	

ALPHANUMERIC
	

5
	

Yes
	

ISSECURITYTOBEACQUIREDTYPE
	

Security to be Acquired Upon Exercise of Option, Warrant or Other Right to Acquire Security
	

ALPHANUMERIC
	

5
	

Yes
	

ISPOOLEDINVESTMENTFUNDTYPE
	

Pooled Investment Fund Interests
	

ALPHANUMERIC
	

5
	

Yes
	

ISTENANTINCOMMONTYPE
	

Tenant-in-Common Securities
	

ALPHANUMERIC
	

5
	

Yes
	

ISMINERALPROPERTYTYPE
	

Mineral Property Securities
	

ALPHANUMERIC
	

5
	

Yes
	

ISOTHERTYPE
	

Other (describe)
	

ALPHANUMERIC
	

5
	

Yes
	

DESCRIPTIONOFOTHERTYPE
	

Description of Pooled Investment Type when indicated as 'Other' in 'OtherType' as Pooled Investment Type
	

ALPHANUMERIC
	

255
	

Yes
	

ISBUSINESSCOMBINATIONTRANS
	

Is this offering being made in connection with a business combination transaction, such as a merger, acquisition, or exchange offer?
	

ALPHANUMERIC
	

5
	

No
	

BUSCOMBCLARIFICATIONOFRESP
	

Clarification of Response (if Necessary)
	

ALPHANUMERIC
	

255
	

Yes
	

MINIMUMINVESTMENTACCEPTED
	

Minimum investment accepted from any outside investor
	

NUMERIC
	

19
	

No
	

OVER100RECIPIENTFLAG
	

Over 100 recipients
	

ALPHANUMERIC
	

5
	

Yes
	

TOTALOFFERINGAMOUNT
	

Total offering amount
	

ALPHANUMERIC
	

12
	

No
	

TOTALAMOUNTSOLD
	

Total amount sold
	

NUMERIC
	

12
	

No
	

TOTALREMAINING
	

Total remaining to be sold
	

ALPHANUMERIC
	

12
	

No
	

SALESAMTCLARIFICATIONOFRESP
	

Clarification of Response (if Necessary)
	

ALPHANUMERIC
	

255
	

Yes
	

HASNONACCREDITEDINVESTORS
	

Select if securities in the offering have been or may be sold to persons who do not qualify as accredited investors
	

ALPHANUMERIC
	

5
	

No
	

NUMBERNONACCREDITEDINVESTORS
	

Number of such non-accredited investors who already have invested in the offering
	

NUMERIC
	

19
	

Yes
	

TOTALNUMBERALREADYINVESTED
	

Regardless of whether securities in the offering have been or may be sold to persons who do not qualify as accredited investors, enter the total number of investors who already have invested in the offering.
	

NUMERIC
	

19
	

No
	

SALESCOMM_DOLLARAMOUNT
	

Sales Commissions, USD
	

NUMERIC
	

12
	

No
	

SALESCOMM_ISESTIMATE
	

Estimate
	

ALPHANUMERIC
	

5
	

Yes
	

FINDERSFEE_DOLLARAMOUNT
	

Finders  Fee USD
	

NUMERIC
	

12
	

No
	

FINDERSFEE_ISESTIMATE
	

Estimate
	

ALPHANUMERIC
	

5
	

Yes
	

FINDERFEECLARIFICATIONOFRESP
	

Clarification of Response (if Necessary)
	

ALPHANUMERIC
	

255
	

Yes
	

GROSSPROCEEDSUSED_DOLLARAMOUNT
	

Provide the amount of the gross proceeds of the offering that has been or is proposed to be used for payments to any of the persons required to be named as executive officers, directors, or promoters in response to Item 3 above. If the amount is unknown, provide an estimate and check the box next to the amount. USD
	

NUMERIC
	

12
	

No
	

GROSSPROCEEDSUSED_ISESTIMATE
	

Estimate
	

ALPHANUMERIC
	

5
	

Yes
	

GROSSPROCEEDSUSED_CLAROFRESP
	

Clarification of Response (if Necessary)
	

ALPHANUMERIC
	

255
	

Yes
	

AUTHORIZEDREPRESENTATIVE
	

I also am a duly authorized representative of the other Issuer(s) in Item 1 above and authorized to sign on their behalf.
	

ALPHANUMERIC
	

5
	

Yes
	

 
5.4       RECIPIENTS

The RECIPIENTS data file contains the recipients information.

Figure 4. Fields in the RECIPIENTS data file

Field Name
	

Field Description
	

Format
	

Max Size
	

May be NULL
	

Key

ACCESSIONNUMBER
	

The 20-character string formed from the 18-digit number assigned by the Commission to each EDGAR submission.
	

ALPHANUMERIC (nnnnnnnnnn-nn-nnnnnn)
	

20
	

No
	

*

RECIPIENT_SEQ_KEY
	

Recipient index key.
	

NUMERIC
	

38
	

No
	

*

RECIPIENTNAME
	

Recipient
	

ALPHANUMERIC
	

150
	

No
	

RECIPIENTCRDNUMBER
	

Recipient CRD Number
	

ALPHANUMERIC
	

9
	

No
	

ASSOCIATEDBDNAME
	

(Associated) Broker or Dealer
	

ALPHANUMERIC
	

150
	

No
	

ASSOCIATEDBDCRDNUMBER
	

(Associated) Broker or Dealer CRD Number
	

ALPHANUMERIC
	

9
	

No
	

STREET1
	

Street Address 1
	

ALPHANUMERIC
	

40
	

No
	

STREET2
	

Street Address 2
	

ALPHANUMERIC
	

40
	

Yes
	

CITY
	

City
	

ALPHANUMERIC
	

30
	

No
	

STATEORCOUNTRY
	

State/Province/Country
	

ALPHANUMERIC
	

255
	

No
	

STATEORCOUNTRYDESCRIPTION
	

Full name of the country or state
	

ALPHANUMERIC
	

50
	

Yes
	

ZIPCODE
	

Zip/Postal Code
	

ALPHANUMERIC
	

10
	

No
	

STATES_OR_VALUE_LIST
	

List of States or Countries of Recipients
	

ALPHANUMERIC
	

1000
	

Yes
	

DESCRIPTIONS_LIST
	

Full name of States or Countries of Recipients
	

ALPHANUMERIC
	

1000
	

Yes
	

FOREIGNSOLICITATION
	

Selected if the recipient has solicited sales in foreign countries.
	

ALPHANUMERIC
	

5
	

Yes
	
5.5       RELATEDPERSONS

The RELATEDPERSONS data file provides information of related persons with the submission.

Figure 5. Fields in the RELATEDPERSONS data file

Field Name
	

Field Description
	

Format
	

Max Size
	

May be NULL
	

Key

ACCESSIONNUMBER
	

The 20-character string formed from the 18-digit number assigned by the Commission to each EDGAR submission.
	

ALPHANUMERIC (nnnnnnnnnn-nn-nnnnnn)
	

20
	

No
	

*

RELATEDPERSON_SEQ_KEY
	

Related person index key.
	

NUMERIC
	

38
	

No
	

*

FIRSTNAME
	

First Name
	

ALPHANUMERIC
	

150
	

No
	

MIDDLENAME
	

Middle Name
	

ALPHANUMERIC
	

150
	

Yes
	

LASTNAME
	

Last Name
	

ALPHANUMERIC
	

150
	

No
	

STREET1
	

Street Address 1
	

ALPHANUMERIC
	

40
	

No
	

STREET2
	

Street Address 2
	

ALPHANUMERIC
	

40
	

Yes
	

CITY
	

City
	

ALPHANUMERIC
	

30
	

No
	

STATEORCOUNTRY
	

State/Province/Country
	

ALPHANUMERIC
	

255
	

No
	

STATEORCOUNTRYDESCRIPTION
	

Full name of the country or state
	

ALPHANUMERIC
	

50
	

Yes
	

ZIPCODE
	

Zip/Postal Code
	

ALPHANUMERIC
	

10
	

No
	

RELATIONSHIP_1
	

Relationship of related person to issuer consisting of Executive Officer, Director, or Promoter.
	

ALPHANUMERIC
	

255
	

Yes
	

RELATIONSHIP_2
	

Relationship of related person to issuer consisting of Executive Officer, Director, or Promoter.
	

ALPHANUMERIC
	

255
	

Yes
	

RELATIONSHIP_3
	

Relationship of related person to issuer consisting of Executive Officer, Director, or Promoter.
	

ALPHANUMERIC
	

255
	

Yes
	

RELATIONSHIPCLARIFICATION
	

Clarification of Response (if Necessary)
	

ALPHANUMERIC
	

255
	

Yes
	
5.6       SIGNATURES

The SIGNATURES data file provides data for the submission person signature.

Figure 6. Fields in the SIGNATURES data file

Field Name
	

Field Description
	

Format
	

Max Size
	

May be NULL
	

Key

ACCESSIONNUMBER
	

The 20-character string formed from the 18-digit number assigned by the Commission to each EDGAR submission.
	

ALPHANUMERIC (nnnnnnnnnn-nn-nnnnnn)
	

20
	

No
	

*

SIGNATURE_SEQ_KEY
	

Signature index key.
	

NUMERIC
	

38
	

No
	

*

ISSUERNAME
	

Name of Issuer
	

ALPHANUMERIC
	

150
	

No
	

SIGNATURENAME
	

Name of signature
	

ALPHANUMERIC
	

30
	

No
	

NAMEOFSIGNER
	

Full name of person signing the form.
	

ALPHANUMERIC
	

150
	

No
	

SIGNATURETITLE
	

Title of person signing the form.
	

ALPHANUMERIC
	

60
	

No
	

SIGNATUREDATE
	

Date of signature.
	

ALPHANUMERIC
	

255
	

No
	

 

 

6         Appendix

U.S. State/Country Codes and Descriptions

 

 

US State / Country Codes
	

Descriptions

AL
	

ALABAMA

AK
	

ALASKA

AZ
	

ARIZONA

AR
	

ARKANSAS

CA
	

CALIFORNIA

CO
	

COLORADO

CT
	

CONNECTICUT

DE
	

DELAWARE

DC
	

DISTRICT OF COLUMBIA

FL
	

FLORIDA

GA
	

GEORGIA

GU
	

GUAM

HI
	

HAWAII

ID
	

IDAHO

IL
	

ILLINOIS

IN
	

INDIANA

IA
	

IOWA

KS
	

KANSAS

KY
	

KENTUCKY

LA
	

LOUISIANA

ME
	

MAINE

MD
	

MARYLAND

MA
	

MASSACHUSETTS

MI
	

MICHIGAN

MN
	

MINNESOTA

MS
	

MISSISSIPPI

MO
	

MISSOURI

MT
	

MONTANA

NE
	

NEBRASKA

NV
	

NEVADA

NH
	

NEW HAMPSHIRE

NJ
	

NEW JERSEY

NM
	

NEW MEXICO

NY
	

NEW YORK

NC
	

NORTH CAROLINA

ND
	

NORTH DAKOTA

OH
	

OHIO

OK
	

OKLAHOMA

OR
	

OREGON

PA
	

PENNSYLVANIA

RI
	

RHODE ISLAND

SC
	

SOUTH CAROLINA

SD
	

SOUTH DAKOTA

TN
	

TENNESSEE

TX
	

TEXAS

UT
	

UTAH

VT
	

VERMONT

VA
	

VIRGINIA

WA
	

WASHINGTON

WV
	

WEST VIRGINIA

WI
	

WISCONSIN

WY
	

WYOMING

PR
	

PUERTO RICO

VI
	

VIRGIN ISLANDS, U.S.

A0
	

ALBERTA, CANADA

A1
	

BRITISH COLUMBIA, CANADA

Z4
	

CANADA (FEDERAL LEVEL)

A2
	

MANITOBA, CANADA

A3
	

NEW BRUNSWICK, CANADA

A4
	

NEWFOUNDLAND, CANADA

A5
	

NOVA SCOTIA, CANADA

A6
	

ONTARIO, CANADA

A7
	

PRINCE EDWARD ISLAND, CANADA

A8
	

QUEBEC, CANADA

A9
	

SASKATCHEWAN, CANADA

B0
	

YUKON, CANADA

B2
	

AFGHANISTAN

Y6
	

ALAND ISLANDS

B3
	

ALBANIA

B4
	

ALGERIA

B5
	

AMERICAN SAMOA

B6
	

ANDORRA

B7
	

ANGOLA

1A
	

ANGUILLA

B8
	

ANTARCTICA

B9
	

ANTIGUA AND BARBUDA

C1
	

ARGENTINA

1B
	

ARMENIA

1C
	

ARUBA

C3
	

AUSTRALIA

C4
	

AUSTRIA

1D
	

AZERBAIJAN

C5
	

BAHAMAS

C6
	

BAHRAIN

C7
	

BANGLADESH

C8
	

BARBADOS

1F
	

BELARUS

C9
	

BELGIUM

D1
	

BELIZE

G6
	

BENIN

D0
	

BERMUDA

D2
	

BHUTAN

D3
	

BOLIVIA

1E
	

BOSNIA AND HERZEGOVINA

B1
	

BOTSWANA

D4
	

BOUVET ISLAND

D5
	

BRAZIL

D6
	

BRITISH INDIAN OCEAN TERRITORY

D9
	

BRUNEI DARUSSALAM

E0
	

BULGARIA

X2
	

BURKINA FASO

E2
	

BURUNDI

E3
	

CAMBODIA

E4
	

CAMEROON

E8
	

CAPE VERDE

E9
	

CAYMAN ISLANDS

F0
	

CENTRAL AFRICAN REPUBLIC

F2
	

CHAD

F3
	

CHILE

F4
	

CHINA

F6
	

CHRISTMAS ISLAND

F7
	

COCOS (KEELING) ISLANDS

F8
	

COLOMBIA

F9
	

COMOROS

G0
	

CONGO

Y3
	

CONGO, THE DEMOCRATIC REPUBLIC OF THE

G1
	

COOK ISLANDS

G2
	

COSTA RICA

L7
	

COTE D'IVOIRE

1M
	

CROATIA

G3
	

CUBA

G4
	

CYPRUS

2N
	

CZECH REPUBLIC

G7
	

DENMARK

1G
	

DJIBOUTI

G9
	

DOMINICA

G8
	

DOMINICAN REPUBLIC

H1
	

ECUADOR

H2
	

EGYPT

H3
	

EL SALVADOR

H4
	

EQUATORIAL GUINEA

1J
	

ERITREA

1H
	

ESTONIA

H5
	

ETHIOPIA

H7
	

FALKLAND ISLANDS (MALVINAS)

H6
	

FAROE ISLANDS

H8
	

FIJI

H9
	

FINLAND

I0
	

FRANCE

I3
	

FRENCH GUIANA

I4
	

FRENCH POLYNESIA

2C
	

FRENCH SOUTHERN TERRITORIES

I5
	

GABON

I6
	

GAMBIA

2Q
	

GEORGIA

2M
	

GERMANY

J0
	

GHANA

J1
	

GIBRALTAR

J3
	

GREECE

J4
	

GREENLAND

J5
	

GRENADA

J6
	

GUADELOUPE

J8
	

GUATEMALA

Y7
	

GUERNSEY

J9
	

GUINEA

S0
	

GUINEA-BISSAU

K0
	

GUYANA

K1
	

HAITI

K4
	

HEARD ISLAND AND MCDONALD ISLANDS

X4
	

HOLY SEE (VATICAN CITY STATE)

K2
	

HONDURAS

K3
	

HONG KONG

K5
	

HUNGARY

K6
	

ICELAND

K7
	

INDIA

K8
	

INDONESIA

K9
	

IRAN, ISLAMIC REPUBLIC OF

L0
	

IRAQ

L2
	

IRELAND

Y8
	

ISLE OF MAN

L3
	

ISRAEL

L6
	

ITALY

L8
	

JAMAICA

M0
	

JAPAN

Y9
	

JERSEY

M2
	

JORDAN

1P
	

KAZAKSTAN

M3
	

KENYA

J2
	

KIRIBATI

M4
	

KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF

M5
	

KOREA, REPUBLIC OF

M6
	

KUWAIT

1N
	

KYRGYZSTAN

M7
	

LAO PEOPLE'S DEMOCRATIC REPUBLIC

1R
	

LATVIA

M8
	

LEBANON

M9
	

LESOTHO

N0
	

LIBERIA

N1
	

LIBYAN ARAB JAMAHIRIYA

N2
	

LIECHTENSTEIN

1Q
	

LITHUANIA

N4
	

LUXEMBOURG

N5
	

MACAU

1U
	

MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF

N6
	

MADAGASCAR

N7
	

MALAWI

N8
	

MALAYSIA

N9
	

MALDIVES

O0
	

MALI

O1
	

MALTA

1T
	

MARSHALL ISLANDS

O2
	

MARTINIQUE

O3
	

MAURITANIA

O4
	

MAURITIUS

2P
	

MAYOTTE

O5
	

MEXICO

1K
	

MICRONESIA, FEDERATED STATES OF

1S
	

MOLDOVA, REPUBLIC OF

O9
	

MONACO

P0
	

MONGOLIA

Z5
	

MONTENEGRO

P1
	

MONTSERRAT

P2
	

MOROCCO

P3
	

MOZAMBIQUE

E1
	

MYANMAR

T6
	

NAMIBIA

P5
	

NAURU

P6
	

NEPAL

P7
	

NETHERLANDS

P8
	

NETHERLANDS ANTILLES

1W
	

NEW CALEDONIA

Q2
	

NEW ZEALAND

Q3
	

NICARAGUA

Q4
	

NIGER

Q5
	

NIGERIA

Q6
	

NIUE

Q7
	

NORFOLK ISLAND

1V
	

NORTHERN MARIANA ISLANDS

Q8
	

NORWAY

P4
	

OMAN

R0
	

PAKISTAN

1Y
	

PALAU

1X
	

PALESTINIAN TERRITORY, OCCUPIED

R1
	

PANAMA

R2
	

PAPUA NEW GUINEA

R4
	

PARAGUAY

R5
	

PERU

R6
	

PHILIPPINES

R8
	

PITCAIRN

R9
	

POLAND

S1
	

PORTUGAL

S3
	

QATAR

S4
	

REUNION

S5
	

ROMANIA

1Z
	

RUSSIAN FEDERATION

S6
	

RWANDA

Z0
	

SAINT BARTHELEMY

U8
	

SAINT HELENA

U7
	

SAINT KITTS AND NEVIS

U9
	

SAINT LUCIA

Z1
	

SAINT MARTIN

V0
	

SAINT PIERRE AND MIQUELON

V1
	

SAINT VINCENT AND THE GRENADINES

Y0
	

SAMOA

S8
	

SAN MARINO

S9
	

SAO TOME AND PRINCIPE

T0
	

SAUDI ARABIA

T1
	

SENEGAL

Z2
	

SERBIA

T2
	

SEYCHELLES

T8
	

SIERRA LEONE

U0
	

SINGAPORE

2B
	

SLOVAKIA

2A
	

SLOVENIA

D7
	

SOLOMON ISLANDS

U1
	

SOMALIA

T3
	

SOUTH AFRICA

1L
	

SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS

U3
	

SPAIN

F1
	

SRI LANKA

V2
	

SUDAN

V3
	

SURINAME

L9
	

SVALBARD AND JAN MAYEN

V6
	

SWAZILAND

V7
	

SWEDEN

V8
	

SWITZERLAND

V9
	

SYRIAN ARAB REPUBLIC

F5
	

TAIWAN, PROVINCE OF CHINA

2D
	

TAJIKISTAN

W0
	

TANZANIA, UNITED REPUBLIC OF

W1
	

THAILAND

Z3
	

TIMOR-LESTE

W2
	

TOGO

W3
	

TOKELAU

W4
	

TONGA

W5
	

TRINIDAD AND TOBAGO

W6
	

TUNISIA

W8
	

TURKEY

2E
	

TURKMENISTAN

W7
	

TURKS AND CAICOS ISLANDS

2G
	

TUVALU

W9
	

UGANDA

2H
	

UKRAINE

C0
	

UNITED ARAB EMIRATES

X0
	

UNITED KINGDOM

2J
	

UNITED STATES MINOR OUTLYING ISLANDS

X3
	

URUGUAY

2K
	

UZBEKISTAN

2L
	

VANUATU

X5
	

VENEZUELA

Q1
	

VIET NAM

D8
	

VIRGIN ISLANDS, BRITISH

X8
	

WALLIS AND FUTUNA 
"""