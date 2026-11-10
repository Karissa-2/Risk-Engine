function EventForm() {
  return (
    <form>
      <label>Duration:</label>
      <input id="duration" type="number" name="duration" step="any"/>
      <br />

      <label>Protocol Type:</label>
      <select id="protocolType" name="protocolType">
        <option value="TCP">TCP</option>
        <option value="UDP">UDP</option>
        <option value="ICMP">ICMP</option>
      </select>
      <br />

      <label>Service:</label>
      <select id="service" name="service">
        <option value="AOL">AOL</option>
        <option value="AUTH">AUTH</option>
        <option value="BGP">BGP</option>
      </select>
      <br />

      <label>Src Bytes:</label>
      <input id="srcBytes" type="number" name="srcBytes" step="any"/>
      <br />

      <button type="submit">Submit</button>
    </form>
  );
}

export default EventForm;
