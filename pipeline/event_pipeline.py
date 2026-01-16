from models.qa_detector import detect_qa_events
from models.agreement_detector import detect_agreement
from models.disagreement_detector import detect_disagreement

def run_event_pipeline(segments):
    events = []
    events.extend(detect_qa_events(segments))
    events.extend(detect_agreement(segments))
    events.extend(detect_disagreement(segments))
    return events
