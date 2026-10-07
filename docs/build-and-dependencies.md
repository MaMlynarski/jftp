# Build and dependencies (current state)

This page records the build configuration currently present in the repository. It describes configured behavior; it does not claim that the project has been successfully built or packaged on a current machine.

## Project and toolchain configuration

The project is a Maven JAR with coordinates `com.myjavaworld:jftp:5.0.2-SNAPSHOT`. The project name and description in `pom.xml` are `jftp` and `The Universal FTP Client`. The only declared Maven property is `project.build.sourceEncoding=UTF-8`.

The Maven compiler plugin is `org.apache.maven.plugins:maven-compiler-plugin:2.4`, configured with `<source>1.5</source>` and `<target>1.5</target>`. The checked-in Eclipse settings disagree with Maven: `.classpath` selects `JavaSE-1.6`, while `.settings/org.eclipse.jdt.core.prefs` sets compiler compliance, source, and target to `1.6`. These are observed settings, not a verified statement about the source code's actual compatibility.

There is no Maven wrapper (`mvnw`), Gradle build, or other build wrapper/configuration in the repository root. The Eclipse project metadata in `.project` enables the Java builder and Maven/m2e nature. No `module-info.java` was found in the inspected build/configuration inventory.

## Direct dependencies

The dependencies declared in `pom.xml` are:

| Coordinate | Version | Scope in `pom.xml` | Purpose indicated by coordinates/project |
|---|---:|---|---|
| `junit:junit` | `3.8.1` | `test` | Test framework |
| `com.myjavaworld:ftpapi` | `3.0.0` | default compile scope | FTP library |
| `javax.help:javahelp` | `2.0.05` | default compile scope | Java Help integration |

The POM also declares the `jMethods` Maven repository at `http://www.jMethods.com/mvn-repo`. The POM does not state that any dependency is vendored locally. Whether this repository and the `ftpapi` artifact are currently reachable/resolvable has not been verified.

## Maven plugins and release configuration

The plugins and build extension pinned in `pom.xml` are:

| Plugin/extension | Version | Configured role |
|---|---:|---|
| `maven-compiler-plugin` | `2.4` | Compiles with Java source/target 1.5 |
| `maven-jar-plugin` | `2.4` | Adds implementation/specification manifest entries, manifest classpath, and main class |
| `maven-source-plugin` | `2.1.2` | Attaches a sources JAR through the `jar` goal |
| `maven-assembly-plugin` | `2.3` | Runs the `single` goal in `package` using `src/main/assembly/binary.xml` |
| `maven-scm-plugin` | `1.7` | Has a `tag` execution configured with `developerConnection` |
| `maven-deploy-plugin` | `2.7` | Deployment plugin |
| `maven-release-plugin` | `2.3` | Uses release profile `release` and goal `deploy` |
| `org.apache.maven.wagon:wagon-ftp` build extension | `2.2` | FTP Wagon transport extension |

The POM's SCM connection points at `https://spullabhotla@github.com/jftp.git`; its developer connection is `git@github.com:spullabhotla/jftp.git`. `distributionManagement` configures a repository at `ftp://ftp.kattare.com/jmethods_com/mvn-repo` and sets `uniqueVersion` to `false`. These are historical configured endpoints; their current availability and intended use are unknown.

## Resources and application entry point

`pom.xml` explicitly adds these resource directories to the main artifact:

- `src/main/resources`
- `src/main/resources_de`
- `src/main/resources_zh_TW`
- `src/main/images`
- `src/main/help`

The JAR manifest configuration in `maven-jar-plugin` sets `Main-Class` to `com.myjavaworld.jftp.JFTPApplication`, enables manifest classpath entries, and sets `classpathPrefix` to `lib/`. The configured entry point indicates the intended launch class; successful startup has not been verified.

## Assembly and launch scripts

`src/main/assembly/binary.xml` defines assembly ID `bin`, includes a base directory, and requests `zip`, `dir`, and `tar.gz` formats. Its dependency set excludes the project artifact and places transitive dependencies in `lib`. A separate file set copies JAR files from `${project.build.directory}` into the assembly root, excluding `*-sources.jar`. Another file set includes root-level `*.txt` and `*.md` files. The final file set copies and filters `${project.build.scriptSourceDirectory}` into the assembly root.

The scripts in `src/main/scripts` contain these commands:

- `jftp.sh`: `java -jar lib/${project.artifactId}-${project.version}.jar`
- `jftp.bat`: `java -jar lib\${project.artifactId}-${project.version}.jar`

As written, the assembly descriptor's project-JAR file set targets the assembly root, while the scripts expect the project JAR under `lib`. The dependency set does target `lib`, but explicitly sets `useProjectArtifact` to `false`. This is an apparent layout inconsistency in the configuration. The actual generated assembly contents and whether filtering or another configuration changes that layout have not been checked by running Maven.

## Repository-described product

`README.md` describes JFTP as a graphical Java FTP client. It lists FTP transfers, SSL/TLS, SOCKS proxies, local and remote file operations, and English, German, and Traditional Chinese language packs. It does not document a Java requirement, Maven build command, or launch procedure. This summary reflects README claims and is not a runtime verification.

## Observed build and runtime hazards

- Maven requests Java 5 source and bytecode output; the checked-in Eclipse configuration instead requests Java 6. Current-JDK behavior has not been tested, but this old source/target configuration is a likely compatibility blocker.
- The pinned Maven compiler, JAR, assembly, release, and other plugins are old. Their ability to run under a contemporary Maven/JDK has not been tested.
- Dependency resolution may rely on the POM's HTTP `jMethods` repository, including for `com.myjavaworld:ftpapi:3.0.0`. Artifact availability is unknown.
- The configured FTP distribution repository and `wagon-ftp` extension are legacy release/deployment configuration. Whether any current development workflow still needs them is unknown.
- The manifest names `com.myjavaworld.jftp.JFTPApplication` and scripts reference the project JAR under `lib`, while the assembly descriptor appears to copy the project JAR to the assembly root. Packaged launch behavior is unverified.
- The README provides no documented setup or run instructions, and the repository has no build wrapper.

## Verification status

This document was prepared by inspecting `pom.xml`, `README.md`, `src/main/assembly/binary.xml`, `src/main/scripts/jftp.sh`, `src/main/scripts/jftp.bat`, `.classpath`, `.project`, and `.settings` configuration. No Maven build, package/assembly generation, test suite, or application launch was run for this inventory. Any prediction above about compatibility, artifact resolution, or generated archive layout is therefore an assumption based on the checked-in configuration, not an observed build result.
