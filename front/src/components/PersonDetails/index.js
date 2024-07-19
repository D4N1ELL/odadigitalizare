import React, { useState } from 'react';
import styled from 'styled-components';
import {StyledPersonDetails, ButtonContainer, Summary, Arrow, Input} from './styles'

const PersonDetails = ({ person }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editedPerson, setEditedPerson] = useState({ ...person });

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const toggleEdit = () => {
    setIsEditing(!isEditing);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setEditedPerson({
      ...editedPerson,
      [name]: value,
    });
  };

  const saveChanges = () => {
    // Add logic to save the changes to the backend or state management
    setIsEditing(false);
  };

  return (
    <StyledPersonDetails>
      <Summary className="summaryStyle">
        <div className="info">
          <div className="info-item">{person.username}</div>
          <div className="info-item">{person.surname}</div>
          <div className="info-item">{person.idnp}</div>
          <div className="info-item">{person.phone_number}</div>
          <div className="info-item">{person.email}</div>
        </div>
        <Arrow className="arrowStyle" onClick={toggleExpand}>
          {isExpanded ? "▲" : "▼"}
        </Arrow>
      </Summary>
      {isExpanded && (
        <div className="detailsStyle">
          <div><b>Data aplicării:</b> {isEditing ? <Input type="text" name="application_date" value={editedPerson.application_date.join(", ")} onChange={handleChange} /> : person.application_date.join(", ")}</div>
          <div><b>Data nașterii: </b>{isEditing ? <Input type="text" name="bday" value={editedPerson.bday} onChange={handleChange} /> : person.bday}</div>
          <div><b>Vârsta:</b> {isEditing ? <Input type="text" name="age" value={editedPerson.age} onChange={handleChange} /> : person.age}</div>
          <div><b>Localitate:</b> {isEditing ? <Input type="text" name="location" value={editedPerson.location} onChange={handleChange} /> : person.location}</div>
          <div><b>Programul la care aplică:</b> {isEditing ? <Input type="text" name="program" value={editedPerson.program} onChange={handleChange} /> : person.program}</div>
          <div><b>Persoana la care a apelat:</b> {isEditing ? <Input type="text" name="operator" value={editedPerson.operator} onChange={handleChange} /> : person.operator}</div>
          <div><b>Data confirmării recepționării formularului:</b> {isEditing ? <Input type="text" name="confirmation_date" value={editedPerson.confirmation_date} onChange={handleChange} /> : person.confirmation_date}</div>
          <div><b>Comentariu în urma discuției:</b> {isEditing ? <Input type="text" name="comment" value={editedPerson.comment} onChange={handleChange} /> : person.comment}</div>
          <div><b>Statut în urma discuției:</b> {isEditing ? <Input type="text" name="statut" value={editedPerson.statut} onChange={handleChange} /> : person.statut}</div>
          <div><b>Grupa de instruire în care a fost invitat:</b> {isEditing ? <Input type="text" name="instruction_participation" value={editedPerson.instruction_participation.join(", ")} onChange={handleChange} /> : person.instruction_participation.join(", ")}</div>
          <div><b>Certificat obținut: </b>{isEditing ? <Input type="text" name="certificate" value={editedPerson.certificate} onChange={handleChange} /> : person.certificate}</div>
          <div><b>Aplicat la finanțare:</b> {isEditing ? <Input type="text" name="finance" value={editedPerson.finance} onChange={handleChange} /> : person.finance}</div>
          <div><b>Statut în urma evaluării planului de afaceri:</b> {isEditing ? <Input type="text" name="final_statut" value={editedPerson.final_statut || "N/A"} onChange={handleChange} /> : person.final_statut || "N/A"}</div>
          <div><b>Excluderea din baza de date: </b>{isEditing ? <Input type="text" name="exclusion" value={editedPerson.exclusion || "N/A"} onChange={handleChange} /> : person.exclusion || "N/A"}</div>
          <div className={`phoneStyle ${isEditing ? 'editing' : ''}`}>
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
                      <td>{isEditing ? <Input type="text" name={`phone_call_${index}`} value={editedPerson.notice.phone_call[index] || "N/A"} onChange={handleChange} /> : date || "N/A"}</td>
                      <td>{isEditing ? <Input type="text" name={`email_call_${index}`} value={editedPerson.notice.email_call[index] || "N/A"} onChange={handleChange} /> : person.notice.email_call[index] || "N/A"}</td>
                      <td>{isEditing ? <Input type="text" name={`sms_call_${index}`} value={editedPerson.notice.sms_call[index] || "N/A"} onChange={handleChange} /> : person.notice.sms_call[index] || "N/A"}</td>
                      <td>{isEditing ? <Input type="text" name={`viber_call_${index}`} value={editedPerson.notice.viber_call[index] || "N/A"} onChange={handleChange} /> : person.notice.viber_call[index] || "N/A"}</td>
                      <td>{isEditing ? <Input type="text" name={`response_${index}`} value={editedPerson.notice.response[index] || "N/A"} onChange={handleChange} /> : person.notice.response[index] || "N/A"}</td>
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
      {isExpanded && (
        <ButtonContainer>
          {!isEditing ? (
            <button onClick={toggleEdit}>Edit</button>
          ) : (
            <>
              <button onClick={toggleEdit}>Cancel</button>
              <button onClick={saveChanges}>Save</button>
            </>
          )}
        </ButtonContainer>
      )}
    </StyledPersonDetails>
  );
};
export default PersonDetails;

