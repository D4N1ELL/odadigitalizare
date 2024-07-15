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
          <div>Data aplicarii: {person.application_date.join(", ")}</div>
          <div>Data nasterii: {person.bday}</div>
          <div>Varsta: {person.age}</div>
          <div>Localitate: {person.location}</div>
          <div>Programul la care aplica: {person.program}</div>
          <div>Persoana la care a apelat: {person.operator}</div>
          <div>
            Data confirmării recepționării formularului:{" "}
            {person.confirmation_date}
          </div>
          <div>Comentariu în urma discuției: {person.comment}</div>
          <div>Statut în urma dicuției: {person.statut}</div>
          <div>
            Grupa de instruire în care a fost invitat:{" "}
            {person.instruction_participation.join(", ")}
          </div>
          <div>Certificat obținut: {person.certificate}</div>
          <div>Aplicat la finanțare: {person.finance}</div>
          <div>
            Statut în urma evaluării planului de afaceri:{" "}
            {person.final_statut || "N/A"}
          </div>
          <div>Excluderea din baza de date: {person.exclusion || "N/A"}</div>
          <div className="phoneStyle">
            Informarea prin poștei electronice:{" "}
            {person.notice ? (
              <>
                <div>Phone Calls: {person.notice.phone_call.join(", ")}</div>
                <div>Email Calls: {person.notice.email_call.join(", ")}</div>
                <div>SMS Calls: {person.notice.sms_call.join(", ")}</div>
                <div>Viber Calls: {person.notice.viber_call.join(", ")}</div>
                <div>Response: {person.notice.response.join(", ")}</div>
              </>
            ) : (
              "N/A"
            )}
          </div>
        </div>
      )}
    </S.PersonDetails>
  );
};



const detailsStyle = {
  marginTop: "10px",
  display: "flex",
  flexDirection: "column",
  gap: "0.8em",
};

export default PersonDetails;
