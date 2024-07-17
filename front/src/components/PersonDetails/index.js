import { useState } from "react";
import * as S from "./styles";
import { Summary, Arrow } from "./styles"; // Ensure the correct path

const PersonDetails = ({ person }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <S.PersonDetails>
     <Summary>
        <div className="info">
          <div className="info-item">{person.user_data.username}</div>
          <div className="info-item">{person.user_data.surname}</div>
          <div className="info-item">{person.user_data.idnp}</div>
          <div className="info-item">{person.user_data.phone_number}</div>
          <div className="info-item">{person.user_data.email}</div>
        </div>
        <Arrow onClick={toggleExpand}>
          {isExpanded ? "▲" : "▼"}
        </Arrow>
      </Summary>
      {isExpanded && (
        <div className="detailsStyle">
          <div><b>Data aplicării:</b> {person.application_dates.join(", ")}</div>
          <div><b>Data nașterii: </b>{person.user_data.bday}</div>
          <div><b>Vârsta:</b> {person.user_data.age}</div>
          <div><b>Localitate:</b> {person.user_data.location}</div>
          <div><b>Programul la care aplică:</b> {person.user_data.program}</div>
          <div><b>Persoana la care a apelat:</b> {person.user_data.operator}</div>
          <div>
            <b>Data confirmării recepționării formularului:</b>{" "}
            {person.user_data.confirmation_date}
          </div>
          <div><b>Comentariu în urma discuției:</b> {person.user_data.comment}</div>
          <div><b>Statut în urma dicuției:</b> {person.user_data.status}</div>
          <div>
            <b>Grupa de instruire în care a fost invitat:</b>{" "}
            {person.instruction_groups.join(", ")}
          </div>
          <div><b>Certificat obținut: </b>{person.user_data.certificate}</div>
          <div><b>Aplicat la finanțare:</b> {person.user_data.finance}</div>
          <div>
            <b>Statut în urma evaluării planului de afaceri:</b>{" "}
            {person.user_data.final_status || "N/A"}
          </div>
          <div><b>Excluderea din baza de date: </b>{person.user_data.exclusion || "N/A"}</div>
          <div className="phoneStyle">
          <b>Informarea prin poștei electronice:</b>
            {person.notices ? (
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
                  {person.notices.map((notice, index) => (
                    <tr key={index}>
                      <td>{index + 1}</td>
                      <td>{notice[0] || "N/A"}</td>
                      <td>{notice[1] || "N/A"}</td>
                      <td>{notice[2] || "N/A"}</td>
                      <td>{notice[3] || "N/A"}</td>
                      <td>{notice[4]}</td>
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
