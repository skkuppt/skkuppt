import Layout from '../components/layout'
import { getCookie } from 'cookies-next';
import styles from "./index.module.css"; 
import Link from 'next/link';

export default function HomePage({ username }) {
  return (
    <Layout pageTitle="Home">
      <div className={styles.desktop1}>
        {/* 기존 로그인 상태에 따른 인사말을 새로운 UI에 통합 */}
        {username ? (
          <>
            <h2 className={styles.skkuPptMaker}>Hi {username}</h2>
            <div className={styles.groupParent}>
              <Link href="/profile">Profile</Link><br />
              <Link href="/api/logout">Logout</Link>
            </div>
          </>
        ) : (
          <div className={styles.login1}>
            <div className={styles.login1Inner}>
              <div className={styles.groupWrapper}>
                <div className={styles.groupWrapper}>
                  <div className={styles.skkuPptMaker}>SKKU PPT Maker</div>
                  <div className={styles.createSimply}>{`Create simply `}</div>
                </div>
              </div>
            </div>
            <div className={styles.groupParent}>
              <div className={styles.orWrapper}>
                <div className={styles.or}> or</div>
              </div>
              <Link href="/signup">
                <div className={styles.signInButton}>
                  <div className={styles.iconsParent}>
                    <img className={styles.icons} alt="" src="/icons.svg" />
                    <div className={styles.signUp}>Sign up</div>
                  </div>
                </div>
              </Link>
              <Link href="/login">
                <div className={styles.signUpBotton}>
                  <div className={styles.iconsGroup}>
                    <img className={styles.icons} alt="" src="/icons1.svg" />
                    <div className={styles.signUp}>Sign in</div>
                  </div>
                </div>
              </Link>
            </div>
            <div className={styles.div}>
              <img className={styles.skkuIm1} alt="" src="/skku-im-1@2x.png" />
            </div>
          </div>
        )}
      </div>
    </Layout>
  );
}

export async function getServerSideProps(context) {
    const req = context.req
    const res = context.res
    var username = getCookie('username', { req, res });
    if (username == undefined){
        username = false;
    }
    return { props: {username} };
};
