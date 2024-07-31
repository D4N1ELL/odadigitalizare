import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import React, { useEffect } from 'react';

const ExcelExportButton = ({ data }) => {
  useEffect(() => {
    console.log("Data passed to ExcelExportButton:", data);
  }, [data]);

  const exportToExcel = () => {
    const wb = XLSX.utils.book_new();
    const wsData = [];

    // Define the static headers
    const staticHeaders = [
      "Nume Prenume", "IDNP", "Data nașterii", "Vârsta", "Localitate", "Telefon",
      "E-mail", "Programul la care aplică", "Persoana care a apelat", "Data confirmării recepționării formularului / Data apelului", "Comentariu în urma discuției",
      "Statut în urma discuției", "Participare la instruire", "Certificat obținut", "Aplicat la finanțare", "Statut în urma evaluării planului de afaceri", "Excluderea din baza de date"
    ];

    let maxApplicationDates = 0;
    let maxNotices = 0;
    data.forEach(person => {
      if (person.application_dates.length > maxApplicationDates) {
        maxApplicationDates = person.application_dates.length;
      }
      if (person.notices.length > maxNotices) {
        maxNotices = person.notices.length;
      }
    });

    const dynamicHeaders = [];
    for (let i = 0; i < maxApplicationDates; i++) {
      dynamicHeaders.push(`Data aplicării ${i + 1}`);
    }
    for (let i = 0; i < maxNotices; i++) {
      dynamicHeaders.push(`Inștiințare TELEFON ${i + 1}`);
      dynamicHeaders.push(`Inștiințare E-MAIL ${i + 1}`);
      dynamicHeaders.push(`Inștiințare SMS ${i + 1}`);
      dynamicHeaders.push(`Inștiințare VIBER ${i + 1}`);
      dynamicHeaders.push(`Inștiințare Răspuns ${i + 1}`);
    }

    const headers = [...staticHeaders, ...dynamicHeaders];
    wsData.push(headers);

    data.forEach((person) => {
      const row = [
        person.user_data.username || 'N/A',
        person.user_data.idnp || 'N/A',
        person.user_data.bday || 'N/A',
        person.user_data.age || 'N/A',
        person.user_data.loc_name || 'N/A',
        person.user_data.phone_number || 'N/A',
        person.user_data.email || 'N/A',
        person.user_data.program_name || 'N/A',
        person.user_data.operator || 'N/A',
        person.user_data.confirmation_date || 'N/A',
        person.user_data.comment || 'N/A',
        person.user_data.status || 'N/A',
        person.instruction_groups.join(", ") || 'N/A',
        person.user_data.certificate || 'N/A',
        person.user_data.finance || 'N/A',
        person.user_data.final_status || 'N/A',
        person.user_data.exclusion ? 'Exclus' : 'N/A'
      ];

      for (let i = 0; i < maxApplicationDates; i++) {
        row.push(person.application_dates[i] || 'N/A');
      }

      for (let i = 0; i < maxNotices; i++) {
        row.push(person.notices[i] ? person.notices[i][0] || 'N/A' : 'N/A');
        row.push(person.notices[i] ? person.notices[i][1] || 'N/A' : 'N/A');
        row.push(person.notices[i] ? person.notices[i][2] || 'N/A' : 'N/A');
        row.push(person.notices[i] ? person.notices[i][3] || 'N/A' : 'N/A');
        row.push(person.notices[i] ? person.notices[i][4] || 'N/A' : 'N/A');
      }

      wsData.push(row);
    });

    // Debugging: Log the wsData array to ensure it has the correct data
    console.log(wsData);

    // Create worksheet
    const ws = XLSX.utils.aoa_to_sheet(wsData);

    const columnWidths = headers.map(header => ({ wch: header.length + 5 }));
    ws["!cols"] = columnWidths;

    XLSX.utils.book_append_sheet(wb, ws, 'PersonDetails');

    const wbout = XLSX.write(wb, { bookType: "xlsx", type: "array" });
    const blob = new Blob([wbout], { type: "application/octet-stream" });

    saveAs(blob, "PersonDetails.xlsx");
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
