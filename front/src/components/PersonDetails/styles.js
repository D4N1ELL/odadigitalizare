import styled from "styled-components";

export const StyledPersonDetails = styled.div`
  border: 1px solid #0073e6;
  border-radius: 15px;
  padding: 15px;
  margin-bottom: 6px;
  background-color: #f0f4ff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  gap: 12px;

  .phoneStyle {
    display: flex;
    flex-direction: column;
    gap: 12px;

    &.editing {
      padding: 10px;
      border: 1px solid #0073e6;
      border-radius: 8px;
    }
  }

  .detailsStyle {
    display: flex;
    flex-wrap: wrap;
    margin-top: 10px;
    gap: 12px;
    & > div {
      max-width: calc(50% - 8px);
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }
  }

  .arrowStyle {
    cursor: pointer;
  }

  .summaryStyle {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .noticeTable {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
  }

  .noticeTable th,
  .noticeTable td {
    border: 1px solid #0073e6;
    padding: 8px;
    text-align: center;
  }

  .noticeTable th {
    background-color: #0073e6;
    color: white;
  }

  .noticeTable td {
    position: relative;
  }

  .noticeTable input {
    width: 80%;
    padding: 5px;
    margin: 0;
    box-sizing: border-box;
    border: 1px solid #ccc;
  }
`;

export const ButtonContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 0;

  button {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: white;
    cursor: pointer;

    &:hover {
      background-color: #0056b3;
    }
  }
`;

export const Summary = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #e0e7ff;
  border-radius: 10px;

  .info {
    display: flex;
    gap: 20px;
    justify-content: space-between;
    align-items: center;
    width: 100%;

    .info-item {
      padding: 5px 10px;
      background-color: #d1e7ff;
      border-radius: 5px;
      font-weight: bold;
      color: #000000;
    }
  }
`;

export const Arrow = styled.div`
  margin-left: 16px;
  cursor: pointer;
  font-size: 24px;
`;

export const Input = styled.input`
  padding: 5px;
  margin-left: 10px;
  width: 100%;
  max-width: 200px; /* Adjust the max-width to your preference */
  box-sizing: border-box;
`;