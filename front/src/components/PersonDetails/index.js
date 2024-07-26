import React, { useState } from 'react';
import { StyledPersonDetails, ButtonContainer, Summary, Arrow, Input } from './styles';
import axios from "axios";

const PersonDetails = ({ person = {} }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editedPerson, setEditedPerson] = useState({ ...person });

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const toggleEdit = () => {
    if (!isEditing) {
      setEditedPerson({ ...person });
    }
    setIsEditing(!isEditing);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setEditedPerson({
      ...editedPerson,
      [name]: value,
    });
  };

  const handleSave = async () => {
    try {
      // Send the updated data to the backend
      const response = await axios.post('http://127.0.0.1:5000/update', editedPerson);

      if (response.data.success) {
        // Update the state with the new data
        setIsEditing(false);
      } else {
        console.error('Error saving changes');
      }
    } catch (error) {
      console.error('Error saving changes:', error);
    }
  };

  // Safely access user_data and other fields
  const userData = editedPerson.user_data || {};
  const applicationDates = editedPerson.application_dates || [];
  const instructionGroups = editedPerson.instruction_groups || [];
  const notices = editedPerson.notices || [];

  return (
    <StyledPersonDetails>
      <Summary className="summaryStyle">
        <div className="info">
          <div className="info-item">{userData.username || 'N/A'}</div>
          <div className="info-item">{userData.idnp || 'N/A'}</div>
          <div className="info-item">{userData.phone_number || 'N/A'}</div>
          <div className="info-item">{userData.email || 'N/A'}</div>
        </div>
        <Arrow className="arrowStyle" onClick={toggleExpand}>
          {isExpanded ? '▲' : '▼'}
        </Arrow>
      </Summary>
      {isExpanded && (
        <div className="detailsStyle">
          <div><b>Data aplicării:</b> {isEditing ? <Input type="text" name="application_dates" value={applicationDates.join(", ")} onChange={handleChange} /> : applicationDates.join(", ")}</div>
          <div><b>Data nașterii: </b>{isEditing ? <Input type="date" name="bday" value={userData.bday || ''} onChange={handleChange} /> : userData.bday || 'N/A'}</div>
          <div><b>Vârsta:</b> {isEditing ? <Input type="text" name="age" value={userData.age || ''} onChange={handleChange} /> : userData.age || 'N/A'}</div>
          <div><b>Localitate:</b> {isEditing ? <Input type="text" name="location" value={userData.location || ''} onChange={handleChange} /> : userData.location || 'N/A'}</div>
          <div><b>Programul la care aplică:</b> {isEditing ? <Input type="text" name="program" value={userData.program || ''} onChange={handleChange} /> : userData.program || 'N/A'}</div>
          <div><b>Persoana la care a apelat:</b> {isEditing ? <Input type="text" name="operator" value={userData.operator || ''} onChange={handleChange} /> : userData.operator || 'N/A'}</div>
          <div><b>Data confirmării recepționării formularului:</b> {isEditing ? <Input type="date" name="confirmation_date" value={userData.confirmation_date || ''} onChange={handleChange} /> : userData.confirmation_date || 'N/A'}</div>
          <div><b>Comentariu în urma discuției:</b> {isEditing ? <Input type="text" name="comment" value={userData.comment || ''} onChange={handleChange} /> : userData.comment || 'N/A'}</div>
          <div><b>Statut în urma discuției:</b> {isEditing ? <Input type="text" name="status" value={userData.status || ''} onChange={handleChange} /> : userData.status || 'N/A'}</div>
          <div><b>Grupa de instruire în care a fost invitat:</b> {isEditing ? <Input type="text" name="instruction_groups" value={instructionGroups.join(", ")} onChange={handleChange} /> : instructionGroups.join(", ")}</div>
          <div><b>Certificat obținut: </b>{isEditing ? <Input type="text" name="certificate" value={userData.certificate || ''} onChange={handleChange} /> : userData.certificate || 'N/A'}</div>
          <div><b>Aplicat la finanțare:</b> {isEditing ? <Input type="text" name="finance" value={userData.finance || ''} onChange={handleChange} /> : userData.finance || 'N/A'}</div>
          <div><b>Statut în urma evaluării planului de afaceri:</b> {isEditing ? <Input type="text" name="final_status" value={userData.final_status || ''} onChange={handleChange} /> : userData.final_status || 'N/A'}</div>
          <div><b>Excluderea din baza de date: </b>{isEditing ? <Input type="text" name="exclusion" value={userData.exclusion || ''} onChange={handleChange} /> : (userData.exclusion === 1 ? 'Excludat' : 'N/A')}</div>
          <div className="phoneStyle">
            <b>Informarea prin poșta electronice:</b>
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
                      <td>{isEditing ? <Input type="text" name={`notice_${index}_phone_call`} value={editedPerson.notices?.[index]?.[0] || ''} onChange={handleChange} /> : notice[0] || 'N/A'}</td>
                      <td>{isEditing ? <Input type="text" name={`notice_${index}_email_call`} value={editedPerson.notices?.[index]?.[1] || ''} onChange={handleChange} /> : notice[1] || 'N/A'}</td>
                      <td>{isEditing ? <Input type="text" name={`notice_${index}_sms_call`} value={editedPerson.notices?.[index]?.[2] || ''} onChange={handleChange} /> : notice[2] || 'N/A'}</td>
                      <td>{isEditing ? <Input type="text" name={`notice_${index}_viber_call`} value={editedPerson.notices?.[index]?.[3] || ''} onChange={handleChange} /> : notice[3] || 'N/A'}</td>
                      <td>{isEditing ? <Input type="text" name={`notice_${index}_response`} value={editedPerson.notices?.[index]?.[4] || ''} onChange={handleChange} /> : notice[4] || 'N/A'}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              'N/A'
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
              <button onClick={handleSave}>Save</button>
            </>
          )}
        </ButtonContainer>
      )}
    </StyledPersonDetails>
  );
};

export default PersonDetails;
