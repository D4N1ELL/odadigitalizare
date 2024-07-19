import * as XLSX from "xlsx";
import { saveAs } from "file-saver";

const ExcelExportButton = ({ data }) => {
  const exportToExcel = () => {
    const wb = XLSX.utils.book_new();

    data.forEach((person, index) => {
      const ws = XLSX.utils.json_to_sheet([formatPersonDetails(person)]);
      XLSX.utils.book_append_sheet(wb, ws, `PersonDetails${index + 1}`);
    });

    const wbout = XLSX.write(wb, { bookType: "xlsx", type: "array" });

    const blob = new Blob([wbout], { type: "application/octet-stream" });

    saveAs(blob, "PersonDetails.xlsx");
  };

  const formatPersonDetails = (person) => {
    return {
      Username: person.username,
      Surname: person.surname,
      "Application Date": person.application_date.join(", "),
      IDNP: person.idnp,
      "Birth Date": person.bday,
      Age: person.age,
      Location: person.location,
      "Phone Number": person.phone_number,
      Email: person.email,
      Program: person.program,
      Operator: person.operator,
      "Confirmation Date": person.confirmation_date,
      Comment: person.comment,
      Status: person.statut,
      "Instruction Participation": person.instruction_participation.join(", "),
      Certificate: person.certificate,
      Finance: person.finance,
      "Final Status": person.final_statut,
      Exclusion: person.exclusion,
      "Phone Calls": person.notice.phone_call.join(", "),
      "Email Calls": person.notice.email_call.join(", "),
      "SMS Calls": person.notice.sms_call.join(", "),
      "Viber Calls": person.notice.viber_call.join(", "),
      Response: person.notice.response.join(", "),
    };
  };

  return (
    <div style={buttonContainerStyle}>
      <button onClick={exportToExcel} style={buttonStyle}>
        Export to Excel
      </button>
    </div>
  );
};

const buttonContainerStyle = {
  backgroundColor: "#213b8b",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  height: "42vh",
};

const buttonStyle = {
  padding: "10px 20px",
  borderRadius: "25px",
  border: "1px solid #0073e6",
  backgroundColor: "#0073e6",
  color: "#fff",
  fontSize: "16px",
  fontWeight: "bold",
  cursor: "pointer",
  transition: "background-color 0.3s, box-shadow 0.3s",
};

export default ExcelExportButton;
