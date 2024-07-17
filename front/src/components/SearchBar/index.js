
const SearchBar = ({ query, setQuery }) => {
  return (
    <div
      style={{
        padding: "12px",
        borderRadius: "25px", // Change to more rounded
        border: "1px solid #0073e6", // Change border color to match the logo's blue
        width: "100%",
        maxWidth: "400px", // Adjust width to be more responsive
        display: "flex",
        justifyContent: "start",
        gap: "0.5em",
        alignItems: "center",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.2)", // Increase shadow for better effect
        backgroundColor: "#f0f4ff", // Light blue background
      }}
    >
      <img src='/images/search.svg' alt="looking-glass" height={20} width={20} style={{ filter: "invert(36%) sepia(100%) saturate(2431%) hue-rotate(191deg) brightness(95%) contrast(101%)" }} />
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search a user..."
        style={{
          width: "100%",
          border: 'none',
          outline: 'none', // Remove input outline
          backgroundColor: 'transparent',
          color: "#0073e6", // Change text color to match the logo
          fontSize: "16px", // Increase font size
          fontWeight: "300", // Make text bold
        }}
      />
    </div>
  );
}

export default SearchBar;
