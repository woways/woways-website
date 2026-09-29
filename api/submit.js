// Woways form handler — emails the team and sends the applicant a confirmation, via Resend.
// Requires a Vercel Environment Variable: RESEND_API_KEY
// Optional env overrides: MAIL_FROM, TEAM_TO, TEAM_CC
// woways.in must be verified as a sending domain in Resend for delivery to work.

const MAIL_FROM = process.env.MAIL_FROM || "Woways <no-reply@woways.in>";
const TEAM_TO = (process.env.TEAM_TO || "tech@woways.in").split(",").map(s => s.trim()).filter(Boolean);
const TEAM_CC = (process.env.TEAM_CC || "povanapun@woways.in, hr@woways.in").split(",").map(s => s.trim()).filter(Boolean);

const TEAM_SUBJECT = {
  partnership: "New partnership requirement — Woways website",
  internship: "New internship application — Woways website",
  enquiry: "New enquiry — Woways website",
};
const APPLICANT_SUBJECT = {
  partnership: "We've received your enquiry — Woways",
  internship: "We've received your application — Woways",
  enquiry: "We've received your message — Woways",
};
const APPLICANT_INTRO = {
  partnership: "Thanks for reaching out to Woways. We've received your partnership enquiry and our team will get back to you within 48 hours.",
  internship: "Thanks for applying to Woways. We've received your application and will review it and get back to you within 48 hours.",
  enquiry: "Thanks for getting in touch with Woways. We've received your message and will reply within 48 hours.",
};

const INTERNAL = new Set(["_form", "_subject", "botcheck", "access_key", "cc", "from_name", "subject"]);
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

function rows(data) {
  return Object.keys(data)
    .filter(k => !INTERNAL.has(k) && String(data[k] ?? "").trim() !== "")
    .map(k => `<tr><td style="padding:8px 14px;border:1px solid #DCE3EA;background:#F5F7FA;font-weight:600;color:#000F24;white-space:nowrap">${esc(k)}</td><td style="padding:8px 14px;border:1px solid #DCE3EA;color:#122238">${esc(data[k]).replace(/\n/g, "<br/>")}</td></tr>`)
    .join("");
}

function teamHtml(type, data) {
  return `<div style="font-family:Arial,Helvetica,sans-serif;max-width:640px;margin:0 auto">
    <p style="color:#00807F;font-size:12px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;margin:0 0 6px">Woways website</p>
    <h2 style="color:#000F24;margin:0 0 16px">${esc(TEAM_SUBJECT[type] || TEAM_SUBJECT.enquiry)}</h2>
    <table style="border-collapse:collapse;width:100%;font-size:14px">${rows(data)}</table>
    <p style="color:#6B7C93;font-size:12px;margin-top:18px">Reply directly to this email to respond to the sender.</p>
  </div>`;
}

function applicantHtml(type, name) {
  return `<div style="font-family:Arial,Helvetica,sans-serif;max-width:560px;margin:0 auto">
    <h2 style="color:#000F24;margin:0 0 12px">Hi${name ? " " + esc(name) : ""},</h2>
    <p style="color:#122238;font-size:15px;line-height:1.6">${esc(APPLICANT_INTRO[type] || APPLICANT_INTRO.enquiry)}</p>
    <p style="color:#122238;font-size:15px;line-height:1.6">If it's urgent, you can also reach us at <a href="mailto:tech@woways.in" style="color:#00807F">tech@woways.in</a> or +91 93901 88553.</p>
    <p style="color:#122238;font-size:15px;line-height:1.6;margin-top:22px">— The Woways team<br/><span style="color:#6B7C93;font-size:13px">Execute. Grow. Transform.</span></p>
  </div>`;
}

async function sendEmail(key, payload) {
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { "Authorization": `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!r.ok) {
    const t = await r.text().catch(() => "");
    throw new Error(`Resend ${r.status}: ${t}`);
  }
  return r.json().catch(() => ({}));
}

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    res.status(405).json({ success: false, message: "Method not allowed." });
    return;
  }
  const key = process.env.RESEND_API_KEY;
  if (!key) {
    res.status(503).json({ success: false, message: "Forms are being connected. Please email tech@woways.in." });
    return;
  }

  let data = req.body;
  if (typeof data === "string") { try { data = JSON.parse(data); } catch { data = {}; } }
  if (!data || typeof data !== "object") data = {};

  // Honeypot: pretend success, send nothing.
  if (data.botcheck) { res.status(200).json({ success: true, message: "Thank you." }); return; }

  const type = ["partnership", "internship", "enquiry"].includes(data._form) ? data._form : "enquiry";
  const applicantEmail = String(data.email || "").trim();
  const applicantName = String(data["Your name"] || data["Full name"] || data.name || "").trim();

  try {
    // 1) Notify the team (reply-to the sender).
    await sendEmail(key, {
      from: MAIL_FROM,
      to: TEAM_TO,
      cc: TEAM_CC,
      reply_to: EMAIL_RE.test(applicantEmail) ? applicantEmail : undefined,
      subject: TEAM_SUBJECT[type] || TEAM_SUBJECT.enquiry,
      html: teamHtml(type, data),
    });

    // 2) Confirm to the applicant (best effort — never fail the request on this).
    if (EMAIL_RE.test(applicantEmail)) {
      try {
        await sendEmail(key, {
          from: MAIL_FROM,
          to: [applicantEmail],
          subject: APPLICANT_SUBJECT[type] || APPLICANT_SUBJECT.enquiry,
          html: applicantHtml(type, applicantName),
        });
      } catch (e) { /* confirmation is non-critical */ }
    }

    res.status(200).json({ success: true, message: "Thank you. Our team will get back to you within 48 hours." });
  } catch (e) {
    res.status(502).json({ success: false, message: "We couldn't send your message. Please email tech@woways.in." });
  }
};
