import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.TreeSet;

/**
 *
 * @Author Master Ward Project used to list all possible Filenames in order
 **/
public class Main2 {

	public static void main(String[] args) throws Exception {
		// File f = new File("C:\\Users\\maste\\Desktop\\Python PDF Project");
		File f = new File("C:\\Users\\maste\\Dropbox\\XX");
		File s[] = f.listFiles();
		ArrayList<File> cur = new ArrayList<>();
		ArrayList<File> fin = new ArrayList<>();
		TreeSet<String> hs = new TreeSet<>();
		ArrayList<String> fins = new ArrayList<>();
		
		for (File i : s) {
			cur.add(i);
		}
		while (!cur.isEmpty()) {
			File temp = cur.remove(0);
			if (temp.isDirectory()) {
				File te[] = temp.listFiles();
				for (File i : te) {
					cur.add(i);
				}
			} else {
				if (temp.getName().contains(".pdf")) {
					fin.add(temp);
					hs.add(temp.getName());
//					hs.add(temp.getPath());
				}
			}
		}
		/*
		for(String sd: hs) {
			System.out.println(sd);
		}
//		fins.addAll(fin);
 */
		for(File sd: fin) {
			fins.add(sd.getName());
		}
		Collections.sort(fins);
		/*
		for(File sd: fin) {
			System.out.println(sd.getName());
		}
		/*
		int o = 0;
		for (File qq : fin) {
			// System.out.println(qq.getAbsolutePath() + " " + qq.getName());
			System.out.println(qq.getAbsolutePath() + " " + o++);
		}
*/		
//		System.out.println(fins.toString());
		System.out.print("[\'");
		Object qx[] = hs.toArray();
		for (int i = 0; i < qx.length; i++) {
//			if(i % 40 == 0) {
//				System.out.println();
//			}
			System.out.println(qx[i] + "\', \'");
		}
		
		System.out.println("]");
/*
		// System.out.println(Arrays.toString(qx));
		Path p = Paths.get(fin.get(0).getAbsolutePath());
		File ff = fin.get(41);
		File fq = fin.get(55);
		Date df = new Date(ff.lastModified());
		Date dq = new Date(fq.lastModified());
		System.out.println(df);
		System.out.println(dq);
		if (df.before(dq)) {
			System.out.println("Date 1 is before date 2");
		} else {
			System.out.println("Date 2 is before date 1");
		}

		// PosixFileAttributes attr = Files.readAttributes(p,
		// PostfixFileAttributes.class);
		// BasicFileAttributes attr = Files.readAttributes(p, BasicAttributes.class,
		// NOFOLLOW_LINK);

		String sp = "C:\\Users\\maste\\Desktop\\Python PDF Project\\PDF Attempt 1.py";
		Process pro = Runtime.getRuntime().exec("python " + sp);
		*/
	}
}
