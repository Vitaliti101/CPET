import argparse
from cpet.data_loader import load_csv
from cpet.biomarkers import compute_biomarkers
from cpet.risk import assess_risk
from cpet.recommendations import doctor_recommendations, coach_plan
from cpet.plot import plot_wasserman


def main():
    parser = argparse.ArgumentParser(description="CPET Analysis Tool")
    parser.add_argument('csv', help='Path to CPET CSV data file')
    parser.add_argument('--tid', choices=['polarized', 'pyramidal'], default='polarized',
                        help='Training intensity distribution for coach plan')
    parser.add_argument('--volume', type=float, default=5.0,
                        help='Current weekly training volume in hours (0-10)')
    parser.add_argument('--plot', help='Output path for Wasserman plot image')

    args = parser.parse_args()

    df = load_csv(args.csv)
    biomarkers = compute_biomarkers(df)
    risk = assess_risk(biomarkers)

    doc_recs = doctor_recommendations(risk)
    coach_recs = coach_plan(args.volume, args.tid)

    print('Biomarkers:')
    for k, v in biomarkers.items():
        print(f"  {k}: {v:.2f}")

    print(f"Risk category: {risk}\n")

    print('Doctor Recommendations:')
    for rec in doc_recs:
        print(f"- {rec}")

    print('\nCoach Plan:')
    print(f"  Weekly volumes (h): {coach_recs['weeks']}")
    print(f"  Intensity distribution: {coach_recs['distribution']}")

    if args.plot:
        plot_wasserman(df, args.plot)
        print(f"Plot saved to {args.plot}")


if __name__ == '__main__':
    main()
