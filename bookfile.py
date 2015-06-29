import convertcobolfiles as ccf

"""
SIMPLE BOOK FILE EXAMPLE


01  REG-SIS099                         PIC X(150).                             
                                                                                                                                                                              
01  REG-SIS099-1.                                                              
    03 COD-TYPE-REG-SIS099-1           PIC 9(001).                             
    03 ID-CLIENT-SIS099-1              PIC 9(014)        COMP-3.               
    03 COD-TYPE-SEX-SIS099-1           PIC 9(001).                             
    03 NAM-CLIENT-SIS099-1             PIC X(050).                             
    03 DT-BIRTHDAY-SIS099-1            PIC 9(008)        COMP-3.               
    03 FILLER                          PIC X(080).                             
    03 SEQ-REG-SIS099-1                PIC 9(009)        COMP-3.               
                                                                                
01  REG-SIS099-2.                                                              
    03 COD-TYPE-REG-SIS099-2           PIC 9(001).                             
    03 ID-CLIENT-SIS099-2              PIC 9(014)        COMP-3.               
    03 COD-TYPE-SEX-SIS099-2           PIC 9(001).                             
    03 NUM-REFERENCE-SIS099-2          PIC 9(018)        COMP-3.               
    03 COD-TYPE-REGISTER-SIS099-2      PIC 9(001).                             
    03 FILLER                          PIC X(124).                             
    03 SEQ-REG-SIS099-2                PIC 9(009)        COMP-3.                                                                                                 
"""


SIZE_BUFFER = 150


COD_TYPE_REG_SIS099_1 = ccf.Field(0, 1, strip=True)
ID_CLIENT_SIS099_1 = ccf.Field(1, 14, strip=True, comp3=True)
COD_TYPE_SEX_SIS099_1 = ccf.Field(2, 1, strip=True)
NAM_CLIENT_SIS099_1 = ccf.Field(3, 50, strip=True)
DT_BIRTHDAY_SIS099_1 = ccf.Field(4, 8, strip=True, comp3=True)
FILLER_1 = ccf.Field(5, 80, strip=True)
SEQ_REG_SIS099_1 = ccf.Field(6, 9, strip=True, comp3=True)

REG_SIS099_1 = [COD_TYPE_REG_SIS099_1, ID_CLIENT_SIS099_1,
                COD_TYPE_SEX_SIS099_1, NAM_CLIENT_SIS099_1,
                DT_BIRTHDAY_SIS099_1, FILLER_1, SEQ_REG_SIS099_1]


COD_TYPE_REG_SIS099_2 = ccf.Field(0, 1, strip=True)
ID_CLIENT_SIS099_2 = ccf.Field(1, 14, strip=True, comp3=True)
COD_TYPE_SEX_SIS099_2 = ccf.Field(2, 1, strip=True)
NUM_REFERENCE_SIS099_2 = ccf.Field(3, 18, strip=True, comp3=True)
COD_TYPE_REGISTER_SIS099_2 = ccf.Field(4, 1, strip=True)
FILLER_2 = ccf.Field(5, 124, strip=True)
SEQ_REG_SIS099_2 = ccf.Field(6, 9, strip=True, comp3=True)

REG_APID056_2 = [COD_TYPE_REG_SIS099_2, ID_CLIENT_SIS099_2,
                 COD_TYPE_SEX_SIS099_2, NUM_REFERENCE_SIS099_2,
                 COD_TYPE_REGISTER_SIS099_2, FILLER_2, SEQ_REG_SIS099_2]
