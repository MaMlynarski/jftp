# Aider repository map: JFTP

Generated on 2026-10-06 with Aider 0.86.2 from the repository root.

Aider reported scanning 576 repository files and emitted 92 selected file sections for this 6,000-token-budget map. It shows selected symbols and source context, not every declaration or all runtime behavior. Regenerate it after substantial source-structure changes. The generation completed despite a non-fatal failure to fetch public model metadata from `raw.githubusercontent.com`; no LLM response was requested.

Map-generation command used (PowerShell; output was captured and the startup preamble removed):

```powershell
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
$env:COLUMNS = '220'
$env:GIT_CONFIG_COUNT = '1'
$env:GIT_CONFIG_KEY_0 = 'safe.directory'
$env:GIT_CONFIG_VALUE_0 = (Get-Location).Path.Replace('\', '/')
aider --model gpt-4o-mini --openai-api-key map-only-placeholder --show-repo-map --map-tokens 6000 --map-refresh always --no-check-update --no-pretty
```

The placeholder key was supplied only to bypass Aider's interactive provider setup for map-only execution; the map was generated locally without requesting a model completion. The temporary Git setting applies only to the current process and avoids changing global Git configuration; omit it when Git already trusts the checkout. Aider wrote startup diagnostics before the map, so this saved file retains the generated map beginning at its first source-file entry and omits that console preamble.

