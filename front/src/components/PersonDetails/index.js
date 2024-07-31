import React, { useState, useEffect } from 'react';
import { StyledPersonDetails, ButtonContainer, Summary, Arrow, Input } from './styles';
import axios from "axios";

const PersonDetails = ({ person = {} }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editedPerson, setEditedPerson] = useState({ ...person });

  useEffect(() => {
    setEditedPerson({ ...person });
  }, [person]);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const toggleEdit = () => {
    setIsEditing(!isEditing);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    const [field, index, subfield] = name.split('_');
    if (field === 'notices') {
      const updatedNotices = [...editedPerson.notices];
      updatedNotices[index][subfield] = value;
      setEditedPerson({
        ...editedPerson,
        notices: updatedNotices
      });
    } else if (field === 'application_dates') {
      const updatedDates = [...editedPerson.application_dates];
      updatedDates[index] = value;
      setEditedPerson({
        ...editedPerson,
        application_dates: updatedDates
      });
    } else {
      setEditedPerson({
        ...editedPerson,
        user_data: {
          ...editedPerson.user_data,
          [name]: value
        }
      });
    }
  };

  const addApplicationDate = () => {
    setEditedPerson({
      ...editedPerson,
      application_dates: [...editedPerson.application_dates, ""]
    });
  };

  const handleSave = async () => {
    try {
      const dataToSend = {
        ...editedPerson,
        user_data: {
          ...editedPerson.user_data,
          age: parseInt(editedPerson.user_data.age, 10)
        }
      };

      const response = await axios.post('http://127.0.0.1:5000/update', dataToSend);

      if (response.data.success) {
        setIsEditing(false);
      } else {
        console.error('Error saving changes');
      }
    } catch (error) {
      console.error('Error saving changes:', error);
    }
  };

  const formatDate = (date) => {
    if (!date) return '';
    const parts = date.split('/');
    if (parts.length === 3) {
      return `${parts[2]}-${parts[1]}-${parts[0]}`;
    }
    return date;
  };

  const userData = editedPerson.user_data || editedPerson;
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
          <div><b>Data aplicării:</b> {isEditing ? (
            <div>
              {applicationDates.map((date, index) => (
                <Input
                  key={index}
                  type="date"
                  name={`application_dates_${index}`}
                  value={date}
                  onChange={handleChange}
                />
              ))}
              <button onClick={addApplicationDate}>Add Date</button>
            </div>
          ) : (
            applicationDates.join(", ") || 'N/A'
          )}</div>
          <div><b>Data nașterii: </b>{isEditing ? <Input type="date" name="bday" value={formatDate(userData.bday)} onChange={handleChange} /> : formatDate(userData.bday)}</div>
          <div><b>Vârsta:</b> {isEditing ? <Input type="number" name="age" value={userData.age || ''} onChange={handleChange} /> : userData.age || 'N/A'}</div>
          <div><b>Localitate:</b> {isEditing ? <Input type="text" name="loc_name" value={userData.loc_name || ''} onChange={handleChange} /> : userData.loc_name || 'N/A'}</div>
          <div><b>Programul la care aplică:</b> {isEditing ? <Input type="text" name="program_name" value={userData.program_name || ''} onChange={handleChange} /> : userData.program_name || 'N/A'}</div>
          <div><b>Persoana la care a apelat:</b> {isEditing ? <Input type="text" name="operator" value={userData.operator || ''} onChange={handleChange} /> : userData.operator || 'N/A'}</div>
          <div><b>Data confirmării recepționării formularului:</b> {isEditing ? <Input type="date" name="confirmation_date" value={formatDate(userData.confirmation_date)} onChange={handleChange} /> : formatDate(userData.confirmation_date)}</div>
          <div><b>Comentariu în urma discuției:</b> {isEditing ? <Input type="text" name="comment" value={userData.comment || ''} onChange={handleChange} /> : userData.comment || 'N/A'}</div>
          <div><b>Statut în urma discuției:</b> {isEditing ? <Input type="text" name="status" value={userData.status || ''} onChange={handleChange} /> : userData.status || 'N/A'}</div>
          <div><b>Grupa de instruire în care a fost invitat:</b> {isEditing ? <Input type="text" name="instruction_groups" value={instructionGroups.join(", ")} onChange={handleChange} /> : instructionGroups.join(", ") || 'N/A'}</div>
          <div><b>Certificat obținut: </b>{isEditing ? <Input type="text" name="certificate" value={userData.certificate || ''} onChange={handleChange} /> : userData.certificate || 'N/A'}</div>
          <div><b>Aplicat la finanțare:</b> {isEditing ? <Input type="text" name="finance" value={userData.finance || ''} onChange={handleChange} /> : userData.finance || 'N/A'}</div>
          <div><b>Statut în urma evaluării planului de afaceri:</b> {isEditing ? <Input type="text" name="final_status" value={userData.final_status || ''} onChange={handleChange} /> : userData.final_status || 'N/A'}</div>
          <div><b>Excluderea din baza de date: </b>{isEditing ? <Input type="text" name="exclusion" value={userData.exclusion || ''} onChange={handleChange} /> : (userData.exclusion === 1 ? 'Exclus' : 'N/A')}</div>
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
                      <td>{isEditing ? <Input type="date" name={`notices_${index}_0`} value={formatDate(notice[0])} onChange={handleChange} /> : notice[0] || 'N/A'}</td>
                      <td>{isEditing ? <Input type="date" name={`notices_${index}_1`} value={formatDate(notice[1])} onChange={handleChange} /> : notice[1] || 'N/A'}</td>
                      <td>{isEditing ? <Input type="date" name={`notices_${index}_2`} value={formatDate(notice[2])} onChange={handleChange} /> : notice[2] || 'N/A'}</td>
                      <td>{isEditing ? <Input type="date" name={`notices_${index}_3`} value={formatDate(notice[3])} onChange={handleChange} /> : notice[3] || 'N/A'}</td>
                      <td>{isEditing ? <Input type="text" name={`notices_${index}_4`} value={notice[4] || ''} onChange={handleChange} /> : notice[4] || 'N/A'}</td>
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
