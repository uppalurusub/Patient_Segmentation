export type Primitive = string | number | boolean | null;
export type ApiValue = Primitive | ApiRecord | ApiValue[];
export interface ApiRecord { [key: string]: ApiValue }

export interface Patient extends ApiRecord {
  patient_id?: string;
  age?: number;
  gender?: string;
  insurance?: string;
  risk_category?: string;
}

export interface SegmentProfile extends ApiRecord {
  segment_id?: number;
  segment_name?: string;
}
