'use client';

import { useEffect, useState } from 'react';

const API = '/api';

interface Record {
  id: string;
  ownerId: string;
  patientName: string;
  ssn: string;
  diagnosis: string;
  notes: string;
  createdAt: string;
}

export default function RecordsPage() {
  const [selectedUser, setSelectedUser] = useState('');
  const [records, setRecords] = useState<Record[]>([]);
  const [loading, setLoading] = useState(false);

  async function load(user: string) {
    setLoading(true);
    const res = await fetch(`${API}/records?ownerId=${user}`, {
      headers: { 'x-user-id': user },
    });
    const data = await res.json();
    setRecords(data);
    setLoading(false);
  }

  useEffect(() => {
    load(selectedUser);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <main>
      <h1>Records</h1>

      <div style={{ marginBottom: 16 }}>
        <span style={{ marginRight: 8 }}>View as:</span>
        <button onClick={() => { setSelectedUser('user-1'); load('user-1'); }}>
          user-1
        </button>{' '}
        <button onClick={() => { setSelectedUser('user-2'); load('user-2'); }}>
          user-2
        </button>
        <span style={{ marginLeft: 12, color: '#888' }}>
          current: {selectedUser || '(none)'}
        </span>
      </div>

      {loading && <p>Loading…</p>}

      <table cellPadding={8} style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr style={{ textAlign: 'left', borderBottom: '1px solid #ccc' }}>
            <th>Patient</th>
            <th>Owner</th>
            <th>SSN</th>
            <th>Diagnosis</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          {records.map((r) => (
            <tr key={r.id} style={{ borderBottom: '1px solid #eee' }}>
              <td>{r.patientName}</td>
              <td>{r.ownerId}</td>
              <td>{r.ssn}</td>
              <td>{r.diagnosis}</td>
              <td>{r.notes}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {!loading && records.length === 0 && <p>No records.</p>}
    </main>
  );
}
