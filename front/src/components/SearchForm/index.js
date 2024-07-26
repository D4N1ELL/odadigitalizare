import { useState } from "react";
import { location } from "./orase";
import { program } from "./programs";
import { instruction_group } from "./instructionGroups";

const SearchForm = ({ onSubmit }) => {
  const [formValues, setFormValues] = useState({
    name: "",
    surname: "",
    idnp: "",
    email: "",
    phoneNumber: "",
    city: "",
    program: "",
    instructionGroup: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formValues);
    // Reset form values after submission
    setFormValues({
      name: "",
      surname: "",
      idnp: "",
      email: "",
      phoneNumber: "",
      city: "",
      program: "",
      instructionGroup: "",
    });
  };

  return (
    <form onSubmit={handleSubmit} style={formStyle}>
      <div style={inputGroupStyle}>
        <label style={labelStyle}>Prenume</label>
        <input
          type="text"
          name="name"
          value={formValues.name}
          onChange={handleChange}
          style={inputStyle}
          placeholder="Adaugă nume"
        />
      </div>
      <div style={inputGroupStyle}>
        <label style={labelStyle}>Nume</label>
        <input
          type="text"
          name="surname"
          value={formValues.surname}
          onChange={handleChange}
          style={inputStyle}
          placeholder="Adaugă nume de familie"
        />
      </div>
      <div style={inputGroupStyle}>
        <label style={labelStyle}>IDNP</label>
        <input
          type="text"
          name="idnp"
          value={formValues.idnp}
          onChange={handleChange}
          style={inputStyle}
          placeholder="Adaugă IDNP"
        />
      </div>
      <div style={inputGroupStyle}>
        <label style={labelStyle}>Email</label>
        <input
          type="email"
          name="email"
          value={formValues.email}
          onChange={handleChange}
          style={inputStyle}
          placeholder="Adaugă email"
        />
      </div>
      <div style={inputGroupStyle}>
        <label style={labelStyle}>Număr de telefon</label>
        <input
          type="tel"
          name="phoneNumber"
          value={formValues.phoneNumber}
          onChange={handleChange}
          style={inputStyle}
          placeholder="Adaugă număr"
        />
      </div>
      <div style={inputGroupStyle}>
        <label style={labelStyle}>Oraș</label>
        <select
          name="city"
          value={formValues.city}
          onChange={handleChange}
          style={{
            ...inputStyle,
            color: `${formValues.city === "" ? "#757575" : "#212121"}`,
          }}
        >
          <option
            value=""
            style={{ ...optionStyle, color: "#ccc", fontWeight: "300" }}
            disabled
          >
            Alege oraș
          </option>
          {location.map((city, index) => (
            <option key={index} value={city} style={optionStyle}>
              {city}
            </option>
          ))}
        </select>
      </div>
      <div style={inputGroupStyle}>
        <label style={labelStyle}>Tipul de program</label>
        <select
          name="program"
          value={formValues.program}
          onChange={handleChange}
          style={{
            ...inputStyle,
            color: `${formValues.program === "" ? "#757575" : "#212121"}`,
          }}
        >
          <option
            value=""
            style={{ ...optionStyle, color: "#ccc", fontWeight: "300" }}
            disabled
          >
            Alege program
          </option>
          {program.map((program, index) => (
            <option key={index} value={program} style={optionStyle}>
              {program}
            </option>
          ))}
        </select>
      </div>
      <div style={inputGroupStyle}>
        <label style={labelStyle}>Grupa de instruire</label>
        <select
          name="instructionGroup"
          value={formValues.instructionGroup}
          onChange={handleChange}
          style={{
            ...inputStyle,
            color: `${formValues.instructionGroup === "" ? "#757575" : "#212121"}`,
          }}
        >
          <option
            value=""
            style={{ ...optionStyle, color: "#ccc", fontWeight: "300" }}
            disabled
          >
            Alege grupa de instruire
          </option>
          {instruction_group.map((group, index) => (
            <option key={index} value={group} style={optionStyle}>
              {group}
            </option>
          ))}
        </select>
      </div>
      <button type="submit" style={submitButtonStyle}>
        Caută
      </button>
    </form>
  );
};

const formStyle = {
  display: "flex",
  flexDirection: "column",
  gap: "1em",
  padding: "20px",
  borderRadius: "15px",
  border: "1px solid #0073e6",
  backgroundColor: "#f0f4ff",
  boxShadow: "0 4px 8px rgba(0, 0, 0, 0.2)",
  maxWidth: "500px",
};

const inputGroupStyle = {
  display: "flex",
  flexDirection: "column",
  gap: "0.5em",
};

const labelStyle = {
  fontWeight: "bold",
  color: "#0073e6",
};

const inputStyle = {
  padding: "10px",
  borderRadius: "5px",
  border: "1px solid #ccc",
  fontSize: "16px",
};

const optionStyle = {
  fontSize: "16px",
};

const submitButtonStyle = {
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

export default SearchForm;
