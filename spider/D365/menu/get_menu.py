#coding:utf-8
import xlrd
import xlsxwriter


# def get_menu(dct):
#     for item in dct["GetDataContract"]:
#         print(item["getTitleStr"])
#         if "GetDataContract" in item:
#             for item_2 in item["GetDataContract"]:
#                 print("======"+item_2["getTitleStr"])
#                 if "GetDataContract" in item_2:
#                     for item_3 in item_2["GetDataContract"]:
#                         print("+++++++++++++++++++"+item_3["getTitleStr"])


# def get_new(dct,n=0):
#     print(str(n)+'. '+dct["getTitleStr"])
#     if "GetDataContract" in dct:
#         n+=1
#         for item in dct["GetDataContract"]:
#             get_new(item,n)
             


# 把结果放到一个lst中，然后，再用for循环写在menu中
# def get_new(dct,n=0,islast=False):
#     if "GetDataContract" in dct:
#         print(str(n)+'. '+dct["getTitleStr"]+"    "+str(islast))
#         n+=1
#         for item in dct["GetDataContract"]:
#             get_new(item,n)
#     else:
#         islast=True
#         print(str(n)+'. '+dct["getTitleStr"]+"    "+str(islast))
     

#[false,1,xxxx]
res=[]
def get_data(dct,n=0,islast=False):
    if "GetDataContract" in dct:
        res.append([islast,n,dct["getTitleStr"]])
        n+=1
        for item in dct["GetDataContract"]:
            get_data(item,n)
    else:
        islast=True
        res.append([islast,n,dct["getTitleStr"]])

    
             


def write_into_xlsx(result):
        workbook = xlsxwriter.Workbook('menu1.xlsx')
        worksheet = workbook.add_worksheet(result[0][2])
        menu_lst=result[1:]
        row=0
        # col=0
        for i in menu_lst:
            worksheet.write(row,0,str(i[0]))#0列写是否是根目录
            worksheet.write(row,i[1],i[2])#n写内容
            row+=1
        workbook.close()



