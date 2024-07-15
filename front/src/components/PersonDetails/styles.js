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
`;
