import styled from "styled-components";

export const Header = styled.div`
  max-height: 85px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 16px 80px;
  color: white;
  border-bottom: 1px solid #A9A9AC;
  .logo {
    width: 20%;
  }
  input {
    ::placeholder {
      font-weight: 300 !important;
    }
  }
  .add {
    max-width: 46px;
    height: 30%;
    border-radius: 28%;
  }
`;
