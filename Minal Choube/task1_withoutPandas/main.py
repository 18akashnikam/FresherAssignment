import csv
from xml.dom import minidom

list1 = []
list_subscribers = []
with open('sample_csv.csv', mode='r')as file:
    csv = csv.reader(file)
    for lines in csv:
        list1.append(lines)


def unique():
    for i in list1:
        mob_no = i[0]
        flag = True
        for j in list_subscribers:
            flag = True
            if j[0] == i[0]:
                flag = False
                break
        if flag:
            list_subscribers.append(i[:3])

    for i in list_subscribers:
        print (i)


def single_audit():
    root = minidom.Document()

    xml = root.createElement('Audit')
    xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    xml.setAttribute('xsi:noNamespaceSchemaLocation', 'schema.xsd')
    root.appendChild(xml)
    audit_subscriber = root.createElement('auditSubscribers')
    xml.appendChild(audit_subscriber)
    msisdn = root.createElement('MSIDN')
    msisdn.appendChild(root.createTextNode(str(list_subscribers[0][0])))
    audit_subscriber.appendChild(msisdn)
    operation_type = root.createElement('OperationType')
    operation_type.appendChild(root.createTextNode(str(list_subscribers[0][1])))
    audit_subscriber.appendChild(operation_type)
    service_indication = root.createElement('ServiceIndication')
    service_indication.appendChild(root.createTextNode(str(list_subscribers[0][2])))
    audit_subscriber.appendChild(service_indication)

    xml_str = root.toprettyxml(indent="\t")
    save_path_file = "SingleAuditSubscriber.xml"
    with open(save_path_file, "w") as f:
        f.write(xml_str)


def multiple_audit():
    root = minidom.Document()

    xml = root.createElement('Audit')
    xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    xml.setAttribute('xsi:noNamespaceSchemaLocation', 'schema.xsd')
    root.appendChild(xml)

    for i in list_subscribers:
        audit_subsciber = root.createElement('auditSubscribers')
        xml.appendChild(audit_subsciber)
        msisdn = root.createElement('MSIDN')
        msisdn.appendChild(root.createTextNode(str(i[0])))
        audit_subsciber.appendChild(msisdn)
        operation_type = root.createElement('OperationType')
        operation_type.appendChild(root.createTextNode(str(i[1])))
        audit_subsciber.appendChild(operation_type)
        service_indication = root.createElement('ServiceIndication')
        service_indication.appendChild(root.createTextNode(str(i[2])))
        audit_subsciber.appendChild(service_indication)

    xml_str = root.toprettyxml(indent="\t")
    save_path_file = "MultipleAuditSubscribers.xml"
    with open(save_path_file, "w") as f:
        f.write(xml_str)


unique()

single_audit()

multiple_audit()
