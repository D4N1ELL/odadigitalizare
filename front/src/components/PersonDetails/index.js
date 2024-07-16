import { useState } from "react";
import { person } from "./exemplu";
import * as S from "./styles";

const PersonDetails = () => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <S.PersonDetails>
      <div className="summaryStyle">
        <div>{person.username}</div>
        <div>{person.surname}</div>
        <div>{person.idnp}</div>
        <div>{person.phone_number}</div>
        <div>{person.email}</div>
        <div className="arrowStyle" onClick={toggleExpand}>
          {isExpanded ? "▲" : "▼"}
        </div>
      </div>
      {isExpanded && (
        <div className="detailsStyle">
          <div><b>Data aplicării:</b> {person.application_date.join(", ")}</div>
          <div><b>Data nașterii: </b>{person.bday}</div>
          <div><b>Vârsta:</b> {person.age}</div>
          <div><b>Localitate:</b> {person.location}</div>
          <div><b>Programul la care aplică:</b> {person.program}</div>
          <div><b>Persoana la care a apelat:</b> {person.operator}</div>
          <div>
            <b>Data confirmării recepționării formularului:</b>{" "}
            {person.confirmation_date}
          </div>
          <div><b>Comentariu în urma discuției:</b> {person.comment}</div>
          <div><b>Statut în urma dicuției:</b> {person.statut}</div>
          <div>
            <b>Grupa de instruire în care a fost invitat:</b>{" "}
            {person.instruction_participation.join(", ")}
          </div>
          <div><b>Certificat obținut: </b>{person.certificate}</div>
          <div><b>Aplicat la finanțare:</b> {person.finance}</div>
          <div>
            <b>Statut în urma evaluării planului de afaceri:</b>{" "}
            {person.final_statut || "N/A"}
          </div>
          <div><b>Excluderea din baza de date: </b>{person.exclusion || "N/A"}</div>
          <div className="phoneStyle">
          <b>Informarea prin poștei electronice:</b>
            {person.notice ? (
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
                  {person.notice.phone_call.map((date, index) => (
                    <tr key={index}>
                      <td>{index + 1}</td>
                      <td>{date || "N/A"}</td>
                      <td>{person.notice.email_call[index] || "N/A"}</td>
                      <td>{person.notice.sms_call[index] || "N/A"}</td>
                      <td>{person.notice.viber_call[index] || "N/A"}</td>
                      <td>{person.notice.response[index] || "N/A"}</td>
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
