import pandas as pd
from lxml import etree
import logging
import os

os.chdir('C://Users//guptaran//Desktop//Python')

log_format = '%(asctime)s : %(message)s'
logging.basicConfig(filename="test.log", level=logging.DEBUG, format=log_format)
logging.debug("Reading Record of Csv file successfully done")
data_file = pd.read_csv("sample_input.csv", usecols=[0, 1, 2])
result = []


def unique_record_of_auditSubscriber():
    logging.debug("Searching Unique Record of AuditSubscriber Successfully done")
    unique_words = data_file['MSISDN'].unique()
    for row in data_file.values:
        for unique_field in unique_words:
            if unique_field in row:
                result.append(row.tolist())

    for i in result:
        print i


def create_xml_for_single_auditSubscriber():
    logging.debug("Single Record Xml File Created for AuditSubscriber Successfully done" )
    xsi = "http://www.w3.org/2001/XMLSchema-instance"
    schemaLocation = "schema.xsd"
    root_config = etree.Element("Audit",
                                attrib={"{" + xsi + "}noNamespaceSchemaLocation": schemaLocation},
                                nsmap={'noNamespaceSchemaLocation': schemaLocation, 'xsi': xsi
                                       })
    root_config = etree.SubElement(root_config, "Audit")
    auditSubscribers = etree.SubElement(root_config, "auditSubscribers")
    MSISDN = etree.SubElement(auditSubscribers, "MSISDN")
    MSISDN.text = str(data_file['MSISDN'][0])
    OperationType = etree.SubElement(auditSubscribers, "OperationType")
    OperationType.text = str(data_file['OperationType'][1])
    ServiceIndication = etree.SubElement(auditSubscribers, "ServiceIndication")
    ServiceIndication.text = str(data_file['ServiceIndication'][2])
    tree = etree.ElementTree(root_config)
    tree.write("singleAuditSubscriber.xml", encoding='utf-8', xml_declaration=True, pretty_print=True)


def create_xml_for_mutiple_auditSubscriber():
    logging.debug("Mutiple Record Xml File Created for AuditSubscriber- Successfully done")
    xsi = "http://www.w3.org/2001/XMLSchema-instance"
    schemaLocation = "schema.xsd"
    root_config = etree.Element("Audit",
                                attrib={"{" + xsi + "}noNamespaceSchemaLocation": schemaLocation},
                                nsmap={'noNamespaceSchemaLocation': schemaLocation, 'xsi': xsi
                                       })
    root_config = etree.SubElement(root_config, "Audit")
    for user in range(len(result)):
        auditSubscribers = etree.SubElement(root_config, "auditSubscribers")
        MSISDN = etree.SubElement(auditSubscribers, "MSISDN")
        MSISDN.text = str(result[user][0])
        OperationType = etree.SubElement(auditSubscribers, "OperationType")
        OperationType.text = str(result[user][1])
        ServiceIndication = etree.SubElement(auditSubscribers, "ServiceIndication")
        ServiceIndication.text = str(result[user][2])
        tree = etree.ElementTree(root_config)
        tree.write("multipleAuditSubscriber.xml", encoding='utf-8', xml_declaration=True, pretty_print=True)


def configuration_service_indication():
    logging.debug("configuration file filter on basis of user Service Indication Successfully done")
    input_string = raw_input("Enter service indication to filter")
    data_file1 = pd.read_csv("sample_input.csv")
    result1 = []
    for row1 in data_file1.values:
        if input_string in row1:
            result1.append(row1.tolist())

    for i in result1:
        print i


if __name__ == "__main__":
    unique_record_of_auditSubscriber()
    create_xml_for_single_auditSubscriber()
    create_xml_for_mutiple_auditSubscriber()
    configuration_service_indication()