```text
src\main\java\com\myjavaworld\gui\DefaultTheme.java:
⋮
│public class DefaultTheme extends DefaultMetalTheme {
│
│       private static final FontUIResource controlFont = new FontUIResource(
│                       "Dialog", Font.PLAIN, 12);
│       private static final FontUIResource systemFont = new FontUIResource(
│                       "Dialog", Font.PLAIN, 12);
│       private static final FontUIResource userFont = new FontUIResource("Dialog",
│                       Font.PLAIN, 12);
│       private static final FontUIResource smallFont = new FontUIResource(
│                       "Dialog", Font.PLAIN, 10);
│
⋮
│       @Override
│       public FontUIResource getControlTextFont() {
⋮
│       @Override
│       public FontUIResource getSystemTextFont() {
⋮
│       @Override
│       public FontUIResource getUserTextFont() {
⋮
│       @Override
│       public FontUIResource getMenuTextFont() {
⋮
│       @Override
│       public FontUIResource getWindowTitleFont() {
⋮
│       @Override
│       public FontUIResource getSubTextFont() {
⋮

src\main\java\com\myjavaworld\gui\GUIUtil.java:
⋮
│public class GUIUtil {
│
│       public static final int ACCELERATOR_MASK = Toolkit.getDefaultToolkit()
│                       .getMenuShortcutKeyMask();
│
│       /**
│        * Gives the center point relative to the user's screen, given the size of
│        * some component.
│        * 
│        * @param size
⋮
│       public static void showInformation(Component parent, String info) {
│               showInformation(parent, CommonResources.getString("title.info"), info,
│                               false);
⋮
│       public static void showInformation(Component parent, String info,
⋮
│       public static void showInformation(Component parent, String title,
⋮
│       public static void showInformation(Component parent, String title,
⋮
│       public static int showConfirmation(Component parent, String message) {
│               return showConfirmation(parent,
│                               CommonResources.getString("title.confirm"), message, false);
⋮
│       public static int showConfirmation(Component parent, String message,
⋮
│       public static int showConfirmation(Component parent, String title,
⋮
│       public static int showConfirmation(Component parent, String title,
⋮
│       public static void showError(Component parent, String error) {
│               showError(parent, CommonResources.getString("title.error"), error,
│                               false);
⋮
│       public static void showError(Component parent, String title, String error) {
│               showError(parent, title, error, false);
⋮
│       public static void showError(Component parent, String title, String error,
⋮
│       public static void showError(Component parent, Throwable t) {
│               showError(parent, CommonResources.getString("title.error"), t);
⋮
│       public static void showError(Component parent, String title, Throwable t) {
│               MessageFormat mf = new MessageFormat(
│                               CommonResources.getString("error.exception"));
│               showError(parent, title, mf.format(new Object[] { t }), true);
│               t.printStackTrace();
⋮
│       public static String htmlFormat(String input) {
│               input = input.replaceAll("\n", "<br>");
│               input = input.replaceAll("\t",
│                               "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
│               return "<html><body><table width=\"500\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><tr><td
│                               + input + "</td></tr></table></body></html>";
⋮

src\main\java\com\myjavaworld\gui\IDTreeNode.java:
⋮
│public class IDTreeNode extends DefaultMutableTreeNode {
│
│       protected int id = 0;
│
│       public IDTreeNode() {
│               super();
│       }
│
│       public IDTreeNode(int id, Object userObject) {
│               super(userObject);
⋮
│       public void setID(int id) {
│               this.id = id;
⋮

src\main\java\com\myjavaworld\gui\IndentIcon.java:
⋮
│public class IndentIcon implements Icon {
│
│       private static final int space = 10;
│       private Icon icon = null;
│       private int depth = 0;
│
│       public IndentIcon() {
│               super();
│       }
│
⋮
│       public void paintIcon(Component c, Graphics g, int x, int y) {
│               if (c.getComponentOrientation().isLeftToRight()) {
│                       icon.paintIcon(c, g, x + depth * space, y);
│               } else {
│                       icon.paintIcon(c, g, x, y);
│               }
⋮
│       public int getIconWidth() {
│               return icon.getIconWidth() + depth * space;
⋮
│       public int getIconHeight() {
│               return icon.getIconHeight();
⋮

src\main\java\com\myjavaworld\gui\IntegerField.java:
⋮
│public class IntegerField extends MTextField {
│
│       /**
│        * Constructs an <code>IntegerField</code>.
│        */
│       public IntegerField() {
│               // super("0");
│               super();
│               // setText("0");
│       }
│
⋮
│       public void setValue(int value) {
│               // super.setText("" + value);
│               setText(String.valueOf(value));
⋮
│       public int getValue() {
│               return Integer.parseInt(getText());
⋮
│       static class IntegerDocument extends SingleLineDocument {
│
│               @Override
│               public void insertString(int offset, String str, AttributeSet a)
│                               throws BadLocationException {
│                       StringBuffer sb = new StringBuffer(getText(0, getLength()));
│                       sb.insert(offset, str);
│                       try {
│                               Integer.parseInt(sb.toString());
│                               super.insertString(offset, str, a);
⋮

src\main\java\com\myjavaworld\gui\MButton.java:
⋮
│public class MButton extends JButton {
│
│       /**
│        * Constructs an object of <code>MButton</code>.
│        * 
│        */
│       public MButton() {
│               super();
│       }
│
⋮
│       public void setMnemonic(String str) {
│               if (str != null && str.trim().length() > 0) {
│                       super.setMnemonic(str.charAt(0));
│               }
⋮
│       public void setDisplayedMnemonicIndex(String str) {
│               if (str != null && str.trim().length() > 0) {
│                       try {
│                               super.setDisplayedMnemonicIndex(Integer.parseInt(str));
│                       } catch (NumberFormatException exp) {
│                               throw exp;
│                       }
│               }
⋮
│       public void setMnemonic(String mnemonic, String mnemonicIndex) {
│               if (!SystemUtil.isMac()) {
│                       super.setMnemonic(mnemonic.charAt(0));
│                       super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│               }
⋮

src\main\java\com\myjavaworld\gui\MCheckBox.java:
⋮
│public class MCheckBox extends JCheckBox {
│
│       public MCheckBox() {
│               super();
│       }
│
│       public MCheckBox(Icon icon) {
│               super(icon);
│       }
│
⋮
│       public void setMnemonic(String mnemonic) {
│               if (mnemonic != null && mnemonic.trim().length() != 0) {
│                       super.setMnemonic(mnemonic.charAt(0));
│               }
⋮
│       public void setDisplayedMnemonicIndex(String mnemonicIndex) {
│               if (mnemonicIndex != null && mnemonicIndex.trim().length() != 0) {
│                       try {
│                               super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│                       } catch (NumberFormatException exp) {
│                               throw exp;
│                       }
│               }
⋮
│       public void setMnemonic(String mnemonic, String mnemonicIndex) {
│               if (!SystemUtil.isMac()) {
│                       super.setMnemonic(mnemonic.charAt(0));
│                       super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│               }
⋮

src\main\java\com\myjavaworld\gui\MGlassPane.java:
⋮
│public class MGlassPane extends JComponent implements MouseListener,
│               KeyListener {
│
⋮
│       public void mouseEntered(MouseEvent evt) {
│               evt.consume();
⋮
│       public void mouseExited(MouseEvent evt) {
│               evt.consume();
⋮
│       public void mousePressed(MouseEvent evt) {
│               evt.consume();
⋮
│       public void mouseReleased(MouseEvent evt) {
│               evt.consume();
⋮
│       public void mouseClicked(MouseEvent evt) {
│               evt.consume();
⋮
│       public void keyPressed(KeyEvent evt) {
│               evt.consume();
⋮
│       public void keyReleased(KeyEvent evt) {
│               evt.consume();
⋮
│       public void keyTyped(KeyEvent evt) {
│               evt.consume();
⋮

src\main\java\com\myjavaworld\gui\MLabel.java:
⋮
│public class MLabel extends JLabel {
│
│       /**
│        * Constructs an object of <code>MLabel</code>.
│        * 
│        */
│       public MLabel() {
│               super();
│       }
│
⋮
│       public void setDisplayedMnemonic(String mnemonic) {
│               if (mnemonic != null && mnemonic.trim().length() > 0) {
│                       super.setDisplayedMnemonic(mnemonic.charAt(0));
│               }
⋮
│       public void setDisplayedMnemonicIndex(String mnemonicIndex) {
│               if (mnemonicIndex != null && mnemonicIndex.trim().length() > 0) {
│                       try {
│                               super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│                       } catch (NumberFormatException exp) {
│                               throw exp;
│                       }
│               }
⋮
│       public void setMnemonic(String mnemonic, String mnemonicIndex) {
│               if (!SystemUtil.isMac()) {
│                       super.setDisplayedMnemonic(mnemonic.charAt(0));
│                       super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│               }
⋮

src\main\java\com\myjavaworld\gui\MMenu.java:
⋮
│public class MMenu extends JMenu {
│
│       public MMenu() {
│               super();
│       }
│
│       public MMenu(String text) {
│               super(text);
│       }
│
⋮
│       public void setMnemonic(String str) {
│               if (str != null && str.trim().length() > 0) {
│                       super.setMnemonic(str.charAt(0));
│               }
⋮
│       public void setDisplayedMnemonicIndex(String str) {
│               if (str != null && str.trim().length() > 0) {
│                       try {
│                               super.setDisplayedMnemonicIndex(Integer.parseInt(str));
│                       } catch (NumberFormatException exp) {
│                               throw exp;
│                       }
│               }
⋮
│       public void setMnemonic(String mnemonic, String mnemonicIndex) {
│               if (!SystemUtil.isMac()) {
│                       super.setMnemonic(mnemonic.charAt(0));
│                       super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│               }
⋮
│       @Override
│       public JMenuItem add(Action action) {
⋮

src\main\java\com\myjavaworld\gui\MMenuItem.java:
⋮
│public class MMenuItem extends JMenuItem {
│
│       public MMenuItem() {
│               super();
│       }
│
│       public MMenuItem(String text) {
│               super(text);
│       }
│
⋮
│       public void setMnemonic(String str) {
│               if (str != null && str.trim().length() > 0) {
│                       super.setMnemonic(str.charAt(0));
│               }
⋮
│       public void setDisplayedMnemonicIndex(String str) {
│               if (str != null && str.trim().length() > 0) {
│                       try {
│                               super.setDisplayedMnemonicIndex(Integer.parseInt(str));
│                       } catch (NumberFormatException exp) {
│                               throw exp;
│                       }
│               }
⋮
│       public void setMnemonic(String mnemonic, String mnemonicIndex) {
│               if (!SystemUtil.isMac()) {
│                       super.setMnemonic(mnemonic.charAt(0));
│                       super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│               }
⋮

src\main\java\com\myjavaworld\gui\MOptionPane.java:
⋮
│public class MOptionPane extends JOptionPane {
│
│       public MOptionPane() {
│               super();
│       }
│
│       public MOptionPane(Object message) {
│               super(message);
│       }
│
⋮
│       @Override
│       public int getMaxCharactersPerLineCount() {
⋮

src\main\java\com\myjavaworld\gui\MPlainDocument.java:
⋮
│public class MPlainDocument extends PlainDocument {
│
│       private int maximumLength = 0;
│       private int characterCase = 0;
│
│       /**
│        * Created an instance of <code>MPlainDocument</code>.
│        * 
│        */
│       public MPlainDocument() {
⋮
│       @Override
│       public void insertString(int offset, String str, AttributeSet a)
⋮

src\main\java\com\myjavaworld\gui\MPopupMenu.java:
⋮
│public class MPopupMenu extends JPopupMenu {
│
│       /**
│        * Displays this popup menu at the given position x and y on the component,
│        * <code>invoker</code>. This method always makes sure that the popup will
│        * fit in the screen. If the popup is going beyond the screen size, the
│        * orientation of the popup will be changed to fit in the screen area.
│        * 
│        * @param invoker
│        *            Component that invoked this popup menu.
⋮
│       @Override
│       public JMenuItem add(Action action) {
⋮

src\main\java\com\myjavaworld\gui\MRadioButton.java:
⋮
│public class MRadioButton extends JRadioButton {
│
│       public MRadioButton() {
│               super();
│       }
│
│       public MRadioButton(String text) {
│               super(text);
│       }
│
⋮
│       public void setMnemonic(String mnemonic) {
│               if (mnemonic != null && mnemonic.trim().length() != 0) {
│                       super.setMnemonic(mnemonic.charAt(0));
│               }
⋮
│       public void setDisplayedMnemonicIndex(String mnemonicIndex) {
│               if (mnemonicIndex != null && mnemonicIndex.trim().length() != 0) {
│                       try {
│                               super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│                       } catch (NumberFormatException exp) {
│                               throw exp;
│                       }
│               }
⋮
│       public void setMnemonic(String mnemonic, String mnemonicIndex) {
│               if (!SystemUtil.isMac()) {
│                       super.setMnemonic(mnemonic.charAt(0));
│                       super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│               }
⋮

src\main\java\com\myjavaworld\gui\MRadioButtonMenuItem.java:
⋮
│public class MRadioButtonMenuItem extends JRadioButtonMenuItem {
│
│       public MRadioButtonMenuItem() {
│               super();
│       }
│
│       public MRadioButtonMenuItem(Icon icon) {
│               super(icon);
│       }
│
⋮
│       public void setMnemonic(String str) {
│               if (str != null && str.trim().length() > 0) {
│                       super.setMnemonic(str.charAt(0));
│               }
⋮
│       public void setDisplayedMnemonicIndex(String str) {
│               if (str != null && str.trim().length() > 0) {
│                       try {
│                               super.setDisplayedMnemonicIndex(Integer.parseInt(str));
│                       } catch (NumberFormatException exp) {
│                               throw exp;
│                       }
│               }
⋮
│       public void setMnemonic(String mnemonic, String mnemonicIndex) {
│               if (!SystemUtil.isMac()) {
│                       super.setMnemonic(mnemonic.charAt(0));
│                       super.setDisplayedMnemonicIndex(Integer.parseInt(mnemonicIndex));
│               }
⋮

src\main\java\com\myjavaworld\gui\MTableCellRenderer.java:
⋮
│public class MTableCellRenderer extends JLabel implements TableCellRenderer {
│
│       /**
│        * Creates an instance of <code>MTableCellRenderer</code>.
│        * 
│        */
│       public MTableCellRenderer() {
│               super();
│               setOpaque(true);
│               setBorder(BorderFactory.createEmptyBorder(1, 5, 1, 5));
⋮

src\main\java\com\myjavaworld\gui\MTextField.java:
⋮
│public class MTextField extends JTextField implements MTextComponent,
⋮

src\main\java\com\myjavaworld\gui\ProgressDialog.java:
⋮
│public class ProgressDialog extends MDialog {
│
│       private static final ResourceBundle resources = ResourceLoader
│                       .getBundle("com.myjavaworld.gui.ProgressDialog");
│       private MButton butCancel = null;
│       private MLabel labMessage = null;
│       private JProgressBar progressBar = null;
│
│       public ProgressDialog(Frame parent) {
│               this(parent, resources.getString("title.dialog"), true);
⋮
│       public void setIndeterminate(boolean indterminate) {
│               progressBar.setIndeterminate(indterminate);
⋮
│       @Override
│       public void setVisible(boolean visible) {
⋮
│       public void addActionListener(ActionListener al) {
│               butCancel.addActionListener(al);
⋮

src\main\java\com\myjavaworld\gui\SingleLineDocument.java:
⋮
│public class SingleLineDocument extends MPlainDocument {
│
│       /**
│        * Default Constructor.
│        * 
│        */
│       public SingleLineDocument() {
│               super();
│       }
│
⋮
│       @Override
│       public void insertString(int offset, String str, AttributeSet a)
⋮

src\main\java\com\myjavaworld\gui\SplashWindow.java:
⋮
│public class SplashWindow extends JWindow {
│
│       /**
│        * Creates an instance of <code>SplashWindow</code>.
│        * 
│        * @param icon
│        *            to show in the splash window
│        * 
│        */
│       public SplashWindow(Icon icon) {
⋮
│       @Override
│       public void setVisible(boolean visible) {
⋮

src\main\java\com\myjavaworld\gui\SwingWorker.java:
⋮
│public abstract class SwingWorker {
│
│       private Object value; // see getValue(), setValue()
│
│       // private Thread thread;
│
│       /**
│        * Class to maintain reference to current worker thread under separate
│        * synchronization control.
│        */
⋮
│       protected synchronized Object getValue() {
│               return value;
⋮
│       private synchronized void setValue(Object x) {
│               value = x;
⋮

src\main\java\com\myjavaworld\jftp\FTPSession.java:
⋮
│public class FTPSession extends SessionPanel implements FTPConnectionListener,
│               ControlConnectionListener, DataConnectionListener, ActionListener,
│               FileChangeListener, ProgressListener, ZipListener {
│
⋮
│       @Override
│       public String toString() {
⋮
│       public boolean isConnected() {
│               if (client == null) {
│                       return false;
│               }
│               return client.isConnected();
⋮

src\main\java\com\myjavaworld\jftp\Favorite.java:
⋮
│public class Favorite extends RemoteHost implements java.io.Serializable,
│               Comparable {
│
⋮
│       @Override
│       public int compareTo(Object obj) {
⋮

src\main\java\com\myjavaworld\jftp\FavoritesDlg.java:
⋮
│public class FavoritesDlg extends MDialog implements ActionListener,
│               ListSelectionListener, MouseListener {
│
⋮
│       class FavoritesListModel extends AbstractListModel {
│
│               private java.util.List favorites = null;
│
│               public FavoritesListModel() {
│                       this(new ArrayList());
│               }
│
│               public FavoritesListModel(java.util.List favorites) {
│                       setFavorites(favorites);
⋮
│               public void add(Object obj) {
│                       favorites.add(obj);
│                       Collections.sort(favorites);
│                       fireContentsChanged(this, 0, this.favorites.size());
⋮

src\main\java\com\myjavaworld\jftp\JFTP.java:
⋮
│public class JFTP extends MFrame implements WindowListener, ActionListener,
│               ChangeListener {
│
⋮
│       public void exit() {
│               int sessionCount = tabs.getTabCount();
│               for (int i = 0; i < sessionCount; i++) {
│                       FTPSession session = (FTPSession) tabs.getComponentAt(i);
│                       session.closeSession();
│               }
│               Rectangle windowBounds = getBounds();
│               prefs.setWindowBounds(windowBounds);
│               try {
│                       savePreferences(prefs);
⋮
│       public FTPSession getCurrentSession() {
│               int selectedTabIndex = tabs.getSelectedIndex();
│               if (selectedTabIndex >= 0) {
│                       return (FTPSession) tabs.getComponentAt(selectedTabIndex);
│               }
│               return null;
⋮

src\main\java\com\myjavaworld\jftp\JFTPConstants.java:
⋮
│public interface JFTPConstants {
│
│       public static final String PRODUCT_CODE = "jftp";
│       public static final String PRODUCT_NAME = "JFTP";
│       public static final String PRODUCT_DESCRIPTION = "The Universal FTP Client";
│       public static final String PRODUCT_VERSION = "5.0.1";
│       public static final String PRODUCT_BUILD = "20120623";
│       public static final String AUTHOR_NAME = "Sai Pullabhotla";
│       public static final String AUTHOR_EMAIL = "psai@jMethods.com";
│       public static final String PRODUCT_WEBSITE = "http://www.jMethods.com";
⋮

src\main\java\com\myjavaworld\jftp\JFTPHelp2.java:
⋮
│public class JFTPHelp2 {
│
│       private static String HELPSET_NAME = "helpSet";
│       private static String HELPSET_EXTENSION = ".xml";
│       private HelpSet hs = null;
│       private HelpBroker hb = null;
│       private static JFTPHelp2 instance = null;
│
│       private JFTPHelp2() {
│               super();
⋮
│       public void enableHelp(Component comp, String id) {
│               hb.enableHelpOnButton(comp, id, hs);
⋮
│       public void enableHelpKey(Component comp, String id) {
│               hb.enableHelpKey(comp, id, hs);
⋮

src\main\java\com\myjavaworld\jftp\JFTPPreferences.java:
⋮
│public class JFTPPreferences implements Serializable {
│
│       private static final long serialVersionUID = 4316033315068041786L;
│       private static final String DEFAULT_SERVER_CERTIFICATE_STORE = JFTP.DATA_HOME
│                       + File.separator + "serverCertificates.jks";
│       private static final String DEFAULT_CLIENT_CERTIFICATE_STORE = JFTP.DATA_HOME
│                       + File.separator + "clientCertificates.jks";
│       private static final char[] DEFAULT_CERTIFICATE_STORE_PASSWORD = "changeit"
│                       .toCharArray();
│       private static final int DEFAULT_SOCKS_PROXY_PORT = 1080;
⋮
│       public void setPassive(boolean passive) {
│               this.passive = passive;
⋮
│       public void setSSLUsage(int sslUsage) {
│               this.sslUsage = new Integer(sslUsage);
⋮
│       public void setImplicitSSLPort(int implicitSSLPort) {
│               this.implicitSSLPort = new Integer(implicitSSLPort);
⋮
│       public void setDataChannelUnencrypted(boolean dataChannelUnencrypted) {
│               this.dataChannelUnencrypted = new Boolean(dataChannelUnencrypted);
⋮

src\main\java\com\myjavaworld\jftp\JFTPToolBar.java:
⋮
│public class JFTPToolBar extends JToolBar {
│
│       private static final String HELP_ID_HOME = "index";
│       private JFTP jftp = null;
│       private MButton butNewSession = null;
│       private MButton butConnect = null;
│       private MButton butDisconnect = null;
│       private MButton butReconnect = null;
│       private MButton butAbort = null;
│       private MButton butUpload = null;
⋮
│       @Override
│       public JButton add(Action action) {
⋮

src\main\java\com\myjavaworld\jftp\LocalFile.java:
⋮
│public class LocalFile implements Serializable {
│
│       /**
│        * Serial version UID 
│        */
│       private static final long serialVersionUID = -3450118298480840794L;
│       private static final FileSystemView fsv = FileSystemView
│                       .getFileSystemView();
│       private File file = null;
│       private String name = null;
⋮
│       public String getAbsolutePath() {
│               return file.getAbsolutePath();
⋮
│       public LocalFile getAbsoluteFile() {
│               return new LocalFile(file.getAbsoluteFile());
⋮
│       public String getCanonicalPath() throws IOException {
│               return file.getCanonicalPath();
⋮
│       public LocalFile getCanonicalFile() throws IOException {
│               return new LocalFile(file.getCanonicalFile());
⋮
│       public String getDisplayName() {
│               return displayName;
⋮
│       public String getTypeOld() {
│               if (extension == null) {
│                       return "Directory";
│               }
│               if (extension.length() > 0) {
│                       return extension + " File";
│               }
│               return "File";
⋮
│       public long getLastModified() {
│               return lastModified;
⋮
│       public boolean isDirectory() {
│               return dir;
⋮
│       public boolean canWrite() {
│               return file.canWrite();
⋮
│       public boolean isHidden() {
│               return file.isHidden();
⋮
│       public int compareTo(Object obj) {
│               if (obj == null) {
│                       return 1;
│               }
│               LocalFile that = (LocalFile) obj;
│               return name.toUpperCase().compareTo(that.name.toUpperCase());
⋮
│       @Override
│       public String toString() {
⋮
│       public boolean isTraversable() {
│               return fsv.isTraversable(file).booleanValue();
⋮

src\main\java\com\myjavaworld\jftp\LocalPane.java:
⋮
│public class LocalPane extends JPanel implements ActionListener, MouseListener,
│               ListSelectionListener {
│
⋮
│       private LocalFile[] getRoots() {
│               LocalFile[] roots = LocalFile.listRoots();
│               if (roots == null) {
│                       roots = new LocalFile[0];
│               }
│               return roots;
⋮

src\main\java\com\myjavaworld\jftp\RemoteHost.java:
⋮
│public class RemoteHost implements Serializable, Comparable {
│
│       private static final long serialVersionUID = -3213664402994404410L;
│       public static final String DEFAULT_FTP_CLIENT_CLASS_NAME = "com.myjavaworld.ftp.DefaultFTPClient";
│       public static final String DEFAULT_LIST_PARSER_CLASS_NAME = "com.myjavaworld.ftp.DefaultListParser
│       protected String name = null;
│       protected String hostName = null;
│       protected int port = 0;
│       protected String user = null;
│       protected String password = null;
⋮
│       public void setHostName(String hostName) {
│               this.hostName = hostName == null ? "" : hostName.trim();
⋮
│       public void setPassword(String password) {
│               this.password = password == null ? "" : password;
⋮
│       public void setAccount(String account) {
│               this.account = account == null ? "" : account;
⋮
│       public void setFTPClientClassName(String ftpClientClassName) {
│               this.ftpClientClassName = ftpClientClassName;
⋮
│       public void setListParserClassName(String listParserClassName) {
│               this.listParserClassName = listParserClassName;
⋮
│       public void setCommands(String[] commands) {
│               this.commands = commands;
⋮
│       public void setCommands(String commands) {
│               StringTokenizer tokenizer = new StringTokenizer(commands, "\r\n");
│               List commandList = new ArrayList(5);
│               while (tokenizer.hasMoreTokens()) {
│                       String token = tokenizer.nextToken();
│                       if (token.trim().length() > 0) {
│                               commandList.add(token);
│                       }
│               }
│               String[] commandArray = new String[commandList.size()];
⋮
│       public void setPassive(boolean passive) {
│               this.passive = passive;
⋮
│       public void setSSLUsage(int sslUsage) {
│               this.sslUsage = sslUsage;
⋮
│       public void setDataChannelUnencrypted(boolean dataChannelUnencrypted) {
│               this.dataChannelUnencrypted = dataChannelUnencrypted;
⋮
│       public void setImplicitSSLPort(int implicitSSLPort) {
│               this.implicitSSLPort = new Integer(implicitSSLPort);
⋮
│       @Override
│       public String toString() {
⋮
│       public int compareTo(Object obj) {
│               RemoteHost that = (RemoteHost) obj;
│               return this.name.toUpperCase().compareTo(that.name.toUpperCase());
⋮

src\main\java\com\myjavaworld\jftp\StatusBar.java:
⋮
│public class StatusBar extends JPanel {
│
│       private static final ResourceBundle resources = ResourceLoader
│                       .getBundle("com.myjavaworld.jftp.StatusBar");
│       private MLabel labStatus = null;
│       private JProgressBar progressBar = null;
│       private MLabel labSpeed = null;
│       private MLabel labElapsedTime = null;
│       private MLabel labSecured = null;
│       private MessageFormat speedFormat;
⋮
│       public void setMaximum(int max) {
│               progressBar.setMaximum(max);
⋮
│       public void setIndeterminate(boolean indeterminate) {
│               progressBar.setIndeterminate(indeterminate);
│               progressBar.setStringPainted(!indeterminate);
⋮

src\main\java\com\myjavaworld\jftp\TransferObject.java:
⋮
│public class TransferObject {
│
│       public static int DOWNLOAD = 1;
│       public static int UPLOAD = 2;
│       private int direction = 0;
│       private LocalFile localFile = null;
│       private RemoteFile remoteFile = null;
│
│       public TransferObject(int direction, LocalFile localFile,
│                       RemoteFile remoteFile) {
⋮
│       @Override
│       public String toString() {
⋮

src\main\java\com\myjavaworld\jftp\actions\EmailLocalFileAction.java:
⋮
│public class EmailLocalFileAction implements ActionListener {
│
│       private JFTP jftp = null;
│       private static EmailLocalFileAction instance = null;
│
│       private EmailLocalFileAction(JFTP jftp) {
│               this.jftp = jftp;
│       }
│
│       public static synchronized EmailLocalFileAction getInstance(JFTP jftp) {
⋮

src\main\java\com\myjavaworld\jftp\actions\EmailRemoteFileAction.java:
⋮
│public class EmailRemoteFileAction implements ActionListener {
│
│       private JFTP jftp = null;
│       private static EmailRemoteFileAction instance = null;
│
│       private EmailRemoteFileAction(JFTP jftp) {
│               this.jftp = jftp;
│       }
│
│       public static synchronized EmailRemoteFileAction getInstance(JFTP jftp) {
⋮

src\main\java\com\myjavaworld\util\CommonResources.java:
⋮
│public class CommonResources {
│
│       private static final ResourceBundle resources = ResourceLoader
│                       .getBundle("com.myjavaworld.util.CommonResources");
│
│       public static String getString(String key) {
│               return resources.getString(key);
│       }
⋮

src\main\java\com\myjavaworld\util\FileChangeEvent.java:
⋮
│public class FileChangeEvent extends EventObject {
│
│       public File file = null;
│       public long oldDate = 0L;
│       public long newDate = 0L;
│
│       public FileChangeEvent(Object source, File file, long oldDate, long newDate) {
│               super(source);
│               this.file = file;
│               this.oldDate = oldDate;
⋮
│       public long getOldDate() {
│               return oldDate;
⋮
│       public long getnewDate() {
│               return newDate;
⋮

src\main\java\com\myjavaworld\util\FileChangeMonitor.java:
⋮
│public class FileChangeMonitor implements ActionListener {
│
│       private Hashtable filesToMonitor = null;
│       private EventListenerList listenerList = null;
│       private Timer timer = null;
│
│       public FileChangeMonitor() {
│               filesToMonitor = new Hashtable();
│               listenerList = new EventListenerList();
│       }
│
│       public synchronized void add(File file) {
│               filesToMonitor.put(file, new Long(file.lastModified()));
│               if (timer == null) {
│                       if (timer == null) {
│                               timer = new Timer(1000, this);
│                               timer.start();
│                       }
│               }
⋮

src\main\java\com\myjavaworld\util\ResourceLoader.java:
⋮
│public class ResourceLoader {
│
│       public static ResourceBundle getBundle(String baseName) {
│               return getBundle(baseName, Locale.getDefault());
│       }
│
│       public static ResourceBundle getBundle(String baseName, Locale locale) {
│               try {
│                       return ResourceBundle.getBundle(baseName, locale);
│               } catch (MissingResourceException exp) {
│                       exp.printStackTrace();
│                       fireResourceNotFound(baseName, locale);
│                       return null;
│               }
⋮
│       public static ResourceBundle getBundle(String baseName, Locale locale,
⋮
│       private static void fireResourceNotFound(String baseName, Locale locale) {
│               System.err.println("Resource " + baseName + " Not Found for Locale "
│                               + locale + ". ");
│               System.exit(1);
⋮

src\main\java\com\myjavaworld\util\StatusEvent.java:
⋮
│public class StatusEvent extends EventObject {
│
│       private String status = null;
│
│       public StatusEvent(Object source, String status) {
│               super(source);
│               this.status = status;
│       }
│
│       public String getStatus() {
│               return status;
⋮

src\main\java\com\myjavaworld\util\StatusListener.java:
⋮
│public interface StatusListener extends EventListener {
│
│       public void statusChanged(StatusEvent evt);
⋮

src\main\java\com\myjavaworld\util\SystemUtil.java:
⋮
│public class SystemUtil {
│
│       private static String osName = null;
│       private static String osVersion = null;
│       private static String jreVersion = null;
│       private static String jreVendor = null;
│       private static String javaHome = null;
│       private static String userHome = null;
│       private static String workingDirectory = null;
│       private static boolean isMac = false;
│
⋮
│       public static boolean isMac() {
│               return isMac;
⋮
│       public static String getOSName() {
│               return osName;
⋮

src\main\resources\com\myjavaworld\jftp\AboutDlg.properties:
⋮
│text.productInfo=<html>\
│       {0}, Version {1}, Build {2}\
│       <br>\
│       {3}\
│       <br>\
│       {4}\
│       <br>\
│       {5}\
⋮

src\main\resources\com\myjavaworld\jftp\AutoUpdater.properties:
⋮
│message.updatesAvailable=\
│       <strong>A new version of {0} is now available for download. </strong>\
│       \n\
│       \n\
│       You are currently running on version {1} and the latest \
│       version available is {2}. \
│       \n\
│       \n\
│       For more information and download, please visit <strong>{3}</strong>. 
│message.updatesNotAvailable=No updates are available at this time. 

src\main\resources\com\myjavaworld\jftp\ConnectionDlg.properties:
⋮
│text.initialLocalDirectory=Initial Local Directory
│text.initialRemoteDirectory=Initial Remote Directory
⋮
│text.implicitSSLPort=Port Number
⋮

src\main\resources\com\myjavaworld\jftp\FavoritePropertiesDlg.properties:
⋮
│text.initialLocalDirectory=Initial Local Directory
│text.initialRemoteDirectory=Initial Remote Directory
│text.passive=Transfer Data in Passive Mode
│text.executeCommands=Execute the following commands after login
⋮
│text.implicitSSLPort=Port Number
⋮
│error.implicitSSLPort.invalid=Please enter the Implicit SSL port number. \n\
⋮

src\main\resources\com\myjavaworld\jftp\FavoritesDlg.properties:
⋮
│error.duplicateFavorite=A favorite with the specified name already exists. \n\
│    Please specify another name and try again. 
│confirm.deleteFavorites=Are you sure you want to delete the selected item(s) from your \
⋮

src\main\resources\com\myjavaworld\jftp\GeneralConnectionPrefsPanel.properties:
⋮
│text.defaultLocalDirectory=Default Local Directory
│error.email.required=Please specify the e-mail address
│error.defaultLocalDirectory.required=Please Specify the default local directory

src\main\resources\com\myjavaworld\jftp\JFTP.properties:
│text.notConnected=Not Connected
│error.duplicateFavorite=A favorite with the specified name already exists. \n\
⋮

src\main\resources\com\myjavaworld\jftp\LocalFilePropertiesDlg.properties:
⋮
│text.fullPath=Full Path
⋮

src\main\resources\com\myjavaworld\jftp\LocalPane.properties:
⋮
│tooltip.workingDirectory=Current local working directory
│tooltip.up=Displays the contents of the parent directory
│status.objectCount={0} Object(s). {1} Byte(s). 
│status.selectedObjectCount={0} Object(s) Selected. {1} Byte(s). 

src\main\resources\com\myjavaworld\jftp\LocalePrefsPanel.properties:
⋮
│text.dateFormat=Date Format
│text.timeFormat=Time Format
⋮

src\main\resources\com\myjavaworld\jftp\ProxyPrefsPanel.properties:
│text.useProxy=Use the following SOCKS proxy
⋮

src\main\resources\com\myjavaworld\jftp\RemoteFilePropertiesDlg.properties:
⋮
│text.fullPath=Full Path
⋮

src\main\resources\com\myjavaworld\jftp\RemotePane.properties:
│tooltip.workingDirectory=Current Remote working directory
│tooltip.up=Displays the contents of the parent directory
│status.objectCount={0,number} Object(s). {1,number} Byte(s). 
│status.selectedObjectCount={0,number} Object(s) Selected. {1,number} Byte(s). 

src\main\resources\com\myjavaworld\jftp\SoftwareUpdatePrefsPanel.properties:
│text.checkForUpdates=Periodically check for software updates
│text.checkNow=Check Now

src\main\resources\com\myjavaworld\jftp\StatusBar.properties:
⋮
│value.elapsedTime=Elapsed Time: {0}

src\main\resources\com\myjavaworld\jftp\StatusWindow.properties:
│text.productInfo={0} - The Universal FTP Client, Version {1}, Build {2} 
│
⋮

src\main\resources\com\myjavaworld\jftp\TransferModeMenu.properties:
│text.transferMode=Transfer Mode
⋮

src\main\resources\com\myjavaworld\jftp\TransferModesPrefsPanel.properties:
⋮
│text.transferMode=Transfer Mode
⋮

src\main\resources\com\myjavaworld\jftp\UIPrefsPanel.properties:
│text.lookAndFeel=Look and Feel

src\main\resources\com\myjavaworld\jftp\ZipAndUploadDlg.properties:
⋮
│text.zipToTempDir=Create zip file in a temporary directory and delete it after uploading
│text.zipToCurrentDir=Create zip file in the current local working directory
│text.zipToOtherDir=Create zip file in the directory specified below:
⋮
│error.otherDir.required=Please specify the directory to create the zip file in. 
│error.otherDir.doesNotExists=Specified directory does not exists

src\main\resources\com\myjavaworld\jftp\ssl\CertificateManagerDlg.properties:
⋮
│text.serverCertificates=Server Certificates
│text.clientCertificates=Client Certificates
│text.import=Import...
│confirm.deleteServerCertificates=Are you sure you want to delete the selected certificate(s) \n\
│       from your trusted certificate database ? 
│confirm.deleteClientCertificates.message=Are you sure you want to delete the selected certificate(s
⋮

src\main\resources\com\myjavaworld\jftp\ssl\CertificateTableModel.properties:
⋮
│text.validFrom=Valid From
│text.validTo=Valid To

src\main\resources_de\com\myjavaworld\jftp\JFTP_de.properties:
│text.notConnected=Nicht verbunden
│error.duplicateFavorite=Ein Favorit mit dem angegebenen Namen existiert bereits. \n\
⋮

src\main\resources_de\com\myjavaworld\jftp\RemotePane_de.properties:
│tooltip.workingDirectory=Aktuelles entferntes Arbeitsverzeichnis
│tooltip.up=Zeigt den Inhalt des Elternverzeichnisses
│status.objectCount={0,number} Objekt(e). {1,number} Byte(s). 
│status.selectedObjectCount={0,number} Objekt(e) markiert. {1,number} Byte(s). 

src\main\resources_de\com\myjavaworld\jftp\StatusBar_de.properties:
⋮
│value.elapsedTime=Verstrichene Zeit: {0}

src\main\resources_de\com\myjavaworld\jftp\UIPrefsPanel_de.properties:
│text.lookAndFeel=Look and Feel

src\main\resources_zh_TW\com\myjavaworld\jftp\AboutDlg_zh_TW.properties:
⋮
│text.productInfo=<html>{0}, \u7248\u672c {1}, \u7de8\u8b6f\u7248\u672c {2}<br>{3}<br>{4}<br>{5}</ht
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\AutoUpdater_zh_TW.properties:
⋮
│message.updatesAvailable=<strong>\u73fe\u5728\u6709\u65b0\u7248\u672c {0} \u53ef\u4f9b\u53ef\u8f09\
│\n\
│\u60a8\u76ee\u524d\u57f7\u884c\u7684\u662f\u7248\u672c {1} \u800c\u6700\u65b0\u53ef\u4f9b\u4f7f\u75
│\n\
│\u66f4\u591a\u7684\u8cc7\u8a0a\u53ca\u4e0b\u8f09\uff0c\u8acb\u53c3\u8a2a <strong>{3}</strong>. 
│message.updatesNotAvailable=\u76ee\u524d\u6c92\u6709\u65b0\u7248\u53ef\u4ee5\u4f7f\u7528.

src\main\resources_zh_TW\com\myjavaworld\jftp\ConnectionDlg_zh_TW.properties:
⋮
│text.initialLocalDirectory=\u8d77\u59cb\u672c\u6a5f\u76ee\u9304
│text.initialRemoteDirectory=\u8d77\u59cb\u9060\u7aef\u76ee\u9304
│text.passive=\u4ee5\u88ab\u52d5\u6a21\u5f0f\u50b3\u9001\u8cc7\u6599
│text.executeCommands=\u767b\u5165\u5f8c\u57f7\u884c\u4e0b\u5217\u547d\u4ee4
⋮
│text.implicitSSLPort=\u9023\u63a5\u57e0\u865f\u78bc
⋮
│error.implicitSSLPort.invalid=\u8acb\u8f38\u5165\u96b1\u542b\u7684 SSL \u9023\u63a5\u57e0\u865f\u78
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\FavoritePropertiesDlg_zh_TW.properties:
⋮
│text.initialLocalDirectory=\u8d77\u59cb\u672c\u6a5f\u76ee\u9304
│text.initialRemoteDirectory=\u8d77\u59cb\u9060\u7aef\u76ee\u9304
│text.passive=\u4ee5\u88ab\u52d5\u6a21\u5f0f\u50b3\u9001\u8cc7\u6599
│text.executeCommands=\u767b\u5165\u5f8c\u57f7\u884c\u4e0b\u5217\u547d\u4ee4
⋮
│text.implicitSSLPort=\u9023\u63a5\u57e0\u865f\u78bc
⋮
│error.implicitSSLPort.invalid=\u8acb\u8f38\u5165\u96b1\u542b\u7684 SSL \u9023\u63a5\u57e0\u865f\u78
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\FavoritesDlg_zh_TW.properties:
⋮
│error.duplicateFavorite=\u6307\u5b9a\u7684\u540d\u7a31\u5df2\u5b58\u5728\u3002 \n\
│\u8acb\u6307\u5b9a\u53e6\u4e00\u500b\u540d\u7a31\u518d\u8a66\u4e00\u6b21\u3002 
│confirm.deleteFavorites=\u60a8\u78ba\u5b9a\u8981\u5f9e\u6211\u7684\u6700\u611b\u6e05\u55ae\u4e2d\u5

src\main\resources_zh_TW\com\myjavaworld\jftp\GeneralConnectionPrefsPanel_zh_TW.properties:
⋮
│text.defaultLocalDirectory=\u9810\u8a2d\u672c\u6a5f\u76ee\u9304
│error.email.required=\u8acb\u6307\u5b9a\u500b\u96fb\u5b50\u90f5\u4ef6\u4fe1\u7bb1
│error.defaultLocalDirectory.required=\u8acb\u6307\u5b9a\u9810\u8a2d\u672c\u6a5f\u76ee\u9304

src\main\resources_zh_TW\com\myjavaworld\jftp\JFTP_zh_TW.properties:
⋮
│text.notConnected=\u672a\u9023\u7dda
│error.duplicateFavorite=\u6307\u5b9a\u7684\u540d\u7a31\u5df2\u5b58\u5728\u3002 \n\
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\LocalFilePropertiesDlg_zh_TW.properties:
⋮
│text.fullPath=\u5b8c\u6574\u8def\u5f91
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\LocalPane_zh_TW.properties:
⋮
│tooltip.workingDirectory=\u76ee\u524d\u672c\u6a5f\u5de5\u4f5c\u76ee\u9304
│tooltip.up=\u986f\u793a\u4e0a\u5c64\u76ee\u9304\u7684\u5167\u5bb9
│status.objectCount={0} \u7269\u4ef6. {1} \u4f4d\u5143\u7d44. 
│status.selectedObjectCount={0} \u7269\u4ef6\u88ab\u9078\u53d6. {1} \u4f4d\u5143\u7d44. 

src\main\resources_zh_TW\com\myjavaworld\jftp\LocalePrefsPanel_zh_TW.properties:
⋮
│text.dateFormat=\u65e5\u671f\u683c\u5f0f
│text.timeFormat=\u6642\u9593\u683c\u5f0f
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\ProxyPrefsPanel_zh_TW.properties:
⋮
│text.useProxy=\u4f7f\u7528\u4e0b\u5217 SOCKS \u4ee3\u7406\u4f3a\u670d\u5668
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\RemoteFilePropertiesDlg_zh_TW.properties:
⋮
│text.fullPath=\u5b8c\u6574\u8def\u5f91
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\RemotePane_zh_TW.properties:
⋮
│tooltip.workingDirectory=\u76ee\u524d\u9060\u7aef\u5de5\u4f5c\u76ee\u9304
│tooltip.up=\u986f\u793a\u4e0a\u5c64\u76ee\u9304\u7684\u5167\u5bb9
│status.objectCount={0,number} \u7269\u4ef6. {1,number} \u4f4d\u5143\u7d44. 
│status.selectedObjectCount={0,number} \u7269\u4ef6\u88ab\u9078\u53d6. {1,number} \u4f4d\u5143\u7d44

src\main\resources_zh_TW\com\myjavaworld\jftp\SoftwareUpdatePrefsPanel_zh_TW.properties:
⋮
│text.checkForUpdates=\u5b9a\u671f\u6aa2\u67e5\u8edf\u9ad4\u66f4\u65b0
│text.checkNow=\u73fe\u5728\u6aa2\u67e5

src\main\resources_zh_TW\com\myjavaworld\jftp\StatusBar_zh_TW.properties:
⋮
│value.elapsedTime=\u7d93\u904e\u6642\u9593: {0}

src\main\resources_zh_TW\com\myjavaworld\jftp\StatusWindow_zh_TW.properties:
⋮
│text.productInfo={0} - Universal FTP \u5ba2\u6236\u7aef, \u7248\u672c {1}, \u7de8\u8b6f\u7248\u672c
│
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\TransferModeMenu_zh_TW.properties:
⋮
│text.transferMode=\u50b3\u8f38\u6a21\u5f0f(M)
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\TransferModesPrefsPanel_zh_TW.properties:
⋮
│text.transferMode=\u50b3\u8f38\u6a21\u5f0f
⋮

src\main\resources_zh_TW\com\myjavaworld\jftp\UIPrefsPanel_zh_TW.properties:
⋮
│text.lookAndFeel=\u8996\u89ba\u5316\u5916\u89c0

src\main\resources_zh_TW\com\myjavaworld\jftp\ZipAndUploadDlg_zh_TW.properties:
⋮
│text.zipToTempDir=\u5efa\u7acb\u58d3\u7e2e\u6a94\u5728\u66ab\u5b58\u76ee\u9304\u4e14\u4e0a\u50b3\u5
│text.zipToCurrentDir=\u5efa\u7acb\u58d3\u7e2e\u6a94\u5728\u76ee\u524d\u672c\u6a5f\u5de5\u4f5c\u76ee
│text.zipToOtherDir=\u5efa\u7acb\u58d3\u7e2e\u6a94\u5728\u4e0b\u9762\u6307\u5b9a\u7684\u76ee\u9304:
⋮
│error.otherDir.required=\u8acb\u6307\u5b9a\u5efa\u7acb\u58d3\u7e2e\u6a94\u6240\u5728\u7684\u76ee\u9
│error.otherDir.doesNotExists=\u6307\u5b9a\u7684\u76ee\u9304\u4e0d\u5b58\u5728

src\main\resources_zh_TW\com\myjavaworld\jftp\ssl\CertificateManagerDlg_zh_TW.properties:
⋮
│text.serverCertificates=\u4f3a\u670d\u5668\u6191\u8b49
│text.clientCertificates=\u5ba2\u6236\u7aef\u6191\u8b49
│text.import=\u532f\u5165...
│confirm.deleteServerCertificates=\u60a8\u78ba\u5b9a\u8981\u5f9e\u60a8\u7684\u53d7\u4fe1\u4efb\u6191
│confirm.deleteClientCertificates.message=\u60a8\u78ba\u5b9a\u8981\u5f9e\u60a8\u7684\u6191\u8b49\u8c

src\main\resources_zh_TW\com\myjavaworld\jftp\ssl\CertificateTableModel_zh_TW.properties:
⋮
│text.validFrom=\u6709\u6548\u671f\u5f9e
│text.validTo=\u6709\u6548\u671f\u5230
```
