import { useState } from "react";
import * as S from "./styles";
import { Summary, Arrow } from "./styles"; // Ensure the correct path

const PersonDetails = ({ person }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  // Safely access user_data and other fields
  const userData = person.user_data || person;
  const applicationDates = person.application_dates || [];
  const instructionGroups = person.instruction_groups || [];
  const notices = person.notices || [];

  return (
    <S.PersonDetails>
      <Summary>
        <div className="info">
          <div className="info-item">{userData.username || "N/A"}</div>
          <div className="info-item">{userData.idnp || "N/A"}</div>
          <div className="info-item">{userData.phone_number || "N/A"}</div>
          <div className="info-item">{userData.email || "N/A"}</div>
        </div>
        <Arrow onClick={toggleExpand}>
          {isExpanded ? "▲" : "▼"}
        </Arrow>
      </Summary>
      {isExpanded && (
        <div className="detailsStyle">
          <div><b>Data aplicării:</b> {applicationDates.join(", ")}</div>
          <div><b>Data nașterii: </b>{userData.bday || "N/A"}</div>
          <div><b>Vârsta:</b> {userData.age || "N/A"}</div>
          <div><b>Localitate:</b> {userData.location || "N/A"}</div>
          <div><b>Programul la care aplică:</b> {userData.program || "N/A"}</div>
          <div><b>Persoana la care a apelat:</b> {userData.operator || "N/A"}</div>
          <div>
            <b>Data confirmării recepționării formularului:</b>{" "}
            {userData.confirmation_date || "N/A"}
          </div>
          <div><b>Comentariu în urma discuției:</b> {userData.comment || "N/A"}</div>
          <div><b>Statut în urma dicuției:</b> {userData.status || "N/A"}</div>
          <div>
            <b>Grupa de instruire în care a fost invitat:</b>{" "}
            {instructionGroups.join(", ") || "N/A"}
          </div>
          <div><b>Certificat obținut: </b>{userData.certificate || "N/A"}</div>
          <div><b>Aplicat la finanțare:</b> {userData.finance || "N/A"}</div>
          <div>
            <b>Statut în urma evaluării planului de afaceri:</b>{" "}
            {userData.final_status || "N/A"}
          </div>
          <div><b>Excluderea din baza de date: </b>{userData.exclusion || "N/A"}</div>
          <div className="phoneStyle">
          <b>Informarea prin poștei electronice:</b>
            {notices.length > 0 ? (
              <table className="noticeTable">
                <thead>
                  <tr>
                    <th>Notice</th>
                    <th>Phone Calls</th>
                    <th>Email Calls</th>
                    <th>SMS Calls</th>
                    <th>Viber Calls</th>
                    <th>Response</th>
                  </tr>
                </thead>
                <tbody>
                  {notices.map((notice, index) => (
                    <tr key={index}>
                      <td>{index + 1}</td>
                      <td>{notice[0] || "N/A"}</td>
                      <td>{notice[1] || "N/A"}</td>
                      <td>{notice[2] || "N/A"}</td>
                      <td>{notice[3] || "N/A"}</td>
                      <td>{notice[4] || "N/A"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              "N/A"
            )}
          </div>
        </div>
      )}
    </S.PersonDetails>
  );
};

export default PersonDetails;