dct2={"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCountStr":"","getFormName":"VendInvoiceWorkspace","getHelpTextStr":"","getImageLocationStr":"Symbol","getImageStr":"Workspace_VendorInvoiceEntry","getKpiNameStr":"","getMenuItemName":"VendInvoiceWorkspace","getMenuItemType":"Display","getSizeStr":"Wide","getTileDisplayStr":"4","getTileName":"VendInvoiceWorkspace","getTilePath":"MenusAccountsPayableWorkspacesVendorinvoiceentry","getTileTypeStr":"Standard","getTitleStr":"Vendor invoice entry","getUrlStr":""},{"getCountStr":"","getFormName":"VendPaymentWorkspace","getHelpTextStr":"","getImageLocationStr":"Symbol","getImageStr":"Workspace_VendorPayments","getKpiNameStr":"","getMenuItemName":"VendPaymentWorkspace","getMenuItemType":"Display","getSizeStr":"Wide","getTileDisplayStr":"4","getTileName":"VendPaymentWorkspaceTile","getTilePath":"MenusAccountsPayableWorkspacesVendorpayments","getTileTypeStr":"Standard","getTitleStr":"Vendor payments","getUrlStr":""}],"getName":"Workspaces","getTitleStr":"Workspaces"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"VendTable","getHelpTextStr":"","getMenuItemName":"VendTableListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"All vendors"},{"getCrumbPath":"","getFormName":"VendTableListPage","getHelpTextStr":"","getMenuItemName":"VendTableHoldListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendors on hold"},{"getCrumbPath":"","getFormName":"VendTableListPage","getHelpTextStr":"","getMenuItemName":"VendTablePastDueListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendors past due"},{"getCrumbPath":"","getFormName":"VendTableListPage","getHelpTextStr":"","getMenuItemName":"VendTableDiverseListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendors who are diverse"},{"getCrumbPath":"","getFormName":"VendExceptionGroup","getHelpTextStr":"","getMenuItemName":"VendExceptionGroup","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor exception groups"},{"getCrumbPath":"","getFormName":"VendGroup","getHelpTextStr":"","getMenuItemName":"VendGroup","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor groups"},{"getCrumbPath":"","getFormName":"VendPriceToleranceGroup","getHelpTextStr":"","getMenuItemName":"VendPriceToleranceGroup","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor price tolerance groups"},{"getCrumbPath":"","getFormName":"Win_SupplierForm","getHelpTextStr":"","getMenuItemName":"Win_SupplierMaintenance1","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Supplier Maintenance"}],"getName":"Vendors","getTitleStr":"Vendors"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"PurchTable","getHelpTextStr":"","getMenuItemName":"PurchTableListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"All purchase orders"},{"getCrumbPath":"","getFormName":"PurchTable","getHelpTextStr":"","getMenuItemName":"PurchTableListPageAssignedToMe","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Purchase orders assigned to me"},{"getCrumbPath":"","getFormName":"PurchTable","getHelpTextStr":"","getMenuItemName":"PurchTableReceivedNotInvoicedListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Purchase orders received but not invoiced"},{"getCrumbPath":"","getFormName":"PurchAgreement","getHelpTextStr":"","getMenuItemName":"PurchAgreementListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Purchase agreements"},{"getCrumbPath":"","getFormName":"PurchPrepayOpenListPage","getHelpTextStr":"","getMenuItemName":"PurchPrepayOpen","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Open prepayments"}],"getName":"PurchaseOrders","getTitleStr":"Purchase orders"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"VendInvoiceInfoListPage","getHelpTextStr":"","getMenuItemName":"VendInvoiceInfoListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Pending vendor invoices"},{"getCrumbPath":"","getFormName":"VendInvoiceInfoListPage","getHelpTextStr":"","getMenuItemName":"VendInvoiceAssignedToMeListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Pending vendor invoices assigned to me"},{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTable9","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Invoice journal"},{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTableVendInvoiceGlobal","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Global invoice journal"},{"getCrumbPath":"","getFormName":"VendOpenInvoicesListPage","getHelpTextStr":"","getMenuItemName":"VendOpenInvoicesListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Open vendor invoices"},{"getCrumbPath":"","getFormName":"VendOpenInvoicesListPage","getHelpTextStr":"","getMenuItemName":"VendOpenInvoicesDueTodayListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor invoices due today"},{"getCrumbPath":"","getFormName":"VendOpenInvoicesListPage","getHelpTextStr":"","getMenuItemName":"VendOpenInvoicesPastDueListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor invoices past due"},{"getCrumbPath":"","getFormName":"VendInvoiceInfoListPage","getHelpTextStr":"","getMenuItemName":"VendInvoiceAssignedToQueuesThatIBelongTo","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor invoices assigned to queues that I belong to"},{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTable6","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Invoice register"},{"getCrumbPath":"","getFormName":"VendTransInvoicePool","getHelpTextStr":"","getMenuItemName":"VendTransInvoicePoolReg","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Invoice pool"},{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTable4","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Invoice approval"}],"getName":"VendorInvoices","getTitleStr":"Invoices"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTable5","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Payment journal"},{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"VendPaymentAssignedToMeListPage","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Payment journals assigned to me"},{"getCrumbPath":"","getFormName":"VendPostDatedChecks","getHelpTextStr":"","getMenuItemName":"VendPostDatedChecks","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor postdated checks"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTable_VendDrawNote","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Draw promissory note journal"},{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTable_VendRedrawNote","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Redraw promissory note journal"},{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTable_VendPaymRemittance","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Remittance journal"},{"getCrumbPath":"","getFormName":"LedgerJournalTable","getHelpTextStr":"","getMenuItemName":"LedgerJournalTable_VendSettleNote","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Settle promissory note journal"}],"getName":"PromissoryNotes","getTitleStr":"Promissory notes"}],"getName":"Payments","getTitleStr":"Payments"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"MCRBrokerContractmanagement","getHelpTextStr":"","getMenuItemName":"MCRBrokerContractTable","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Broker contracts"},{"getCrumbPath":"","getFormName":"MCRBrokerClaims","getHelpTextStr":"","getMenuItemName":"MCRBrokerClaims","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Broker claims"},{"getCrumbPath":"","getFormName":"MCRRoyaltyTable","getHelpTextStr":"","getMenuItemName":"MCRRoyaltyTable","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Royalty agreements"},{"getCrumbPath":"","getFormName":"MCRRoyaltyVendTable","getHelpTextStr":"","getMenuItemName":"MCRRoyaltyVendTableEdit","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Royalty claims"},{"getCrumbPath":"","getFormName":"MCRBrokerWriteOffReason","getHelpTextStr":"","getMenuItemName":"MCRBrokerDifferentialReason","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Differential reasons"}],"getName":"MCRBrokerAndRoyalties","getTitleStr":"Broker and royalties"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"VendPackingSlipJournal","getHelpTextStr":"","getMenuItemName":"VendPackingSlipJournal","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Product receipt"},{"getCrumbPath":"","getFormName":"vendbalancelist_CN","getHelpTextStr":"","getMenuItemName":"VendBalanceList_CN","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor balance"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendAgingBalance","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor aging report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendTransList","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor transactions report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendLedgerTrans","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"History by transaction report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"MCRBrokerARInvoices","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Broker open AR invoices report"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendAccountStatementInt","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Account statement"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"PurchRankingReport","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Top 100 vendors"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendProvisionalBalance","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor balance list"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendBalanceList","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor balance list with credit limit"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendBasedata","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor base data"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendInvoiceVolume","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor invoice turnover"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendPhoneList","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor phone list"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendLedgerReconciliation_NoReportLabel","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor to ledger reconciliation"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendorListBasic","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendors"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendLedgerTransactions_CN","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor details"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendTransactionwithAgingAnalysis_CN","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor details with aging"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendAging_CN","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor aging - China"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendBalance_CN","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor balance report (China)"}],"getName":"Vendor","getTitleStr":"Vendor reports"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"LedgerTransListAccountVend","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Ledger posting for purchase orders"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"InventPurchAccruals","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Pre-upgrade remaining accruals"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"PurchAgreementCertificationCompliance","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Purchase agreement certification compliance"}],"getName":"PurchaseOrderReports","getTitleStr":"Purchase order reports"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"VendInvoicePostingHistory","getHelpTextStr":"","getMenuItemName":"PurchPostingHistoryInvoiceApproval","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Approval journal history and matching details"},{"getCrumbPath":"","getFormName":"VendInvoicePostingHistory","getHelpTextStr":"","getMenuItemName":"PurchPostingHistoryInvoice","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Invoice history and matching details"},{"getCrumbPath":"","getFormName":"VendInvoiceJournal","getHelpTextStr":"","getMenuItemName":"VendInvoiceJournal","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Invoice journal"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendAccruedPurchases","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Accrued purchases excluding sales tax report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendReportApproveCollection","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Invoices not approved report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendInvoiceSpec","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Invoice specification report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendInvoiceJourReport","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor invoice journal report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendInvoice","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor invoice transactions report"}],"getName":"InvoiceInquiriesAndReports","getTitleStr":"Invoice"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"PaymFeeInquiry","getHelpTextStr":"","getMenuItemName":"VendPaymFeeInquiry","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Payment fee"},{"getCrumbPath":"","getFormName":"VendPromissoryNoteJour","getHelpTextStr":"","getMenuItemName":"VendPromissoryNoteJour","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Promissory note journal"},{"getCrumbPath":"","getFormName":"VendPromissoryNoteStatistics","getHelpTextStr":"","getMenuItemName":"VendPromissoryNoteStat","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Promissory note statistics"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendPostPaymJournal","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor posted payment journal report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendPromissoryNoteReport","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Promissory note journal report"}],"getName":"PaymentInquiriesAndReports","getTitleStr":"Payment"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendPayableTransaction_CN","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Payable details (China)"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendDueAmountAnalysis_CN","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor due amount analysis report (China)"}],"getName":"InquiriesAndReports","getTitleStr":"Inquiries and reports"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"VendexchRateAdjustment","getHelpTextStr":"","getMenuItemName":"VendExchRateAdjustment","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Foreign currency revaluation"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendLedgerReconciliation","getMenuItemType":"Output","getNavigationPath":"","getTitleStr":"Vendor to ledger reconciliation report"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendOneTimeVendorImport_PSN","getMenuItemType":"Action","getNavigationPath":"","getTitleStr":"Import one-time vendors and invoices"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"VendOneTimeVendorProcess_PSN","getMenuItemType":"Action","getNavigationPath":"","getTitleStr":"Process one-time vendors and invoices"},{"getCrumbPath":"","getFormName":"","getHelpTextStr":"","getMenuItemName":"PrenoteAP","getMenuItemType":"Action","getNavigationPath":"","getTitleStr":"Create prenotes"}],"getName":"PeriodicTasks","getTitleStr":"Periodic tasks"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"VendParameters","getHelpTextStr":"","getMenuItemName":"VendParameters","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Accounts payable parameters"},{"getCrumbPath":"","getFormName":"WorkflowtableListPageRnr","getHelpTextStr":"","getMenuItemName":"WorkflowConfigurationVend","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Accounts payable workflows"},{"getCrumbPath":"","getFormName":"CustVendReportInterval","getHelpTextStr":"","getMenuItemName":"VendReportInterval","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Aging period definitions"},{"getCrumbPath":"","getFormName":"LineOfBusiness","getHelpTextStr":"","getMenuItemName":"LineOfBusiness","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Line of business"},{"getCrumbPath":"","getFormName":"VendPosting","getHelpTextStr":"","getMenuItemName":"VendPosting","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor posting profiles"},{"getCrumbPath":"","getFormName":"Reasons","getHelpTextStr":"","getMenuItemName":"VendReason","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor reasons"},{"getCrumbPath":"","getFormName":"PurchSummaryParameters","getHelpTextStr":"","getMenuItemName":"PurchSummaryParameters","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Summary update parameters"},{"getCrumbPath":"","getFormName":"DeliveryTerms","getHelpTextStr":"","getMenuItemName":"VendDeliveryTerms","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Terms of delivery"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"FormLetterRemarks","getHelpTextStr":"","getMenuItemName":"VendFormLetterRemarks","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Form notes"},{"getCrumbPath":"","getFormName":"VendFormletterParameters","getHelpTextStr":"","getMenuItemName":"VendFormletterParameters","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Form setup"},{"getCrumbPath":"","getFormName":"VendFormLetterSortingParameters","getHelpTextStr":"","getMenuItemName":"VendFormLetterSortingParameters","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Form sorting parameters"}],"getName":"Forms","getTitleStr":"Forms"},{"getCrumbPath":"","getFormName":"GAR_CompanyGroup","getHelpTextStr":"","getMenuItemName":"GAR_CompanyGroup","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Company group"},{"getCrumbPath":"","getFormName":"GAR_ProductCode","getHelpTextStr":"","getMenuItemName":"GAR_ProductCode","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Product code"}],"getName":"Setup","getTitleStr":"Setup"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"SysPolicySourceDocumentRuletype","getHelpTextStr":"","getMenuItemName":"VendInvoicePolicyRuleType","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor invoice policy rule types"},{"getCrumbPath":"","getFormName":"SysPolicyListPage","getHelpTextStr":"","getMenuItemName":"VendInvoicePolicies","getMenuItemType":"Action","getNavigationPath":"","getTitleStr":"Vendor invoice policies"},{"getCrumbPath":"","getFormName":"WorkflowparticipantExpenToken","getHelpTextStr":"","getMenuItemName":"VendInvoiceWorkflowParticipantExpenToken","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor invoice expenditure reviewers"}],"getName":"PolicySetup","getTitleStr":"Policy setup"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"PurchPriceTolerance","getHelpTextStr":"","getMenuItemName":"PurchPriceTolerance","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Price tolerances"},{"getCrumbPath":"","getFormName":"PurchLineMatchingPolicy","getHelpTextStr":"","getMenuItemName":"PurchLineMatchingPolicy","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Matching policy"},{"getCrumbPath":"","getFormName":"VendTotalPriceTolerance","getHelpTextStr":"","getMenuItemName":"VendTotalPriceTolerance","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Invoice totals tolerances"},{"getCrumbPath":"","getFormName":"MarkupTolerance","getHelpTextStr":"","getMenuItemName":"MarkupTolerance_Vend","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Charges tolerances"},{"getCrumbPath":"","getFormName":"InventItemPriceToleranceGroup","getHelpTextStr":"","getMenuItemName":"InventItemPriceToleranceGroup","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Item price tolerance groups"}],"getName":"InvoiceMatchingSetup","getTitleStr":"Invoice matching setup"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"MarkupTable","getHelpTextStr":"","getMenuItemName":"MarkupTable_Vend","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Charges code"},{"getCrumbPath":"","getFormName":"MarkupGroup","getHelpTextStr":"","getMenuItemName":"MarkupGroup_Vend","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Vendor charges group"},{"getCrumbPath":"","getFormName":"MarkupGroup","getHelpTextStr":"","getMenuItemName":"MarkupGroup_Invent","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Item charge groups"},{"getCrumbPath":"","getFormName":"MarkupAutoSetup","getHelpTextStr":"","getMenuItemName":"MarkupAutoSetup_Vend","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Automatic charges"}],"getName":"MiscChargesSetup","getTitleStr":"Charges setup"},{"getCompanyNameStr":"寶嘉創業製衣廠(雲浮)有限公司","getCompanyStr":"P001","GetDataContract":[{"getCrumbPath":"","getFormName":"VendPaymMode","getHelpTextStr":"","getMenuItemName":"VendPaymMode","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Methods of payment"},{"getCrumbPath":"","getFormName":"PaymDay","getHelpTextStr":"","getMenuItemName":"PaymDay","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Payment days"},{"getCrumbPath":"","getFormName":"PaymSched","getHelpTextStr":"","getMenuItemName":"PaymSched","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Payment schedules"},{"getCrumbPath":"","getFormName":"PaymTerm","getHelpTextStr":"","getMenuItemName":"PaymTerm","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Terms of payment"},{"getCrumbPath":"","getFormName":"CashDisc","getHelpTextStr":"","getMenuItemName":"CashDisc","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Cash discounts"},{"getCrumbPath":"","getFormName":"VendPaymFee","getHelpTextStr":"","getMenuItemName":"VendPaymFee","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Payment fee"},{"getCrumbPath":"","getFormName":"vendcoverPageLayout","getHelpTextStr":"","getMenuItemName":"VendCoverPageSetup","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Cover page for payments report"},{"getCrumbPath":"","getFormName":"PaymCalendar","getHelpTextStr":"","getMenuItemName":"PaymCalendar","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Payment calendar"},{"getCrumbPath":"","getFormName":"PaymCalendarRules","getHelpTextStr":"","getMenuItemName":"PaymCalendarRuleVendor","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Payment calendar configuration"},{"getCrumbPath":"","getFormName":"PaymFeeBankRule_JP","getHelpTextStr":"","getMenuItemName":"PaymFeeBankRule_JP","getMenuItemType":"Display","getNavigationPath":"","getTitleStr":"Bank rules for payment fee"}],"getName":"PaymentSetup","getTitleStr":"Payment setup"}],"getName":"AccountsPayable","getTitleStr":"Accounts payable"}
####dct1
dct1={
    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
    "getCompanyStr": "P001",
    "GetDataContract": [
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCountStr": "",
                    "getFormName": "CustomerInvoiceWorkspace",
                    "getHelpTextStr": "",
                    "getImageLocationStr": "Symbol",
                    "getImageStr": "Workspace_CustomerInvoicing",
                    "getKpiNameStr": "",
                    "getMenuItemName": "CustomerInvoiceWorkspace",
                    "getMenuItemType": "Display",
                    "getSizeStr": "Wide",
                    "getTileDisplayStr": "4",
                    "getTileName": "CustomerInvoiceWorkspaceTile",
                    "getTilePath": "MenusAccountsReceivableWorkspacesCustomerinvoicing",
                    "getTileTypeStr": "Standard",
                    "getTitleStr": "Customer invoicing",
                    "getUrlStr": ""
                },
                {
                    "getCountStr": "",
                    "getFormName": "CustPaymentWorkspace",
                    "getHelpTextStr": "",
                    "getImageLocationStr": "Symbol",
                    "getImageStr": "Workspace_VendorPayments",
                    "getKpiNameStr": "",
                    "getMenuItemName": "CustPaymentWorkspace",
                    "getMenuItemType": "Display",
                    "getSizeStr": "Wide",
                    "getTileDisplayStr": "4",
                    "getTileName": "CustPaymentWorkspaceTile",
                    "getTilePath": "MenusAccountsReceivableWorkspacesCustomerpayments",
                    "getTileTypeStr": "Standard",
                    "getTitleStr": "Customer payments",
                    "getUrlStr": ""
                }
            ],
            "getName": "Workspaces",
            "getTitleStr": "Workspaces"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "CustTable",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustTableListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "All customers"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustTable",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustTableHoldListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customers on hold"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustTable",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustTablePastDueListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customers past due"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "MCRCustUnmergeWorkbench",
                    "getHelpTextStr": "",
                    "getMenuItemName": "MCRCustUnmergeWorkbench",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer unmerge"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "Win_SalesOrderReport",
                    "getMenuItemType": "Output",
                    "getNavigationPath": "",
                    "getTitleStr": "Sales Report"
                }
            ],
            "getName": "Customers",
            "getTitleStr": "Customers"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "SalesTableListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "SalesTableListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "All sales orders"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "SalesTableListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "SalesTableListPageShippedNotInvoiced",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Shipped but not invoiced sales orders"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "SalesTableListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "SalesTableListPageFulfilled",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "All fulfilled orders"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "SalesTableListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "SalesTableListPagePartiallyPicked",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "All partially picked orders"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "SalesTable",
                    "getHelpTextStr": "",
                    "getMenuItemName": "SalesTableInterCompany",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Intercompany orders"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "ReturnTableListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "ReturnTableListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "All return orders"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "SalesAgreementListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "SalesAgreementListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Sales agreements"
                }
            ],
            "getName": "Orders",
            "getTitleStr": "Orders"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "CustFreeInvoice",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustFreeInvoiceListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "All free text invoices"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustFreeInvoice",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustFreeInvoiceAssignedToMeListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Free text invoices assigned to me"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustOpenInvoicesListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustOpenInvoicesListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Open customer invoices"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustOpenInvoicesListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustOpenInvoicesDueTodayListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer invoices due today"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustOpenInvoicesListPage",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustOpenInvoicesPastDueListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer invoices past due"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "SalesFormLetter_Invoice",
                            "getMenuItemType": "Action",
                            "getNavigationPath": "",
                            "getTitleStr": "Invoice"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustPostInvoiceJob",
                            "getMenuItemType": "Action",
                            "getNavigationPath": "",
                            "getTitleStr": "Free text invoice"
                        }
                    ],
                    "getName": "BatchInvoicing",
                    "getTitleStr": "Batch invoicing"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "CustRecurrenceInvoiceGroup",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustRecurrenceInvoiceGroup",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Post recurring invoices"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustRecurrenceInvoiceServiceOperation",
                            "getMenuItemType": "Action",
                            "getNavigationPath": "",
                            "getTitleStr": "Generate recurring invoices"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "custinvoicetemplate",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustInvoiceTemplate",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Free text invoice templates"
                        }
                    ],
                    "getName": "RecurringInvoices",
                    "getTitleStr": "Recurring invoices"
                }
            ],
            "getName": "Invoices",
            "getTitleStr": "Invoices"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "LedgerJournalTable",
                    "getHelpTextStr": "",
                    "getMenuItemName": "LedgerJournalTable_CustPaym",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Payment journal"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "LedgerJournalTable",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustPaymentAssignedToMeListPage",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Payment journals assigned to me"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "LedgerJournalTable",
                            "getHelpTextStr": "",
                            "getMenuItemName": "LedgerJournalTable_CustDrawBill",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Draw bill of exchange journal"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "LedgerJournalTable",
                            "getHelpTextStr": "",
                            "getMenuItemName": "LedgerJournalTable_CustProtestBill",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Protest bill of exchange journal"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "LedgerJournalTable",
                            "getHelpTextStr": "",
                            "getMenuItemName": "LedgerJournalTable_CustRedrawBill",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Redraw bill of exchange journal"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "LedgerJournalTable",
                            "getHelpTextStr": "",
                            "getMenuItemName": "LedgerJournalTable_CustPaymRemittance",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Remittance journal"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "LedgerJournalTable",
                            "getHelpTextStr": "",
                            "getMenuItemName": "LedgerJournalTable_CustSettleBill",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Settle bill of exchange journal"
                        }
                    ],
                    "getName": "BillOfExchange",
                    "getTitleStr": "Bill of exchange"
                }
            ],
            "getName": "Payments",
            "getTitleStr": "Payments"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "CustExchRateAdjustment",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustExchRateAdjustment",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Foreign currency revaluation"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustLedgerReconciliationPeriodicTask",
                    "getMenuItemType": "Output",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer to ledger reconciliation"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustAccountStatementExt",
                    "getMenuItemType": "Output",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer account statement"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "TaxIntgrExportDocument_CN",
                    "getHelpTextStr": "",
                    "getMenuItemName": "TaxIntgrExportDocument_CN",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "VAT invoice integration"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "PrenoteAR",
                    "getMenuItemType": "Action",
                    "getNavigationPath": "",
                    "getTitleStr": "Create prenotes"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustOverPaym",
                    "getMenuItemType": "Action",
                    "getNavigationPath": "",
                    "getTitleStr": "Reimbursement"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "RetailSyncOrdersJobScheduler",
                    "getMenuItemType": "Action",
                    "getNavigationPath": "",
                    "getTitleStr": "Synchronize orders"
                }
            ],
            "getName": "PeriodicProcesses",
            "getTitleStr": "Periodic tasks"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "CreditCardAuthTrans",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CreditCardAuthTrans",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Credit card history"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CreditCardIssues",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CreditCardIssues",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Credit card issues"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustFreeInvoice",
                    "getHelpTextStr": "",
                    "getMenuItemName": "MCRGiftCardCustFreeInvoiceDetails",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Gift card invoice"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "SalesPostingHistory",
                    "getHelpTextStr": "",
                    "getMenuItemName": "MCRSalesTaxInquiryHistory",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Sales tax history"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CommissionTrans",
                    "getMenuItemType": "Output",
                    "getNavigationPath": "",
                    "getTitleStr": "Commission transaction list report"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustLedgerTrans",
                    "getMenuItemType": "Output",
                    "getNavigationPath": "",
                    "getTitleStr": "History by transaction report"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustTransOpenPerDate",
                    "getMenuItemType": "Output",
                    "getNavigationPath": "",
                    "getTitleStr": "Open transactions report"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustTransTaxTrans",
                    "getMenuItemType": "Output",
                    "getNavigationPath": "",
                    "getTitleStr": "Sales tax specification report"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustTransList",
                    "getMenuItemType": "Output",
                    "getNavigationPath": "",
                    "getTitleStr": "Transactions report"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "SalesCOD",
                    "getHelpTextStr": "",
                    "getMenuItemName": "SalesCODAction",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "COD outstanding"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "custbalancelist_CN",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustBalanceList_CN",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer balance with multiple view"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustLedgerTransactions_CN",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer details report (China)"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustAccountStatementExt",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer account statement"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustReport_Auditor",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer auditor report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustBasedata",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer base data report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustListReport",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustLedgerReconciliation",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer to ledger reconciliation report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustReimbursement",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Reimbursement report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustRevenue",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer turnover report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustAccountStatementInt",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer account statement (internal)"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustReceivableTransaction_CN",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Receivable details report (China)"
                        }
                    ],
                    "getName": "CustomerRelated",
                    "getTitleStr": "Customers"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "SalesLineBackorder",
                            "getHelpTextStr": "",
                            "getMenuItemName": "SalesLineBackOrder",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Backorder lines"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "LedgerTransListAccountCust",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Ledger posting for sales orders"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "SalesNotInvoiced",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Order lines not invoiced report"
                        }
                    ],
                    "getName": "OrderRelated",
                    "getTitleStr": "Orders"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "SalesPostingHistory",
                            "getHelpTextStr": "",
                            "getMenuItemName": "SalesPostingHistoryInvoice",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Invoice history"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "CustInvoiceJournal",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustInvoiceJournal",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Invoice journal"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "SalesPostingHistory",
                            "getHelpTextStr": "",
                            "getMenuItemName": "MCRSalesTaxInquiryHistory",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Sales tax history"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustInvoiceJourReport",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer invoice journal report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustInvoice",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer invoice transactions report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustInvoiceSpec",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Invoice specification report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustInvoiceVolume",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Invoice turnover report"
                        }
                    ],
                    "getName": "InvoiceRelated",
                    "getTitleStr": "Invoices"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "CustBillOfExchangeJour",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustBillOfExchangeJour",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Bill of exchange journal"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustBillOfExchangeReport",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Bill of exchange journal report"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "CustbillOfExchangestatistics",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustBillOfExchangeStat",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Bill of exchange statistics"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "CustPostDatedChecks",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustPostDatedChecks",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer postdated checks"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "PaymFeeInquiry",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustPaymFeeInquiry",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Payment fee"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustPostPaymJournal",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Customer posted payment journal report"
                        }
                    ],
                    "getName": "PaymentRelated",
                    "getTitleStr": "Payments"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "MCRGiftCardOpen",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Open"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "MCRGiftCardRedeemed",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Redeemed"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "MCRGiftCardIssue",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Issued"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "",
                            "getHelpTextStr": "",
                            "getMenuItemName": "MCRGiftCardVoided",
                            "getMenuItemType": "Output",
                            "getNavigationPath": "",
                            "getTitleStr": "Voided"
                        }
                    ],
                    "getName": "GiftReports",
                    "getTitleStr": "Gift reports"
                }
            ],
            "getName": "InquiriesAndReports",
            "getTitleStr": "Inquiries and reports"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "CustParameters",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustParameters",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Accounts receivable parameters"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "WorkflowtableListPageRnr",
                    "getHelpTextStr": "",
                    "getMenuItemName": "WorkflowConfigurationCust",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Accounts receivable workflows"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustGroup",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustGroup",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer groups"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustPosting",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustPosting",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer posting profiles"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "Reasons",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustReasons",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer reason codes"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "XmlCertificate",
                    "getHelpTextStr": "",
                    "getMenuItemName": "XmlCertificate",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Electronic signature certificates"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "PriceDiscAdmTable",
                    "getHelpTextStr": "",
                    "getMenuItemName": "PriceDiscAdmTable_Sales",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Trade agreement journals"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "AgreementClassification",
                    "getHelpTextStr": "",
                    "getMenuItemName": "SalesAgreementClassification",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Sales agreement classifications"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustBillingClassification",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustBillingClassification",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Billing classifications"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustBillingCode",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustBillingCode",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Billing codes"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustCustomField",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustCustomField",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Billing code custom fields"
                },
                {
                    "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
                    "getCompanyStr": "P001",
                    "GetDataContract": [
                        {
                            "getCrumbPath": "",
                            "getFormName": "FormLetterRemarks",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustFormLetterRemarks",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Form notes"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "CustFormletterParameters",
                            "getHelpTextStr": "",
                            "getMenuItemName": "CustFormletterParameters",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Form setup"
                        },
                        {
                            "getCrumbPath": "",
                            "getFormName": "salesformLetterSortingParameters",
                            "getHelpTextStr": "",
                            "getMenuItemName": "SalesFormLetterSortingParameters",
                            "getMenuItemType": "Display",
                            "getNavigationPath": "",
                            "getTitleStr": "Form sorting"
                        }
                    ],
                    "getName": "Forms",
                    "getTitleStr": "Forms"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "TEX_SalesDocType",
                    "getHelpTextStr": "",
                    "getMenuItemName": "TEX_SalesDocType",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Sales Order Document type"
                }
            ],
            "getName": "Setup",
            "getTitleStr": "Setup"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "MarkupAutoSetup",
                    "getHelpTextStr": "",
                    "getMenuItemName": "MarkupAutoSetup_Cust",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Auto charges"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "MarkupTable",
                    "getHelpTextStr": "",
                    "getMenuItemName": "MarkupTable_Cust",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Charges code"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "MarkupGroup",
                    "getHelpTextStr": "",
                    "getMenuItemName": "MarkupGroup_Cust",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Customer charge groups"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "MarkupGroup",
                    "getHelpTextStr": "",
                    "getMenuItemName": "MarkupGroup_Delivery",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Delivery charges groups"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "MarkupGroup",
                    "getHelpTextStr": "",
                    "getMenuItemName": "MarkupGroup_Invent",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Item charge groups"
                }
            ],
            "getName": "MiscellaneousCharge",
            "getTitleStr": "Charges setup"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "CustPaymMode",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustPaymMode",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Methods of payment"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "PaymDay",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustPaymDay",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Payment days"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "PaymSched",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustPaymSched",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Payment schedules"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "PaymTerm",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustPaymTerm",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Terms of payment"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CashDisc",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustCashDisc",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Cash discounts"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CustPaymFee",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CustPaymFee",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Payment fee"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "CreditCardProcessors",
                    "getHelpTextStr": "",
                    "getMenuItemName": "CreditCardProcessors",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Payment services"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "PaymCalendar",
                    "getHelpTextStr": "",
                    "getMenuItemName": "PaymCalendar",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Payment calendar"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "PaymCalendarRules",
                    "getHelpTextStr": "",
                    "getMenuItemName": "PaymCalendarRuleCustomer",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Payment calendar configuration"
                }
            ],
            "getName": "PaymentsSetup",
            "getTitleStr": "Payments setup"
        },
        {
            "getCompanyNameStr": "寶嘉創業製衣廠(雲浮)有限公司",
            "getCompanyStr": "P001",
            "GetDataContract": [
                {
                    "getCrumbPath": "",
                    "getFormName": "TaxProfileTable_CN",
                    "getHelpTextStr": "",
                    "getMenuItemName": "TaxProfileTable_CN",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "Tax integration profiles"
                },
                {
                    "getCrumbPath": "",
                    "getFormName": "VATInvoiceDescTable_CN",
                    "getHelpTextStr": "",
                    "getMenuItemName": "VATInvoiceDescTable_CN",
                    "getMenuItemType": "Display",
                    "getNavigationPath": "",
                    "getTitleStr": "VAT invoice description"
                }
            ],
            "getName": "TaxIntegration",
            "getTitleStr": "Tax integration"
        }
    ],
    "getName": "AccountsReceivable",
    "getTitleStr": "Accounts receivable"
}



# 执行函数
get_data(dct2)
write_into_xlsx(res)
