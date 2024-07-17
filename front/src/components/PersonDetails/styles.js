import styled from "styled-components";

export const PersonDetails = styled.div`
  border: 1px solid #0073e6;
  border-radius: 15px;
  padding: 15px;
  margin-bottom: 6px;
  background-color: #f0f4ff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: space-between;
  gap: 12px;
  flex-direction: column;

  .phoneStyle {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .detailsStyle {
    display: flex;
    margin-top: 10px;
    gap: 12px;
    flex-wrap: wrap;
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
